from web3 import Web3
from web3 import EthereumTesterProvider
from fastapi import FastAPI
import math
from datetime import datetime
import pytz
app = FastAPI()

provider_url = 'https://rinkeby.infura.io/v3/5a5adcea95764d898c7e69d4c27f4c01'
w3 = Web3(Web3.HTTPProvider(provider_url))

#Member Smart Contract
abi = '[ { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" }, { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "name": "addBook", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "customer_id", "type": "string" } ], "name": "connect_user", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" } ], "name": "pop_me_baby", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct Project.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "pop_user", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "showARRAYS", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct Project.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" } ], "name": "showMAPPING", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct Project.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "show_user", "outputs": [ { "components": [ { "internalType": "string", "name": "_user_id", "type": "string" } ], "internalType": "struct Project.USER[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "warehouse", "outputs": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "stateMutability": "view", "type": "function" } ]'
contract_address = '0x337b92Be428e7E1d844b1Dc2CD3D2BDBf430A994'
contract_instance = w3.eth.contract(address = contract_address, abi = abi)

#Token Smart Contract
abi_ERC1155 = '[ { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "account", "type": "address" }, { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": false, "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "ApprovalForAll", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "_user", "type": "address" }, { "internalType": "uint256", "name": "_id", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "burnNFTS", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_user", "type": "address" }, { "internalType": "uint256", "name": "_id", "type": "uint256" }, { "internalType": "uint256", "name": "user_point", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "BurnPointAndMint", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "_user", "type": "address" }, { "internalType": "uint256", "name": "_id", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "giveNFTS", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeBatchTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "uint256", "name": "amount", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "safeTransferFrom", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "bool", "name": "approved", "type": "bool" } ], "name": "setApprovalForAll", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "indexed": false, "internalType": "uint256[]", "name": "values", "type": "uint256[]" } ], "name": "TransferBatch", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "operator", "type": "address" }, { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "id", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "TransferSingle", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "value", "type": "string" }, { "indexed": true, "internalType": "uint256", "name": "id", "type": "uint256" } ], "name": "URI", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address[]", "name": "accounts", "type": "address[]" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" } ], "name": "balanceOfBatch", "outputs": [ { "internalType": "uint256[]", "name": "", "type": "uint256[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" }, { "internalType": "address", "name": "operator", "type": "address" } ], "name": "isApprovedForAll", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" } ], "name": "supportsInterface", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_tokenid", "type": "uint256" } ], "name": "uri", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "pure", "type": "function" } ]'
contract_address_ERC1155 = '0x1B4f42f783C2f998d1820D585824182B9f27415b'
contract_instance_ERC1155 = w3.eth.contract(address = contract_address_ERC1155, abi = abi_ERC1155)

hardwallet = [['0x50f9828ddF89e10Dee9B2E28Db43E86111Df439C', '6a97002b83cdaccc96f0cf894987deed791ae6264effe3b861ac328392ff6e0e'],
['0x1a4aA41Da649C5Bae0628Abb33aF3d0e41e6b740', 'e9bc425c545831ff9b62750745ccf521177cd5653e03327d6e383505fefcd0f9'],
['0x03c0228ABEfAcDe73eFB8B1D72746955a044DB02', '022f894820933e615275d7625a862c46e337ce3a2b72c880d7a5ac022a1aea76'],
['0x960e8FF55267bE5412463be6c538fdAE93db5660', 'bdfca73534bf8c66a30e9a1949fc5fd250fce1c7bb21eedcdf15d9cf1b0cb113'],
['0x945c7D532ed938670e3086E5CE7e3409F292A8Dc', '270b2042ac78203360c80b84f3e7fd6f0b66c906050e06757778e4c1a480cae2'],
['0x76eb66596AA77351065d206418ece525DCf3eae4', '58287f1e7550f99cd03bdd1a2106ecc69cf4c72dd58b92b6e9966c36d86a08f2']]

@app.get("/")
async def show():
    return {"show":"It's working"}




















@app.get("/connect_wallet_dialog/{customer_id}")
async def connect_wallet(customer_id: str):
    users = contract_instance.functions.show_user().call()

    try:
        num_users = len(users)
    except:
        num_users = 0

    if num_users == len(hardwallet):
        hash = 'in_แจ้งwalletเต็ม'
    else:
        nonce = w3.eth.getTransactionCount('0xA393E6989E035b56718FdcE9D30Ff925879361B7')
        update_transaction = contract_instance.functions.connect_user(customer_id).buildTransaction(
            {
            'gas': 1800000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'from': '0xA393E6989E035b56718FdcE9D30Ff925879361B7',
            'nonce': nonce
            }
        )
        sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = 'c91fd9e0aae948763d13f6adf39d7077b41b1676dfe2cbca7b180201b2621f4c')
        transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        hash = 'in_สมัครสมาชิก_richmenu'    
    return {"hash" :hash, "i":str(num_users)}



