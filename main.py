from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class patient(BaseModel):

    name:str
    gender:str
    age:int
    address: Address

address_dict = {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
}

address_obj = Address(**address_dict)


patient_info = {
    "name": "John Doe",
    "gender": "Male",
    "age": 30,
    "address": address_obj
}


patient_obj = patient(**patient_info)




#print(patient1)
print(patient_obj.name)
print("----------ADDRESS------------")
print(patient_obj.address.city)
print(patient_obj.address.zip_code)