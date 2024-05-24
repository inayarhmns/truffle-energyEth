


# IBFT for economic feasibility of LEM in energyEth
[energyEth](https://github.com/fredrbl/energyEth/tree/master) adalah platform bisnis yang memanfaatkan Local Energy Market (LEM) untuk memfasilitasi perdagangan energi terbarukan secara terdesentralisasi yang dilakukan oleh Fredrik Blom dan Hossein Farahmand, 2018. 
<br>
### Dependensi
- Hyperledger Besu
- Web3Signer
- Truffle (dan dependensi tambahan pada [package.json](https://github.com/inayarhmns/truffle-energyEth/blob/master/package.json))


## Langkah-langkah Pengerjaan

### 1. Jalankan permissioned network IBFT
Untuk menjalankan permissioned network IBFT, perlu menjalankan setiap node pada repository [BesuNodes](https://github.com/AdyatmaWAN/BesuNodes). Jalankan setiap node dengan command yang ada pada [start_besu](https://github.com/inayarhmns/truffle-energyEth/blob/master/commands/start_besu.md) pada directory setiap nodes.
> Setelah langkah ini, ada 4 proses yang berjalan dengan 4 port yang berbeda-beda. API Besu dari localhost:8545, localhost:8546, localhost:8547, localhost:8548 sudah bisa diakses.


### 2. Deploy Solidity Contract
Untuk melakukan deploy solidity contract, di proyek ini jalankan `truffle migrate --network besuWallet`. 
> Setelah dijalankan, contract solidity sudah di-deploy dan dapat dilihat sebagai file JSON pada [/build/contracts](https://github.com/inayarhmns/truffle-energyEth/tree/master/build/contracts).




Lalu, jalankan curl ke beberapa api untuk konfigurasi node awal. Di antaranya untuk menambahkan peer dan menambahkan accounts yang di allow. Cara menjalankan api (dengan powershell) ada di file [./command/connect_node.md](https://github.com/inayarhmns/truffle-energyEth/blob/master/commands/connect_node.md).


### 3. Start Web3signer
Di proyek ini, jalankan
`web3signer --key-store-path=./keyFiles/pem/ eth1 --chain-id=1337 --downstream-http-port=8545`
> Di sini, kita sudah bisa akses api Besu menggunakan portnya web3signer. Coba akses endpoint Besu dengan ganti localhost:8545 menjadi localhost:9000 (url web3signer)

### 4. Lihat akun yang terdaftar dan tambahkan agar diberi permission
Di proyek ini, jalankan
seperti yang ada pada file [add_perm](https://github.com/inayarhmns/truffle-energyEth/blob/master/commands/add_perm.md)

### 5. Run Python Code
Di proyek ini, jalankan `py src/networks/ibft/interaction/<NamaFile>.py`. Address contracts yang sudah dideploy ada di `compiled_contracts.txt`
> Di sini transaksi sudah bisa dilakukan.


# Tutorial tambahan: Membuat akun baru
Untuk membuat akun baru, harus dibuat private key baru, masukkan ke dalam file `.yaml`, lalu pindahkan pada `/keyFiles/pem/`. Berikut ini langkah secara general:
- Generate private key:
`openssl ecparam -name secp256k1 -genkey -noout -out keyFiles/ec-secp256k1-priv-key.pem`
- Encode ke hex: `openssl ec -in keyFiles/ec-secp256k1-private.pem -text -noout`
- Parse ke bentu 0x.. dengan masukkan hasil hex ke parser.py, lalu jalankan. (`py keyFiles/parser.py`)
- Buat key config yaml yang baru. Hasilnya masukkan ke private key di yaml filenya.







## REFERENCES:
- penggunaan truffle: https://medium.com/@ajith-m-doodlebug/compile-test-and-deploy-your-smart-contracts-using-truffle-a11371bd6dcc
- membuat private key dengan openssl: https://techdocs.akamai.com/iot-token-access-control/docs/generate-ecdsa-keys

