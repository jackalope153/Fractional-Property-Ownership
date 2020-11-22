class PropertyInfo():
    def __init__(self, owner_user_id, verification_id, sale_price, sale_expiration_date, minted_tokens, address, images, property_id):
        self.owner_user_id = owner_user_id
        self.verification_id = verification_id
        self.selling_price = selling_price
        self.sale_expiration_date = sale_expiration_date        
        self.minted_tokens = minted_tokens
        self.address = address 
        self.images = images
        self.property_id = property_id

class UserInfo():
    def __init__(self, username, password, first_name, last_name, address, phone, email, wallet, user_id):
        self.username = username
        self.password = password 
        self.first_name = first_name
        self.last_name = last_name
        self.address = address 
        self.phone = phone
        self.email = email 
        self.wallet = wallet
        self.user_id = user_id     
        

class PropertyManagementInfo():
    def __init__(self, company_name, contact_first_name, contact_last_name, address, phone, email, properties, property_management_id):
        self.company_name = company_name
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.address = address 
        self.phone = phone
        self.email = email
        self.properties = properties
        self.property_management_id = property_management_id        
        
class AddressInfo():
    def __init__(self, street_address, street_address2, city, state, zip_code):
        self.street_address = street_address
        self.street_address2 = street_address2
        self.city = city
        self.state = state
        self.zip_code = zip_code