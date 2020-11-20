# In theory this should work, but it is not. Error happens with the call function, not sure if it should be call or something else. 

from base_contract import *

propertysaledeployer = "0x39c5246bE3A516eD4F2747Fb32e1132e853341C2"

propertysaledeployercontract = initContract("propertysaledeployerabi.json", propertysaledeployer)

def view_balance(checking_address:str):
    tx_hash = PropertySaleDeployerContract.functions.balanceOf(checking_address).call()
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return tx_hash
    