from contracts.base_contract import *

RegistrationContract = initContract("registration_contract_abi.json", os.getenv("REGISTRATION_CONTRACT_ADDRESS"))    

def register_property(user_id: int, property_info: dict):
    data = convertDataToJSON(property_info)
    propertyURI = pinJSONtoIPFS(data)

    tx_hash = RegistrationContract.functions.registerProperty(user_id, propertyURI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReipt(tx_hash)

    return receipt    

def register_user(address: str, user_info: dict):
    data = convertDataToJSON(user_info)
    user_info_URI = pinJSONtoIPFS(data)

    tx_hash = RegistrationContract.functions.registerUser(address, user_info_URI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReipt(tx_hash)

    return receipt    

def register_property_management(address: str, property_management_info: dict):
    data = convertDataToJSON(property_management_info)
    property_management_URI = pinJSONtoIPFS(data)

    tx_hash = RegistrationContract.functions.registerPropertyManagement(address, property_management_URI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReipt(tx_hash)

    return receipt            