@app.get("/connect_wallet_buying/{customer_id}")
async def connect_wallet(customer_id: str):
    users = contract_instance.functions.show_user().call()

    try:
        num_users = len(users)
    except:
        num_users = 0

    if num_users == len(hardwallet):
        hash = 'in_แจ้งwalletเต็ม'
    else:
        nonce = w3.eth.getTransactionCount('0xA393E6989E035b56718FdcE9D30Ff925879361B7')
        update_transaction = contract_instance.functions.connect_user(customer_id).buildTransaction(
            {
            'gas': 1800000,
            'gasPrice': w3.toWei('50', 'gwei'),
            'from': '0xA393E6989E035b56718FdcE9D30Ff925879361B7',
            'nonce': nonce
            }
        )
        sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = 'c91fd9e0aae948763d13f6adf39d7077b41b1676dfe2cbca7b180201b2621f4c')
        transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        hash = 'in_สมัครสมาชิก_เส้นสั่งซื้อ'    
    return {"hash" :hash, "i":str(num_users)}



@app.get("/pop_user")
async def pop_user():
    nonce = w3.eth.getTransactionCount('0xA393E6989E035b56718FdcE9D30Ff925879361B7')
    update_transaction = contract_instance.functions.pop_user().buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': '0xA393E6989E035b56718FdcE9D30Ff925879361B7',
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = 'c91fd9e0aae948763d13f6adf39d7077b41b1676dfe2cbca7b180201b2621f4c')
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"pop" :"user's poped"}



@app.get("/users")
async def users():
    total = contract_instance.functions.show_user().call()
    return {"total" : str(total)}



@app.get("/getcoin/{customer_id}&{price}")
async def getcoin(customer_id: str, price: int):
    score = math.floor(price/500)
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]
    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.giveNFTS(address, 0, int(score)).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"address":address, "private_key":privatekey, "score":score, "hash" :w3.toHex(transaction_hash)}



@app.get("/getcoin_buying/{customer_id}&{price}")
async def getcoin(customer_id: str, price: int):
    price = price + 50000
    score = math.floor(price/500)
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]
    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.giveNFTS(address, 0, int(score)).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"address":address, "private_key":privatekey, "score":score, "hash" :w3.toHex(transaction_hash)}



@app.get("/burn/{customer_id}&{price}")
async def burncoin(customer_id: str, price: int):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]

    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.burnNFTS(address, 0, int(price)).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"address":address, "private_key":privatekey, "score":price, "hash" :w3.toHex(transaction_hash)}



@app.get("/mycoin/{customer_id}")
async def mycoin(customer_id: str):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    the_coin = contract_instance_ERC1155.functions.balanceOf(address, 0).call()
    return {"total" : str(the_coin)}
















#NFTs
@app.get("/check_point_hobobag/{customer_id}")
async def mycoin(customer_id: str):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    customer_point = contract_instance_ERC1155.functions.balanceOf(address, 0).call()
    if customer_point >= 100:
        result = "hobobag_แลกได้"
    else:
        result = "hobobag_แต้มไม่ถึง"
    return {"result":result}



@app.get("/check_point_ricecooker/{customer_id}")
async def mycoin(customer_id: str):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    customer_point = contract_instance_ERC1155.functions.balanceOf(address, 0).call()
    if customer_point >= 20:
        result = "ricecooker_แลกได้"
    else:
        result = "ricecooker_แต้มไม่ถึง"
    return {"result":result}



@app.get("/check_point_iphone13/{customer_id}")
async def mycoin(customer_id: str):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    customer_point = contract_instance_ERC1155.functions.balanceOf(address, 0).call()
    if customer_point >= 300:
        result = "iphone13_แลกได้"
    else:
        result = "iphone13_แต้มไม่ถึง"
    return {"result":result}



@app.get("/burn_point_and_mint_hobobag/{customer_id}&{price}")
async def burn(customer_id: str, price: int):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]

    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.BurnPointAndMint(address, 1, int(price), 1).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"hash" :w3.toHex(transaction_hash)}



@app.get("/burn_point_and_mint_ricecooker/{customer_id}&{price}")
async def burn(customer_id: str, price: int):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]

    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.BurnPointAndMint(address, 2, int(price), 1).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"hash" :w3.toHex(transaction_hash)}



@app.get("/burn_point_and_mint_iphone13/{customer_id}&{price}")
async def burn(customer_id: str, price: int):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    privatekey = hardwallet[wallet_index][1]

    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance_ERC1155.functions.BurnPointAndMint(address, 3, int(price), 1).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"hash" :w3.toHex(transaction_hash)}



