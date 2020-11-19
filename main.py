from contracts.registration_contract import *

if __name__ == '__main__':
    # register owner
    user_id = register_user(
        address='0xA29370aba1480B7bb32321c67c9406A4af71e05c', 
        user_info={
            "first_name": "John",
            "last_name": "Doe"
        })

    # register investor 1
    investor1_id = register_user(
        address='0xA29370aba1480B7bb32321c67c9406A4af71e05c', 
        user_info={
            "first_name": "Danny",
            "last_name": "Sturridge"
        })

    # register investor 2
    investor2_id = register_user(
        address='0xA29370aba1480B7bb32321c67c9406A4af71e05c', 
        user_info={
            "first_name": "James",
            "last_name": "Rodriguez"            
        })

    # register investor 3
    investor3_id = register_user(
        address='0xA29370aba1480B7bb32321c67c9406A4af71e05c', 
        user_info={
            "first_name": "Ronaldo",
            "last_name": "Doe"
        })

    # register property
    prop_id = register_property(
        user_id=user_id, 
        property_info={
            "aDDRE": ""
            # DATE OF AUCTION
            # PRICE
            # TOKENS TO MINT - 100
            # VALIDATION_ID
        })

    # investors buy tokens (funding crowdsale)

    # get token balance 

    # refund investor 

    # pay rent

    # distribute profits

    pass