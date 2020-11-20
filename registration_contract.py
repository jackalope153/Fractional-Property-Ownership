from base_contract import *

RegistrationContract = initContract(os.getenv('REGISTRATION_CONTRACT_ADDRESS'), "./contracts/registration_contract_abi.json")

def register_user(user_info: dict):    
    wallet = user_info['wallet']        

    data = convertDataToJSON(user_info)
    user_info_URI = pinJSONtoIPFS(data)
    
    tx_hash = RegistrationContract.functions.registerUser(wallet, user_info_URI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)    

    return receipt  

def register_property(property_info: dict):
    owner_wallet = property_info['owner_wallet']    

    data = convertDataToJSON(property_info)
    property_URI = pinJSONtoIPFS(data)
    
    tx_hash = RegistrationContract.functions.registerProperty(owner_wallet, property_URI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    # print(receipt)

    # processed_receipt = RegistrationContract.events.RegisterProperty().processReceipt(receipt)
    # print(processed_receipt)

    # output = f"userID: {processed_receipt[0].args.userID}"
    # print(output)

    return receipt

def register_property_management(property_management_info: dict):
    wallet = property_management_info['wallet'] 

    data = convertDataToJSON(property_management_info)
    property_management_URI = pinJSONtoIPFS(data)

    tx_hash = RegistrationContract.functions.registerPropertyManagement(wallet, property_management_URI).transact({
        "from": w3.eth.accounts[0]
    })
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return receipt            

# def buy_token(from_address: str, to_address:str, tokens_to_purchase:int):
    # pass

# def get_balance(address):
    # pass
