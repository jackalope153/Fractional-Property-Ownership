from web3.auto import w3
import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

load_dotenv()

def initContract(contract_abi_path: str, contract_address: str):
    with open(Path(contract_abi_path)) as json_file:
        abi = json.load(json_file)

    return w3.eth.contract(address=os.getenv(contract_address), abi=abi)

def convertDataToJSON(content: dict):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": content
    }
    return json.dumps(data)

def pinJSONtoIPFS(json):
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": os.getenv("PINATA_API_KEY"),
        "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY")
    }

    r = requests.post("https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers)    
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"