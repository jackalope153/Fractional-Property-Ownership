from web3.auto import w3
import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path
from dotenv import load_dotenv



load_dotenv()
PropertySaleDeployer = os.getenv("PropertySaleDeployer")


def initContract(contract_abi_path: str, contract_address: str):
    with open(Path(contract_abi_path)) as json_file:
        abi = json.load(json_file)

    return w3.eth.contract(address=contract_address, abi=abi)
    
PropertySaleDeployerContract = initContract("PropertySaleDeployer.json", PropertySaleDeployer)

def get_token_address():
    txt_hash = PropertySaleDeployerContract.functions.token_address().call()
    return txt_hash
    
def get_token_sale_address():
    txt_hash = PropertySaleDeployerContract.functions.token_sale_address().call()
    return txt_hash
    
PropertyCrowdsaleContract = initContract("PropertyCrowdsale.json", get_token_sale_address())

def getBalance(address: str):
    txt_hash = PropertyCrowdsaleContract.functions.balanceOf(address).call()
    print(txt_hash)
    return txt_hash

def buyTokens(address: str, amount: int):
    txt_hash = PropertyCrowdsaleContract.functions.buyTokens(address).transact({"from": w3.eth.accounts[0], "value": amount})
    receipt = w3.eth.waitForTransactionReceipt(txt_hash)
    return receipt



income = input("How much do you want to send in wei?: ")
def DeployPaymentSplitterContract(list_of_address: list,list_of_tokens: list, income: int):
        with open(Path("PaymentSplitterABI.json")) as json_file:
            abi = json.load(json_file)
    
        with open(Path("PaymentSplitterByte.json")) as json_file:
            byte = json.load(json_file)
        
        BeginContract = w3.eth.contract(abi = abi, bytecode=bytecode)
        txhash = BeginContract.constructor(list1,list2).transact({"from": w3.eth.accounts[0], "value" : income})
        txreceipt = w3.eth.waitForTransactionReceipt(txhash)
        PaymentSplitterContract = w3.eth.contract(address=txreceipt.contractAddress, abi = abi)
    
        list_of_receipts = []
        for address in list1:
            txt_hash = PaymentSplitterContract.functions.release(address).transact({"from": w3.eth.accounts[0]})
            receipt = w3.eth.waitForTransactionReceipt(txt_hash)
            list_of_receipts.append(receipt)
        
        return list_of_receipts
    

# DeployPaymentsSplitterContract(investor_list, investor_share_amount, income)

# buyTokens("0x04Dffe3A125eA8614ffA7284f138023039c17022", input("How much do feel like losing? "))
# getBalance("0x04Dffe3A125eA8614ffA7284f138023039c17022")