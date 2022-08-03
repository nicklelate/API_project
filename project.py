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
abi_ERC20 = '[ { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "subtractedValue", "type": "uint256" } ], "name": "decreaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "user", "type": "address" }, { "internalType": "uint256", "name": "coin", "type": "uint256" } ], "name": "exchange", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "user", "type": "address" }, { "internalType": "uint256", "name": "coin", "type": "uint256" } ], "name": "getcoin", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "addedValue", "type": "uint256" } ], "name": "increaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]'
contract_address_ERC20 = '0xda749a1fc56cA40E54F81A23E5C1589Ff44A6911'
contract_instance_ERC20 = w3.eth.contract(address = contract_address_ERC20, abi = abi_ERC20)

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
    score = math.ceil(price/500)
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
    update_transaction = contract_instance_ERC20.functions.getcoin(address, int(score)).buildTransaction(
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
    score = math.ceil(price/500)
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
    update_transaction = contract_instance_ERC20.functions.getcoin(address, int(score)).buildTransaction(
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
    update_transaction = contract_instance_ERC20.functions.exchange(address, int(price)).buildTransaction(
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



@app.get("/totalcoin")
async def totalcoin():
    total = contract_instance_ERC20.functions.totalSupply().call()
    return {"total" : str(total)}



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
    the_coin = contract_instance_ERC20.functions.balanceOf(address).call()
    return {"total" : str(the_coin)}





















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