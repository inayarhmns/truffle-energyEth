# API BESU Example
Berisi API BESU yang dapat dicoba. Prerequisite: web3signer sudah start. Params bisa berubah sesuai dengan accounts yang ada.

1. Get ethereum accounts
```
curl -X POST http://127.0.0.1:9000 \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}'

```
2. Add account to allow list
<br>
Dari accounts yang didapat dari no. 1, tambahkan pada params berikut.
```
curl -X POST http://127.0.0.1:8545 \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","method":"perm_addAccountsToAllowlist","params":[<list acccounts>],"id":1}'

``` 
contoh:
`curl -X POST http://127.0.0.1:8545 \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","method":"perm_addAccountsToAllowlist","params":[["0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e"]],"id":1}'`




