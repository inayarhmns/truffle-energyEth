# Setup Node API BESU
1.
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8545" -Body '{"jsonrpc":"2.0","method":"perm_addNodesToAllowlist","params":[["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303","enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304","enode://0b71288b6aed0b0eaa20c84c8998a418789405364442611a854c3c73daaa5c320dcc0cfbc6149ea92c704a502e5092d35b15f1607cfe11879e389df8ac1e5e4c@127.0.0.1:30305","enode://a2cc13ad43ee2a36f37bbe131ed227c8a586c7f64551c75aadefa44ca8c935d54647ab13f314ee2588df1fecda25ff5531f076ceed48c1df4b29dced3e117325@127.0.0.1:30306"]], "id":1}' -ContentType "application/json"
```

2.
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8546" -Body '{"jsonrpc":"2.0","method":"perm_addNodesToAllowlist","params":[["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303","enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304","enode://0b71288b6aed0b0eaa20c84c8998a418789405364442611a854c3c73daaa5c320dcc0cfbc6149ea92c704a502e5092d35b15f1607cfe11879e389df8ac1e5e4c@127.0.0.1:30305","enode://a2cc13ad43ee2a36f37bbe131ed227c8a586c7f64551c75aadefa44ca8c935d54647ab13f314ee2588df1fecda25ff5531f076ceed48c1df4b29dced3e117325@127.0.0.1:30306"]], "id":1}' -ContentType "application/json"
```

3.
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8547" -Body '{"jsonrpc":"2.0","method":"perm_addNodesToAllowlist","params":[["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303","enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304","enode://0b71288b6aed0b0eaa20c84c8998a418789405364442611a854c3c73daaa5c320dcc0cfbc6149ea92c704a502e5092

d35b15f1607cfe11879e389df8ac1e5e4c@127.0.0.1:30305","enode://a2cc13ad43ee2a36f37bbe131ed227c8a586c7f64551c75aadefa44ca8c935d54647ab13f314ee2588df1fecda25ff5531f076ceed48c1df4b29dced3e117325@127.0.0.1:30306"]], "id":1}' -ContentType "application/json"
```

4.
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8548" -Body '{"jsonrpc":"2.0","method":"perm_addNodesToAllowlist","params":[["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303","enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304","enode://0b71288b6aed0b0eaa20c84c8998a418789405364442611a854c3c73daaa5c320dcc0cfbc6149ea92c704a502e5092d35b15f1607cfe11879e389df8ac1e5e4c@127.0.0.1:30305","enode://a2cc13ad43ee2a36f37bbe131ed227c8a586c7f64551c75aadefa44ca8c935d54647ab13f314ee2588df1fecda25ff5531f076ceed48c1df4b29dced3e117325@127.0.0.1:30306"]], "id":1}' -ContentType "application/json"
```

5.
```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8546" -Body '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}' -ContentType "application/json"

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8547" -Body '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}' -ContentType "application/json"

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8548" -Body '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}' -ContentType "application/json"

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8547" -Body '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304"],"id":1}' -ContentType "application/json"

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8548" -Body '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304"],"id":1}' -ContentType "application/json"

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8545" -Body '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}' -ContentType "application/json"
