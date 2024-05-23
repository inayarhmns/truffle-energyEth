from web3 import Web3, HTTPProvider
import json
from web3.middleware import geth_poa_middleware

# This function makes a house to each node in the system

host = 'http://localhost:9000'  # Web3Signer URL

web3 = Web3(HTTPProvider(host))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

jsonFile = open('./build/contracts/FlexCoin.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

abi = values['abi']

address = input("What is the contract address? - FlexCoin: ")
FlexCoin = web3.eth.contract(address, abi=abi)

numHouses = FlexCoin.functions.numHouses().call()

print("Number of houses:", numHouses)
print("Number of accounts:", len(web3.eth.accounts))
print("Accounts:", web3.eth.accounts)

if (numHouses == 0):
    for i in range(len(web3.eth.accounts)):
        account = web3.eth.accounts[i]
        tx_hash = FlexCoin.functions.newHouse().transact({
            'from': account,
            'gas': 1000000,
            'gasPrice': 0,
            'nonce': web3.eth.get_transaction_count(account),
        })
        print("House made for node: ", i)
        print(f'Transaction Hash: {tx_hash.hex()}')