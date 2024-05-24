
### Menambahkan peer
```
curl -X POST http://127.0.0.1:8546 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}'

curl -X POST http://127.0.0.1:8547 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}'

curl -X POST http://127.0.0.1:8548 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://6bb556f960d5b8dc23065e6a294b5b45336a3f7dfa1bc6822a19bf5c8634ad19f7ba10f094cdad53fbd4b9aa31da6253946d5b276889a664d3d7de3ff23fa9b8@127.0.0.1:30303"],"id":1}'

curl -X POST http://127.0.0.1:8547 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304"],"id":1}'

curl -X POST http://127.0.0.1:8548 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"admin_addPeer","params":["enode://727809fef0c460efc6bc09b8a5a06d266f8b719ca46c365c6e9c21a59c1284a5a684613953c24632aa408c54c33dad9092e132505dd010a8a22cd653fce2727a@127.0.0.1:30304"],"id":1}'

# Cek seharusnya bernilai 3
curl -X POST http://127.0.0.1:8545 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":1}'


```
