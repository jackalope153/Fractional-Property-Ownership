from registration_contract import *

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
    # Register investor 3
    # --------------------------------------------------------------------------

    investor3_full_name = input("Please enter the third investor's full name: ")    
    investor3_wallet = input("Please enter the third investor's wallet address: ")

    register_user(        
        user_info={
            "wallet": investor3_wallet, 
            "full_name": investor3_full_name    
        })

    # --------------------------------------------------------------------------
    # Register owner's property
    # --------------------------------------------------------------------------
    
    property_street_address = input("Please enter the property's street address: ")  # h  
    property_city = input("Please enter the property's city: ")
    property_state = input("Please enter the property's state: ")    
    property_zip_code = input("Please enter the property's zip code: ")
    property_validation_id = input("Please enter the property's validation id: ")    
    property_price = input("Please enter the property's selling price: ")    
    property_minted_tokens = input("Please enter the number of token to be minted for the property: ")    
    property_auction_date = input("Please enter the auction date: ")

    property_id = register_property(                
        property_info={
            "owner_wallet": owner_wallet, 
            "address": {
                "street_address": property_street_address,
                "city": property_city,
                "state": property_state,
                "zip_code": property_zip_code
            },
            "auction_date": property_auction_date,
            "price": property_price,
            "minted_tokens": property_minted_tokens,
            "validation_id": property_validation_id
        })
    
    # --------------------------------------------------------------------------
    # Investor 1 buys tokens for property
    # --------------------------------------------------------------------------

    # buy_token(from: 'address', to: 'address', amt_of_token:0)

    # --------------------------------------------------------------------------
    # Investor 2 buys tokens for property
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # Investor 3 buys tokens for property
    # --------------------------------------------------------------------------
    


    # --------------------------------------------------------------------------
    # Investor 1 gets balance of token purchased
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # Investor 2 gets balance of token purchased
    # --------------------------------------------------------------------------


    # --------------------------------------------------------------------------
    # Investor 3 gets balance of token purchased
    # --------------------------------------------------------------------------

    # refund investor 

    # pay rent

    # distribute profits

    