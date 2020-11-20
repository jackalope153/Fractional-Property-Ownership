from web3.auto import w3
import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

load_dotenv()

def initContract(contract_address: str, contract_abi_path: str):
    with open(Path(contract_abi_path)) as json_file:
        abi = json.load(json_file)
        
    if (contract_address.find(";") > -1 or contract_address.find(";") > -1):
        contract_address = contract_address.replace(";", "").replace("'", "")

    return w3.eth.contract(address=contract_address, abi=abi)

def convertDataToJSON(content: dict):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": content
    }
    return json.dumps(data)

def pinJSONtoIPFS(json):
    pinata_api_key = os.getenv("PINATA_API_KEY")

    if (pinata_api_key.find(";") > -1 or pinata_api_key.find(";") > -1):
        pinata_api_key = pinata_api_key.replace(";", "").replace("'", "")

    pinata_secret_api_key = os.getenv("PINATA_SECRET_API_KEY")

    if (pinata_secret_api_key.find(";") > -1 or pinata_secret_api_key.find(";") > -1):
        pinata_secret_api_key = pinata_secret_api_key.replace(";", "").replace("'", "")

    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": pinata_api_key,
        "pinata_secret_api_key": pinata_secret_api_key
    }

    r = requests.post("https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers)
    # print(r.json())
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"