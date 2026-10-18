# Nested Model Validation with Pydantic

A clean Python script demonstrating how to structure, validate, and access nested relationship schemas using **Pydantic V2**.

## 🚀 Features

- **Nested Model Architecture**: Showcases how to map a secondary validation sub-schema (`Address`) as a direct type attribute within a primary model (`patient`).
- **Object Parsing**: Structural unpack validation using the Python dictionary dictionary expansion operator (`**`).
- **Clean Attribute Navigation**: Accesses nested property attributes cleanly through chaining object-attribute dot notation (`patient_obj.address.city`).

## 📦 Installation

Ensure you have Python installed, then fetch Pydantic via pip:

```bash
pip install pydantic
```

## 💻 Script Implementation (`main.py`)

```python
from pydantic import BaseModel

# 1. Define Child Schema
class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

# 2. Define Parent Schema with Nested Reference
class patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

# 3. Supply Child Raw Data and Instantiate
address_dict = {
    "street": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001"
}
address_obj = Address(**address_dict)

# 4. Supply Parent Payload (Passing child object directly)
patient_info = {
    "name": "John Doe",
    "gender": "Male",
    "age": 30,
    "address": address_obj
}
patient_obj = patient(**patient_info)

# 5. Output Clean Attributes Navigation
print(patient_obj.name)
print("----------ADDRESS------------")
print(patient_obj.address.city)
print(patient_obj.address.zip_code)
```

## 🎯 Expected Output

Run the script execution inside your terminal environment layout:

```bash
python main.py
```

Output:
```text
John Doe
----------ADDRESS------------
New York
10001
```

## 🧠 Structural Tip (Simplifying Nested Inputs)
Pydantic is highly intelligent. Instead of instantiating `Address` separately via `Address(**address_dict)`, you can pass the raw inner dictionary directly inside `patient_info`. Pydantic will dynamically initialize the nested sub-schema for you:

```python
patient_info = {
    "name": "John Doe",
    "gender": "Male",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }
}
patient_obj = patient(**patient_info) # Automatically generates the sub-model nested validation!
```
