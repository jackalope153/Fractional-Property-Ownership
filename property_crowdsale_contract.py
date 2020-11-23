from base_contract import *

def get_token_address():
    txt_hash = PropertySaleDeployerContract.functions.token_address().call()
    return txt_hash
    
def get_token_sale_address():
    txt_hash = PropertySaleDeployerContract.functions.token_sale_address().call()
    return txt_hash

def getBalance(address: str):
    txt_hash = PropertyCrowdsaleContract.functions.balanceOf(address).call()
    print(txt_hash)
    return txt_hash

def buyTokens(address: str, amount: int):
    txt_hash = PropertyCrowdsaleContract.functions.buyTokens(address).transact({
        "from": w3.eth.accounts[0], 
        "value": amount
    })

    receipt = w3.eth.waitForTransactionReceipt(txt_hash)
    return receipt

def payRent(transaction_info: dict):
    from_address = transaction_info['from'] 
    to_address = transaction_info['to'] 
    rent_amount = transaction_info['amount'] 

    data = convertDataToJSON(transaction_info)
    transaction_info_URI = pinJSONtoIPFS(data)

    tx_hash = PropertyCrowdsaleContract.functions.pay_rent(to_address, rent_amount).transact({
        "from": from_address        
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt 

def DeployPaymentSplitterContract(list_of_address: list, list_of_tokens: list, income: int):
    with open(Path("./contracts/PaymentSplitterABI.json")) as json_file:
        abi = json.load(json_file)

    with open(Path("./contracts/PaymentSplitterByte.json")) as json_file:
        bytecode = json.load(json_file)
    
    BeginContract = w3.eth.contract(abi = abi, bytecode=bytecode)
    txhash = BeginContract.constructor(list_of_address, list_of_tokens).transact({"from": w3.eth.accounts[0], "value" : income})
    txreceipt = w3.eth.waitForTransactionReceipt(txhash)
    PaymentSplitterContract = w3.eth.contract(address=txreceipt.contractAddress, abi = abi)

    list_of_receipts = []
    for address in list_of_address:
        txt_hash = PaymentSplitterContract.functions.release(address).transact({"from": w3.eth.accounts[0]})
        receipt = w3.eth.waitForTransactionReceipt(txt_hash)
        list_of_receipts.append(receipt)
    
    return list_of_receipts
    
def getETHBalance(address: str):
	balance = w3.eth.getBalance(address)
	ETH = balance/1000000000000000000
	return ETH    

PropertySaleDeployerContract = initContract(os.getenv('PROPERTY_SALE_DEPLOYER_CONTRACT_ADDRESS'), "./contracts/PropertySaleDeployer.json")
# PropertyCrowdsaleContract = initContract(os.getenv('PROPERTY_SALE_CONTRACT_ADDRESS'), "./contracts/Crowdsale.json")
PropertyCrowdsaleContract = initContract(get_token_sale_address(), "./contracts/Crowdsale.json")
