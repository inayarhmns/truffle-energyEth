from web3 import Web3, HTTPProvider
import json
from web3.middleware import geth_poa_middleware
# This function makes a house to each node in the system

host = 'http://127.0.0.1:9000'  # Web3Signer URL

web3 = Web3(HTTPProvider(host))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
jsonFile = open('./build/contracts/FlexCoin.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

abi = values['abi']

address = input("What is the contract address? - FlexCoin: ")
FlexCoin = web3.eth.contract(address, abi=abi)

numHouses = FlexCoin.caller().numHouses()

print("Accounts:", str(web3.eth.accounts))
print("numHouses:", str(numHouses))


if (numHouses == 0):
    for i in range(len(web3.eth.accounts)):
        tx_hash = FlexCoin.functions.newHouse().transact({'from': web3.eth.accounts[i],'gas': 1000000,
            'gasPrice': 0,
            'nonce': web3.eth.get_transaction_count(web3.eth.accounts[i]),})
        print("transact from " + str(web3.eth.accounts[i]))
        print("transaction: " + str(tx_hash))
else:
    for i in range(len(web3.eth.accounts)):
        account = web3.eth.accounts[i]
        eth_balance = web3.eth.get_balance(account)
        flexcoin_balance = FlexCoin.functions.getHouse(account).call()

        print(f'House {i} - ETH: {eth_balance}, FlexCoin: {flexcoin_balance}\n')
# Test Flexcoin transfer
    account_1 = web3.eth.accounts[0]
    account_2 = web3.eth.accounts[1]

    print(f'Transferring FlexCoin from {account_1} to {account_2}')
    tx_hash = FlexCoin.functions.transferHouse(account_1, account_2, 1).transact({
        'from': account,
        'gas': 1000000,
        'gasPrice': 0,
        'nonce': web3.eth.get_transaction_count(account),
    })
    web3.eth.wait_for_transaction_receipt(tx_hash)
    
    # Flexcoin balance after transfer
    flexcoin_balance_1 = FlexCoin.functions.getHouse(account_1).call()
    flexcoin_balance_2 = FlexCoin.functions.getHouse(account_2).call()
    
    print(f'House 1 - FlexCoin: {flexcoin_balance_1}')
    print(f'House 2 - FlexCoin: {flexcoin_balance_2}')