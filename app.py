from datetime import date
from datetime import timedelta
from registration_contract import *
from property_crowdsale_contract import *

if __name__ == '__main__':
    # --------------------------------------------------------------------------
    # Register the owner
    # --------------------------------------------------------------------------

    owner_full_name = input("Please enter the owner's full name: ")    
    owner_wallet = input("Please enter the owner's wallet address: ")

    register_user(
        user_info={
            "wallet": owner_wallet, 
            "full_name": owner_full_name    
        })

    # --------------------------------------------------------------------------
    # Register investor 1
    # --------------------------------------------------------------------------

    investor1_full_name = input("Please enter the first investor's full name: ")    
    investor1_wallet = input("Please enter the first investor's wallet address: ")

    register_user(
        user_info={
            "wallet": investor1_wallet, 
            "full_name": investor1_full_name    
        })

    # --------------------------------------------------------------------------
    # Register investor 2
    # --------------------------------------------------------------------------

    investor2_full_name = input("Please enter the second investor's full name: ")    
    investor2_wallet = input("Please enter the second investor's wallet address: ")

    register_user(        
        user_info={
            "wallet": investor2_wallet, 
            "full_name": investor2_full_name    
        })    

    # --------------------------------------------------------------------------
    # Register a renter
    # --------------------------------------------------------------------------

    renter_full_name = input("Please enter the renter's full name: ")    
    renter_wallet = input("Please enter the renter's wallet address: ")

    register_user(        
        user_info={
            "wallet": renter_wallet, 
            "full_name": renter_full_name
        })

    # --------------------------------------------------------------------------
    # Register a property manager
    # --------------------------------------------------------------------------

    property_manager_company_name = input("Please enter the property manager company name: ")    
    property_manager_wallet = input("Please enter the property manager wallet address: ")

    register_property_management(        
        property_management_info={
            "wallet": property_manager_wallet, 
            "full_name": property_manager_company_name    
        })

    # --------------------------------------------------------------------------
    # Register owner's property
    # --------------------------------------------------------------------------
    
    property_validation_id = input("Please enter the property's validation id: ")    
    property_street_address = input("Please enter the property's street address: ")
    property_city = input("Please enter the property's city: ")
    property_state = input("Please enter the property's state: ")    
    property_zip_code = input("Please enter the property's zip code: ")
    property_price = input("Please enter the property's selling price: ")   
    owner_wallet = '0xbbf10C469a018a662A2e39632E1F9B09486AA2f2'

    property_URI = register_property(
        property_info={
            "owner_wallet": owner_wallet, 
            "validation_id": property_validation_id,
            "address": {
                "street_address": property_street_address,
                "city": property_city,
                "state": property_state,
                "zip_code": property_zip_code
            },
            "price": property_price,
            "minted_tokens": 100,        
            "auction_start_date": str(date.today()),
            "auction_end_date": str(date.today() + timedelta(days=90)),
            "image": "https://gateway.pinata.cloud/ipfs/QmQ64DgxCuce3whbRYGWHeLidgaNf4YqgBhmEmn7YT5W5d"
        })
    
    # --------------------------------------------------------------------------
    # Investor 1 buys tokens for property
    # --------------------------------------------------------------------------
    amount_of_tokens = input("Please enter the number of tokens you would like to purchase: ")   

    buyTokens(address=investor1_wallet, amount=int(amount_of_tokens))

    # --------------------------------------------------------------------------
    # Investor 2 buys tokens for property
    # --------------------------------------------------------------------------

    amount_of_tokens = input("Please enter the number of tokens you would like to purchase: ")   

    buyTokens(address=investor2_wallet, amount=int(amount_of_tokens))
    
    # --------------------------------------------------------------------------
    # Investor 1 gets balance of token purchased
    # --------------------------------------------------------------------------

    getBalance(investor1_wallet)

    # --------------------------------------------------------------------------
    # Investor 2 gets balance of token purchased
    # --------------------------------------------------------------------------
    
    getBalance(investor2_wallet)

    # --------------------------------------------------------------------------
    # Pay rent
    # --------------------------------------------------------------------------
    
    rent = input("Please enter the amount to be paid for the rent: ")

    payRent(transaction={
            'from_address': renter_wallet, 
            'to_address': property_manager_wallet,
            'rent_amount': rent
        })

    # --------------------------------------------------------------------------
    # Distribute profits
    # --------------------------------------------------------------------------

    # Add code here ...

    

    