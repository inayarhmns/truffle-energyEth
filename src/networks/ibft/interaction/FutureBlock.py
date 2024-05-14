
from web3 import Web3, HTTPProvider
import json
import FlexCoin
from web3.middleware import geth_poa_middleware

# Compile and deploy in populus in one terminal and testrpc-py in another
# Open a new terminal and rund this python script in python3

host = 'http://127.0.0.1:9000'  # Web3Signer URL

web3 = Web3(HTTPProvider(host))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

jsonFile = open('./build/contracts/FutureBlock.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

abi = values['abi']
address = input("What is the contract address? - FutureBlock: ")
FutureBlock = web3.eth.contract(address, abi = abi)
cost = 0
print("Accounts:", str(web3.eth.accounts))

####### Isolate and test the mechanism ###########
# This is creating 25 bids, accetps three, and closes
def testFutureBlock():
    tempCost = []
    tempCost.append(FutureBlock.functions.newOffer(15, 150, 180).transact({'from': web3.eth.accounts[0]}))
    a = FutureBlock.caller().numOffers()
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[1]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[2]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[3]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[4]})
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[5]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[6]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[7]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[8]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[9]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[1]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[2]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[3]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[5]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[6]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[3]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[5]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[4]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[5]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[6]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[7]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[8]}))
    tempCost.append(FutureBlock.functions.setBid(a, 10, 40).transact({'from': web3.eth.accounts[2]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 5, 50).transact({'from': web3.eth.accounts[6]}))
    # tempCost.append(FutureBlock.functions.setBid(a, 10, 30).transact({'from': web3.eth.accounts[7]}))
    tempCost.append(FutureBlock.functions.updateBid(a, 0, 19, 29).transact({'from': web3.eth.accounts[1]}))
    tempCost.append(FutureBlock.functions.setAcceptedPrice(a, 30).transact({'from': web3.eth.accounts[0]}))
    tempCost.append(FutureBlock.functions.setAcceptedBids(a, 2).transact({'from': web3.eth.accounts[0]}))
    tempCost.append(FutureBlock.functions.setAcceptedBids(a, 1).transact({'from': web3.eth.accounts[0]}))
    print("Flexcoin address: " + str(FlexCoin.address))
    print("a: " + str(a))

    tempCost.append(FutureBlock.functions.transferAndClose(a, FlexCoin.address).transact())
    for i in range(0,len(tempCost)):
        tempCost[i] = web3.eth.get_transaction_receipt(tempCost[i]).gasUsed
        print(f"tempCost: {i}: " + str(tempCost[i]))

    return tempCost

Costs = testFutureBlock()
