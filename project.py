from web3 import Web3
from web3 import EthereumTesterProvider
from fastapi import FastAPI
import math
from datetime import datetime
import pytz
app = FastAPI()

provider_url = 'https://rinkeby.infura.io/v3/5a5adcea95764d898c7e69d4c27f4c01'
w3 = Web3(Web3.HTTPProvider(provider_url))

abi = '[ { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" }, { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "name": "addBook", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "subtractedValue", "type": "uint256" } ], "name": "decreaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "user", "type": "address" }, { "internalType": "uint256", "name": "coin", "type": "uint256" } ], "name": "exchange", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "user", "type": "address" }, { "internalType": "uint256", "name": "coin", "type": "uint256" } ], "name": "getcoin", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "addedValue", "type": "uint256" } ], "name": "increaseAllowance", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" } ], "name": "pop_me_baby", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct SBC.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [ { "internalType": "uint8", "name": "", "type": "uint8" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "name", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "showARRAYS", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct SBC.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_index", "type": "string" } ], "name": "showMAPPING", "outputs": [ { "components": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "internalType": "struct SBC.DATA[]", "name": "", "type": "tuple[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "warehouse", "outputs": [ { "internalType": "string", "name": "_status", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "string", "name": "_passport", "type": "string" }, { "internalType": "string", "name": "_birthday", "type": "string" }, { "internalType": "string", "name": "_gender", "type": "string" }, { "internalType": "string", "name": "_mail", "type": "string" }, { "internalType": "string", "name": "_phone", "type": "string" }, { "internalType": "string", "name": "_datetime", "type": "string" } ], "stateMutability": "view", "type": "function" } ]'
contract_address = '0x06980cFDCab3b57aBeE1847636C72C0917AAE2BD'

contract_instance = w3.eth.contract(address = contract_address, abi = abi)

hardwallet = ['0x50f9828ddF89e10Dee9B2E28Db43E86111Df439C', '6a97002b83cdaccc96f0cf894987deed791ae6264effe3b861ac328392ff6e0e']
wallet = {'U5c40899d87469fe68d9841d1246d4118': hardwallet}

@app.get("/")
async def show():
    return {"show":"It's working"}

@app.get("/getcoin/{customer_id}&{price}")
async def getcoin(customer_id: str, price: int):
    score = math.ceil(price/20)
    address = wallet[customer_id][0]
    privatekey = wallet[customer_id][1]

    nonce = w3.eth.getTransactionCount(address)
    update_transaction = contract_instance.functions.getcoin(address, int(score)).buildTransaction(
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


@app.get("/totalcoin")
async def totalcoin():
    total = contract_instance.functions.totalSupply().call()
    return {"total" : str(total)}

@app.get("/mycoin/{customer_id}")
async def mycoin(customer_id: str):
    address = wallet[customer_id][0]
    the_coin = contract_instance.functions.balanceOf(address).call()
    return {"total" : str(the_coin)}

# U5c40899d87469fe68d9841d1246d4118&0001&nick-kie&0123456789123&07-06-2543&male&ee@gmail.com&0123456789
@app.get("/register/{customer_id}&{status}&{name}&{passport}&{birthday}&{gender}&{mail}&{phone}")
async def register(customer_id: str, status: str, name: str, passport: str, birthday: str, gender: str, mail: str, phone: str):
    address = wallet[customer_id][0]
    privatekey = wallet[customer_id][1]

    nonce = w3.eth.getTransactionCount(address)
    Thaitime = pytz.timezone("Asia/Bangkok")
    timer = datetime.now(Thaitime)
    timestamp = str(timer.hour)+':'+str(timer.minute)+' '+str(timer.day)+'-'+str(timer.month)+'-'+str(timer.year)

    update_transaction = contract_instance.functions.addBook(customer_id, status, name, passport, birthday, gender, mail, phone, timestamp).buildTransaction(
        {
        'gas': 1000000,
        'gasPrice': w3.toWei('2.6', 'gwei'),
        'from': address,
        'nonce': nonce
        }
    )

    sign_transaction = w3.eth.account.sign_transaction(update_transaction, private_key = privatekey)
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)

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