@app.get("/show_nfts_for_observe/{customer_id}")
async def show_nfts_for_observe(customer_id):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    customer_hobobag = contract_instance_ERC1155.functions.balanceOf(address, 1).call()
    customer_ricecooker = contract_instance_ERC1155.functions.balanceOf(address, 2).call()
    customer_iphone13 = contract_instance_ERC1155.functions.balanceOf(address, 3).call()
    show = 'hobobag = '+ str(customer_hobobag) + ', ricecooker = ' + str(customer_ricecooker) + ', iphone13 = ' + str(customer_iphone13)
    return{"show":show}



@app.get("/show_nfts/{customer_id}")
async def show_nfts(customer_id):
    users = contract_instance.functions.show_user().call()
    wallet_index = 0
    found = 0
    for i in users:
        if i == customer_id:
            wallet_index = found
        else:
            found += 1
    address = hardwallet[wallet_index][0]
    customer_hobobag = contract_instance_ERC1155.functions.balanceOf(address, 1).call()
    customer_ricecooker = contract_instance_ERC1155.functions.balanceOf(address, 2).call()
    customer_iphone13 = contract_instance_ERC1155.functions.balanceOf(address, 3).call()
    if customer_hobobag > 0:
        if customer_ricecooker > 0:
            if customer_iphone13 > 0:
                show = "show_nfts_111"
            else:
                show = "show_nfts_110"
        else:
            if customer_iphone13 > 0:
                show = "show_nfts_101"
            else:
                show = "show_nfts_100"
    else:
        if customer_ricecooker > 0:
            if customer_iphone13 > 0:
                show = "show_nfts_011"
            else:
                show = "show_nfts_010"
        else:
            if customer_iphone13 > 0:
                show = "show_nfts_001"
            else:
                show = "show_nfts_000"
    return{"show":show}            












# Ub771944dc72008fa9dd9ec5ce80c2c62&0001&nick-kie&0123456789123&07-06-2543&male&ee@gmail.com&0123456789
@app.get("/register/{customer_id}&{status}&{name}&{passport}&{birthday}&{gender}&{mail}&{phone}")
async def register(customer_id: str, status: str, name: str, passport: str, birthday: str, gender: str, mail: str, phone: str):
    nonce = w3.eth.getTransactionCount('0xA393E6989E035b56718FdcE9D30Ff925879361B7')
    Thaitime = pytz.timezone("Asia/Bangkok")
    timer = datetime.now(Thaitime)
    timestamp = str(timer.hour)+':'+str(timer.minute)+' '+str(timer.day)+'-'+str(timer.month)+'-'+str(timer.year)

    update_transaction = contract_instance.functions.addBook(customer_id, status, name, passport, birthday, gender, mail, phone, timestamp).buildTransaction(
        {
        'gas': 1000000,
        'gasPrice': w3.toWei('2.6', 'gwei'),
        'from': '0xA393E6989E035b56718FdcE9D30Ff925879361B7',
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = 'c91fd9e0aae948763d13f6adf39d7077b41b1676dfe2cbca7b180201b2621f4c')
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    report = 'ดูแต้มสะสม'
    return {"hash" :w3.toHex(transaction_hash)}



@app.get("/showregister/{customer_id}")
async def showregister(customer_id):
    data = contract_instance.functions.showMAPPING(customer_id).call()
    if data == []:
        data = 'ไม่เป็นสมาชิก'
    else:
        data = data
    return {"showregister" : str(data)}



@app.get("/checkmember_richmenu/{customer_id}")
async def checkmember_richmenu(customer_id):
    data = contract_instance.functions.showMAPPING(customer_id).call()
    if data == []:
        data = 'subscription_ไม่เป็นสมาชิก_richmenu'
    else:
        data = 'subscription_เป็นสมาชิก_richmenu'
    return {"result" : str(data)}


@app.get("/checkmember_buying/{customer_id}")
async def checkmember_richmenu(customer_id):
    data = contract_instance.functions.showMAPPING(customer_id).call()
    if data == []:
        data = 'subscription_ไม่เป็นสมาชิก'
    else:
        data = 'subscription_เป็นสมาชิก'
    return {"result" : str(data)}



@app.get("/pop_register/{customer_id}")
async def pop_register(customer_id):
    nonce = w3.eth.getTransactionCount('0xA393E6989E035b56718FdcE9D30Ff925879361B7')
    update_transaction = contract_instance.functions.pop_me_baby(customer_id).buildTransaction(
        {
        'gas': 1800000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'from': '0xA393E6989E035b56718FdcE9D30Ff925879361B7',
        'nonce': nonce
        }
    )
    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = 'c91fd9e0aae948763d13f6adf39d7077b41b1676dfe2cbca7b180201b2621f4c')
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    return {"pop" :"member's poped"}


