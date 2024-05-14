# API BESU Example
Berisi API BESU yang dapat dicoba. Prerequisite: web3signer sudah start. Params bisa berubah sesuai dengan accounts yang ada.

1. get accounts
```
Invoke-RestMethod -Method Post -Uri 'http://127.0.0.1:9000' -Body '{"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1}' -ContentType 'application/json'
```
2. add account to allow list
``` 
Invoke-RestMethod -Uri 'http://127.0.0.1:8545' -Method Post -Body '{"jsonrpc":"2.0","method":"perm_addAccountsToAllowlist","params":[["0x9a3DBCa554e9f6b9257aAa24010DA8377C57c17e"]], "id":1}' -ContentType 'application/json'
```
3. Lihat peer dari suatu node (port bisa berubah sesuai dengan port node: 8554, 8546, dst.)
```
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8545" -Body '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}' -ContentType "application/json"
```