
### Node-1
```
besu --data-path=data --genesis-file=../genesis.json --permissions-nodes-config-file-enabled --permissions-accounts-config-file-enabled --rpc-http-enabled --rpc-http-api=ADMIN,ETH,NET,PERM,IBFT --host-allowlist="*" --rpc-http-cors-origins="*" --metrics-enabled --metrics-category="BLOCKCHAIN,PEERS,PROCESS,ETHEREUM,EXECUTORS,JVM,NETWORK,PERMISSIONING,PRUNER,RPC,STRATUM,SYNCHRONIZER,TRANSACTION_POOL,KVSTORE_ROCKSDB,KVSTORE_PRIVATE_ROCKSDB,KVSTORE_ROCKSDB_STATS,KVSTORE_PRIVATE_ROCKSDB_STATS" \
     --metrics-enabled=true \
     --metrics-host="0.0.0.0" \
     --metrics-port="9545" \
     --metrics-protocol="PROMETHEUS" \
     --metrics-push-enabled=false
```

### Node-2
```
besu --data-path=data --genesis-file=../genesis.json --permissions-nodes-config-file-enabled --permissions-accounts-config-file-enabled --rpc-http-enabled --rpc-http-api=ADMIN,ETH,NET,PERM,IBFT --host-allowlist="*" --rpc-http-cors-origins="*" --p2p-port=30304 --rpc-http-port=8546 --metrics-category="BLOCKCHAIN,PEERS,PROCESS,ETHEREUM,EXECUTORS,JVM,NETWORK,PERMISSIONING,PRUNER,RPC,STRATUM,SYNCHRONIZER,TRANSACTION_POOL,KVSTORE_ROCKSDB,KVSTORE_PRIVATE_ROCKSDB,KVSTORE_ROCKSDB_STATS,KVSTORE_PRIVATE_ROCKSDB_STATS" \
     --metrics-enabled=true \
     --metrics-host="0.0.0.0" \
     --metrics-port="9546" \
     --metrics-protocol="PROMETHEUS" \
     --metrics-push-enabled=false
```

### Node-3
```
besu --data-path=data --genesis-file=../genesis.json --permissions-nodes-config-file-enabled --permissions-accounts-config-file-enabled --rpc-http-enabled --rpc-http-api=ADMIN,ETH,NET,PERM,IBFT --host-allowlist="*" --rpc-http-cors-origins="*" --p2p-port=30305 --rpc-http-port=8547 --metrics-category="BLOCKCHAIN,PEERS,PROCESS,ETHEREUM,EXECUTORS,JVM,NETWORK,PERMISSIONING,PRUNER,RPC,STRATUM,SYNCHRONIZER,TRANSACTION_POOL,KVSTORE_ROCKSDB,KVSTORE_PRIVATE_ROCKSDB,KVSTORE_ROCKSDB_STATS,KVSTORE_PRIVATE_ROCKSDB_STATS" \
     --metrics-enabled=true \
     --metrics-host="0.0.0.0" \
     --metrics-port="9547" \
     --metrics-protocol="PROMETHEUS" \
     --metrics-push-enabled=false
```

### Node-4
```
besu --data-path=data --genesis-file=../genesis.json --permissions-nodes-config-file-enabled --permissions-accounts-config-file-enabled --rpc-http-enabled --rpc-http-api=ADMIN,ETH,NET,PERM,IBFT --host-allowlist="*" --rpc-http-cors-origins="*" --p2p-port=30306 --rpc-http-port=8548 --metrics-category="BLOCKCHAIN,PEERS,PROCESS,ETHEREUM,EXECUTORS,JVM,NETWORK,PERMISSIONING,PRUNER,RPC,STRATUM,SYNCHRONIZER,TRANSACTION_POOL,KVSTORE_ROCKSDB,KVSTORE_PRIVATE_ROCKSDB,KVSTORE_ROCKSDB_STATS,KVSTORE_PRIVATE_ROCKSDB_STATS" \
     --metrics-enabled=true \
     --metrics-host="0.0.0.0" \
     --metrics-port="9548" \
     --metrics-protocol="PROMETHEUS" \
     --metrics-push-enabled=false
```