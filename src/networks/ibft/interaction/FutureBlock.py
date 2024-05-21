
from web3 import Web3, HTTPProvider
import json
import FlexCoin
from web3.middleware import geth_poa_middleware
import time
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


def wait_for_receipt(tx_hash, timeout=120):
    start_time = time.time()
    while True:
        try:
            receipt = web3.eth.get_transaction_receipt(tx_hash)
            if receipt is not None:
                return receipt
        except:
            pass
        time.sleep(0.5)
        if time.time() - start_time > timeout:
            raise TimeoutError(f"Transaction {tx_hash} not confirmed in {timeout} seconds")



def testFutureBlock():
    tempCost = []
    # Creating a new offer
    tx_hash = FutureBlock.functions.newOffer(15, 150, 180).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(tx_hash)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for new offer: {receipt.gasUsed}")
    numOffers = FutureBlock.functions.numOffers().call()

    # Placing bids
    for i in range(0, 10):
        tx_hash = FutureBlock.functions.setBid(numOffers, 10, 40).transact({
            'from': web3.eth.accounts[i],
            'gas': 1000000,
            'gasPrice': 0,
            'nonce': web3.eth.get_transaction_count(web3.eth.accounts[i]),
        })
        receipt = wait_for_receipt(tx_hash)
        tempCost.append(receipt.gasUsed)
        print(f"Gas used for placing bid from account {i}: {receipt.gasUsed}")

    # Updating bids
    update_bid_tx = FutureBlock.functions.updateBid(numOffers, 0, 19, 29).transact({
        'from': web3.eth.accounts[1],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[1]),
    })
    receipt = wait_for_receipt(update_bid_tx)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for updating bid: {receipt.gasUsed}")

    # Setting accepted price
    accepted_price_tx = FutureBlock.functions.setAcceptedPrice(numOffers, 30).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(accepted_price_tx)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for setting accepted price: {receipt.gasUsed}")

    # Setting accepted bids
    accepted_bids_tx_1 = FutureBlock.functions.setAcceptedBids(numOffers, 2).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(accepted_bids_tx_1)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for setting accepted bids (2): {receipt.gasUsed}")

    accepted_bids_tx_2 = FutureBlock.functions.setAcceptedBids(numOffers, 1).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(accepted_bids_tx_2)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for setting accepted bids (1): {receipt.gasUsed}")

    # Transfer and close
    transfer_close_tx = FutureBlock.functions.transferAndClose(numOffers, FlexCoin.address).transact({
        'from': web3.eth.accounts[0],
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(web3.eth.accounts[0]),
    })
    receipt = wait_for_receipt(transfer_close_tx)
    tempCost.append(receipt.gasUsed)
    print(f"Gas used for transfer and close: {receipt.gasUsed}")

    return tempCost

Costs = testFutureBlock()