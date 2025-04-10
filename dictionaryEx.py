#create a user dictionary with email, phone-number, password properties
user = {
    "email": "salehnasser65784@gmail.com",
    "phone_number": "1234567890",
    "password": "password123",
     "company": {
    "Company_name": "Salouhi ltd",
    "Company_location": "Dubai",
    "Company_username": "salouhi_ltd"
    }
}
#update the phone-number and password
user["phone_number"] = "0987654321"
user["password"] = "new_password123"

#add a nested company dictionary with the following properties : company_name, company_location and company_username
