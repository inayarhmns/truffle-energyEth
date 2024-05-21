


# How to Run
Keterangan: `#Checkpoint` adalah milestone dalam pengerjaan.


### Deploy Solidity Contract
Di proyek ini, jalankan `truffle migrate --network besuWallet`. 
> #Checkpoint: Setelah selesai, di sini contract solidity sudah di-deploy dan diakses node-node BESU. Cek `./build/contracts/*` jika sudah ada file json maka sudah berhasil.


### Run Permissioned network IBFT
Permissioned network IBFT ada pada repo https://github.com/AdyatmaWAN/BesuNodes. Jalankan setiap node besu dengan cara sama seperti start node di https://besu.hyperledger.org/23.4.0/private-networks/tutorials/permissioning#4-copy-the-genesis-file-to-the-permissioned-network-directory. 
> #Checkpoint: Di sini api besu dari localhost:8545, localhost:8546, localhost:8547, localhost:8548 harusnya sudah bisa diakses.

Lalu, jalankan curl ke beberapa api untuk konfigurasi node awal. Cara menjalankan api (dengan powershell) ada di file `./docs/SetupNode.md`.


### Start Web3signer
Di proyek ini, jalankan
`web3signer --key-store-path=./keyFiles/pem/ eth1 --chain-id=1337 --downstream-http-port=8545`
> #Checkpoint: Di sini, kita sudah bisa akses api BESU menggunakan portnya web3signer. Coba akses endpoint BESU dengan ganti localhost:8545 menjadi localhost:9000 (url web3signer)
### Run Python Code
Di proyek ini, jalankan `py src/networks/ibft/interaction/<NamaFile>.py`. Address contracts yang sudah dideploy ada di `compiled_contracts.txt`
> #Checkpoint: Di sini transaksi sudah bisa dilakukan.


# Ongoing Revision
### Mengubah akun pada web3signer menjadi akun yang tidak terikat pada node
Dari How to Run di atas, pada bagian Start Web3signer, `web3signer --key-store-path=./keyFiles/ eth1 --chain-id=1337 --downstream-http-port=8545`, di `.keyFiles/ ` akan dibuat private key baru yang bukan merupakan private key node. Private key akan dibuat dengan cara:
>Ganti ec-secp256k1-priv-key sesuai dengan nama key yg mau dibuat.
- Generate private key:
`openssl ecparam -name secp256k1 -genkey -noout -out keyFiles/ec-secp256k1-priv-key.pem`
- Encode ke hex: `openssl ec -in keyFiles/ec-secp256k1-private.pem -text -noout`
- Parse ke bentu 0x.. dengan masukkan hasil hex ke parser.py, lalu jalankan. (`py keyFiles/parser.py`)
- Buat key config yaml yang baru. Hasilnya masukkan ke private key di yaml filenya.







## REFERENCES:
- penggunaan truffle: https://medium.com/@ajith-m-doodlebug/compile-test-and-deploy-your-smart-contracts-using-truffle-a11371bd6dcc
- membuat private key dengan openssl: https://techdocs.akamai.com/iot-token-access-control/docs/generate-ecdsa-keys

