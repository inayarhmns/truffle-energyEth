
# Followup after initialiseSystem
import copy
from web3 import Web3, HTTPProvider
import json
import random
import match
import time
import numpy as np
import matplotlib.pyplot as plt
from web3.middleware import geth_poa_middleware

# Compile and deploy in populus in one terminal and testrpc-py in another
# Open a new terminal and run this python script in python3
host = 'http://127.0.0.1:9000'  # Web3Signer URL

web3 = Web3(HTTPProvider(host))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
jsonFile = open('./build/contracts/RealTime.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

abi = values['abi']
address = input("What is the contract address? - RealTime: ")
RealTime = web3.eth.contract(address=address, abi = abi)

# Load and parse the ABI for FlexCoin
jsonFileFlexCoin = open('./build/contracts/FlexCoin.json', 'r')
valuesFlexCoin = json.load(jsonFileFlexCoin)
jsonFileFlexCoin.close()
abiFlexCoin = valuesFlexCoin['abi']
addressFlexCoin = input("What is the contract address? - FlexCoin: ")
FlexCoin = web3.eth.contract(address=addressFlexCoin, abi=abiFlexCoin)

createNodeCost = []

# Set how many nodes that should be simulated
testRange = range(4, 5, 1)

averageNode = [0 for i in testRange]
averageCentral = [0 for i in testRange]
numTxCentral = [0 for i in testRange]
numTxNodes = [0 for i in testRange]
numTxInitiate = [0 for i in testRange]

def wait_for_receipt(tx_hash, timeout=120):
# This function sets a price for the battery energy - i.e agent market decisions
    start_time = time.time()
    while True:
        try:
            receipt = web3.eth.get_transaction_receipt(tx_hash)
            if receipt is not None:
                return receipt
        except:
            pass
        time.sleep(1)
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Transaction {tx_hash} not confirmed in {timeout} seconds")
def setPrice(battery, numHouses):
    """
    This function sets a price for the battery energy - i.e agent market decisions.
    The price is set under 470 if the battery buys energy, and above 470 if the battery sells energy.
    """
    price = [[0 for _ in range(numHouses)] for _ in range(2)]

    for i in range(0, 10, 2):
        if battery[i] <= 6700:
            price[0][i] = random.randint(480, 590)
            price[1][i] = random.randint(350, 460)
        else:
            price[0][i] = random.randint(480, 590)
            price[1][i] = random.randint(350, 460)

    print(f"Prices set for battery: {price}")
    return price

def setFlexibility(battery, batteryFlag, numHouses):
    """
    This function sets the different battery levels.
    5000 w in one hour = 5000 wh => 833 w max in 10 minutes
    """
    availableFlex = [[0 for _ in range(numHouses)] for _ in range(2)]

    for i in range(numHouses):
        if 840 < battery[i] < 12500:
            availableFlex[0][i] = 700
            availableFlex[1][i] = 700
        elif battery[i] <= 840 and batteryFlag[i] == 1:
            availableFlex[0][i] = 0
            availableFlex[1][i] = 700
        elif battery[i] >= 12500:
            availableFlex[0][i] = 700
            availableFlex[1][i] = 0

    print(f"Flexibility set for battery: {availableFlex}")
    return availableFlex

def trade(numTxCentral, numTxNodes, numTxInitiate, price, battery, availableFlex, deviation, numHouses):
# This is the main function that does the trading.

    wholesalePrice = 470
    flexFlag = -1
    transactions = [[] for _ in range(3)]
    upPrice = [[0 for _ in range(numHouses)] for y in range(2)]
    upPrice[0] = [x for x in range(numHouses)]
    upPrice[1] = price[0]
    downPrice = [[0 for _ in range(numHouses)] for y in range(2)]
    downPrice[0] = [x for x in range(numHouses)]
    downPrice[1] = price[1]
    upAvailableFlex = [[0 for _ in range(numHouses)] for y in range(2)]
    upAvailableFlex[0] = [x for x in range(numHouses)]
    upAvailableFlex[1] = availableFlex[0] # This is used if the system needs less consumption
    downAvailableFlex = [[0 for _ in range(numHouses)] for y in range(2)]
    downAvailableFlex[0] = [x for x in range(numHouses)]
    downAvailableFlex[1] = availableFlex[1] # This is used if system needs more consumption
    demand = [[] for _ in range(2)]
    supply = [[] for _ in range(2)]
    updateCost = []
    nodeCost = 0
    centralCost = 0

    # Some houses have flexibility, and no deviation. Other houses have deviation, but no flex. Lets do 50/50
    # The for loop under is information gathering to the blockchain
    for i in range(numHouses):
        if i % 2 == 0:
            tx_hash = RealTime.functions.setRealTimeNodePrice(i, upPrice[1][i], downPrice[1][i]).transact({
                'from': web3.eth.accounts[0],
                'gas': 1000000,
                'gasPrice': 0,
                'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
            })
            receipt = wait_for_receipt(tx_hash)
            updateCost.append(receipt.gasUsed)
            print(f"Gas used for setting price for node {i}: {receipt.gasUsed}")

            tx_hash = RealTime.functions.setRealTimeNodeBattery(i, upAvailableFlex[1][i], downAvailableFlex[1][i], 0).transact({
                'from': web3.eth.accounts[0],
                'gas': 1000000,
                'gasPrice': 0,
                'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
            })
            receipt = wait_for_receipt(tx_hash)
            updateCost.append(receipt.gasUsed)
            print(f"Gas used for setting battery for node {i}: {receipt.gasUsed}")
            numTxNodes += 2
        else:
            tx_hash = RealTime.functions.setRealTimeNodePrice(i, 0, 0).transact({
                'from': web3.eth.accounts[0],
                'gas': 1000000,
                'gasPrice': 0,
                'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
            })
            receipt = wait_for_receipt(tx_hash)
            updateCost.append(receipt.gasUsed)
            print(f"Gas used for setting price for node {i}: {receipt.gasUsed}")

            tx_hash = RealTime.functions.setRealTimeNodeBattery(i, 0, 0, deviation[i]).transact({
                'from': web3.eth.accounts[0],
                'gas': 1000000,
                'gasPrice': 0,
                'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
            })
            receipt = wait_for_receipt(tx_hash)
            updateCost.append(receipt.gasUsed)
            print(f"Gas used for setting battery for node {i}: {receipt.gasUsed}")
            numTxNodes += 2


    # The for loop below is the central node fetching all information from the blockchain
    for i in range(0,numHouses):
        h = RealTime.functions.getRealTimeNode(i).call()
        if (h[5] < 0):
            demand[0].append(i)
            demand[1].append(-h[5])
        elif (h[5] > 0):
            supply[0].append(i)
            supply[1].append(h[5])

    # Here, the match.py script is used to match supply and demand
    flexFlag, transactions, restEnergy = match.matching(flexFlag, transactions, demand, supply)


    numTransactionsFirstRound = len(transactions[0])
    if(sum(restEnergy[1]) == 0):  # This means that supply and demand cancel each other, and no more trading is necessary
        flexFlag = 2
        marketPrice = wholesalePrice

    sortedPrice = [[0 for _ in range(numHouses)] for y in range(2)]
    copySortedPrice = [[0 for _ in range(numHouses)] for y in range(2)]

    # If supply and demand do not cancel each other, we must utilise the batteries to cancel the deviations
    i = 0
    if (flexFlag == 0):
        demandFlex = copy.deepcopy(upAvailableFlex)
        supplyFlex = restEnergy
        sortedPrice = copy.deepcopy(upPrice)
        copySortedPrice = copy.deepcopy(upPrice)
        sortedPrice[1] = sorted(sortedPrice[1])
        for i in range(len(upPrice[1])):
            sortedPrice[0][i] = copySortedPrice[0][copySortedPrice[1].index(sortedPrice[1][i])]
            demandFlex[1][i] = upAvailableFlex[1][copySortedPrice[1].index(sortedPrice[1][i])]
            demandFlex[0][i] = sortedPrice[0][i]
            copySortedPrice[1][copySortedPrice[1].index(sortedPrice[1][i])] = -1
    else:
        demandFlex = restEnergy
        supplyFlex = copy.deepcopy(downAvailableFlex)
        sortedPrice = copy.deepcopy(downPrice)
        copySortedPrice = copy.deepcopy(downPrice)
        sortedPrice[1] = sorted(sortedPrice[1], reverse = True)
        for i in range(len(downPrice[1])):
            sortedPrice[0][i] = copySortedPrice[0][copySortedPrice[1].index(sortedPrice[1][i])]
            supplyFlex[1][i] = downAvailableFlex[1][copySortedPrice[1].index(sortedPrice[1][i])]
            supplyFlex[0][i] = sortedPrice[0][i]
            copySortedPrice[1][copySortedPrice[1].index(sortedPrice[1][i])] = -1

    firstFlexFlag = copy.deepcopy(flexFlag)

    # The line below matches the batteries with the rest energy
    flexFlag, transactions, restEnergy = match.matching(flexFlag, transactions, demandFlex, supplyFlex)

    # The part below finds the market price
    if (firstFlexFlag == 0):
        if(flexFlag == 0):
            wholesale = sum(restEnergy[1])
            marketPrice = wholesalePrice
            lastBattery = -1
            print("The system are still ",wholesale," kWh over the bid amount")
        else:
            lastBattery = transactions[1][len(transactions[0]) - 1]
            marketPrice = sortedPrice[1][sortedPrice[0].index(lastBattery)]
            print('The systems batteries can cover the deviations')
    elif(firstFlexFlag == 1):
        if(flexFlag == 0):
            lastBattery = transactions[0][len(transactions[0]) - 1]
            marketPrice = sortedPrice[1][sortedPrice[0].index(lastBattery)]
            print('The systems batteries can cover the deviations')
        else:
            wholesale = sum(restEnergy[1])
            marketPrice = wholesalePrice
            lastBattery = -1
            print("The system are still ",wholesale," kWh under the bid amount")


    ################################################################################
    ### The calculation is done, and the transactions are performed in blockchain ##
    ################################################################################
    numTxCentral = len(transactions[0])
    print(len(transactions[0]), len(transactions[1]), len(transactions[2]))
    tx_hash = RealTime.functions.checkAndTransactList(firstFlexFlag, sortedPrice[0], sortedPrice[1], transactions[0], transactions[1], transactions[2], marketPrice, addressFlexCoin).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(tx_hash)
    transferCost = receipt.gasUsed
    print(f"Gas used for check and transact list: {transferCost}")
    centralCost = transferCost

    if (firstFlexFlag == 0):
        for i in range(numTransactionsFirstRound,len(transactions[0])):
            battery[transactions[1][i]] = battery[transactions[1][i]] - transactions[2][i]
    if (firstFlexFlag == 1):
        for i in range(numTransactionsFirstRound,len(transactions[0])):
            battery[transactions[0][i]] = battery[transactions[0][i]] + transactions[2][i]
    for i in range(0, len(updateCost)):
        nodeCost += updateCost[i]
    print(f"Total node cost: {nodeCost}")
    return(numTxCentral, numTxNodes, numTxInitiate, battery, marketPrice, nodeCost, centralCost)

######## Now, we could test the system over a certain set of time steps
def testRealTime(numHouses, numPeriods):

    #####################################################################################
    ####### The loop below is called if there not are premade sufficient houses in FlexCoin
    ####### If creates new nodes in the blockchain network, and giving them ether, which is necessary in order to trade
    ####### Thereafter, it is created a new house from its address
    #####################################################################################
    numHouses = min(numHouses, len(web3.eth.accounts)) 
    numTxCentral = 0
    numTxNodes = 0
    numTxInitiate = 0

    for i in range(numHouses):
        tx_hash = RealTime.functions.newRealTimeNode(web3.eth.accounts[i]).transact({
            'from': web3.eth.accounts[1],
            'gas': 1000000,
            'gasPrice': 0,
            'nonce': web3.eth.get_transaction_count(web3.eth.accounts[1])
        })
        receipt = web3.eth.wait_for_receipt(tx_hash)
        createNodeCost.append(receipt.gasUsed)
        print(f"Gas used for creating RealTime node ({i + 1}): {receipt.gasUsed}")
        numTxInitiate += 1

    deviation = [[0 for _ in range(numHouses)] for _ in range(numPeriods)]
    battery = [[0 for _ in range(numHouses)] for _ in range(numPeriods)]
    batteryFlag = [0 for _ in range(0,numHouses)]
    price = [[[0 for _ in range(numHouses)] for _ in range(0, 2)] for _ in range(numPeriods)]
    nodeCost = [0 for _ in range(numPeriods)]
    centralCost = [0 for _ in range(numPeriods)]
    flexCoinBalance = [[0 for _ in range(numHouses)] for _ in range(numPeriods)]

    for i in range(0, numHouses):
        if (i % 2 == 0):
            battery[0][i] = 6700
            batteryFlag[i] = 1

    ## Randomising deviations and price
    for i in range(0, numPeriods):
        for j in range(0, numHouses):
            deviation[i][j] = random.randint(-500, 500)
            price[i][0][j] = random.randint(480, 590)
            price[i][1][j] = random.randint(350, 460)

    for j in range(0,numHouses):
        _, flexCoinBalance[0][j] = FlexCoin.functions.getHouse(web3.eth.accounts[j]).call()
    marketPrice = [RealTime.functions.wholesalePrice().call() for _ in range(numPeriods)]

    for i in range(0, numPeriods): #144 for a whole day

        ### Setting the deviations.
        for j in range(0,numHouses):
            if ((battery[i - 1][j] > deviation[i][j]) and (battery[i - 1][j] < deviation[i][j] + 13500) and (batteryFlag[j] == 1)):
                battery[i][j] = battery[i - 1][j] + deviation[i][j]  # If deviation not is included, the batteries work without
                # deviation[i][j] = 0 # It is being set to zero later anyway
            else:
                if (deviation[i][j] < 0 and batteryFlag[j] == 1):
                    deviation[i][j] = deviation[i][j] + (13500 - battery[i][j])
                    battery[i][j] = 13500
                else:
                    deviation[i][j] = deviation[i][j] - battery[i][j]
                    battery[i][j] = 0

        ### Now, we must set the price based on the battery status. This thesis have chosen not to use this function, and rather use a randomised price for each time.
        ## If a user wants to set a different price (which should be done), it is recommended to use setPrice function.
        # price[i] = setPrice(battery[i])

        ### Set the available flexibility in each battery
        availableFlex = setFlexibility(battery[i], batteryFlag, numHouses)

        ### The trading happens, and the batteries are corrected for the trading
        numTxCentral, numTxNodes, numTxInitiate, battery[i], marketPrice[i], nodeCost[i], centralCost[i] = trade(numTxCentral, numTxNodes, numTxInitiate, price[i], battery[i], availableFlex, deviation[i], numHouses)
        for j in range(0,numHouses):
            if (battery[i][j] > battery[i - 1][j]):
                battery[i][j] = round(int(0.9 * battery[i][j]))
            _, flexCoinBalance[i][j] = FlexCoin.functions.getHouse(web3.eth.accounts[j]).call()

    averageNode = (sum(nodeCost)/numPeriods)
    averageCentral = sum(centralCost)/numPeriods
    return numTxCentral, numTxNodes, numTxInitiate, flexCoinBalance, battery, price, deviation, marketPrice, averageNode, averageCentral


#### The simulation is now performed. The main results is averageCentral and averageNode, where these provides with the gas results from the central calculation and the nodes
counter = 0
node = [0 for _ in testRange]
total = [0 for _ in testRange]
for i in testRange:
    numTxCentral[counter], numTxNodes[counter], numTxInitiate[counter], flexCoinBalance, battery, price, deviation, marketPrice, averageNode[counter], averageCentral[counter] = testRealTime(i, 1)
    total[counter] = node[counter] + averageCentral[counter]
    counter += 1
