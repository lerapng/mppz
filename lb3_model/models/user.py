from typing import List


class Address:
    def __init__(self, id: int, city: str, street: str, postal_code: str):
        self.id = id
        self.city = city
        self.street = street
        self.postal_code = postal_code

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"


class User:
    def __init__(self, id: int, full_name: str, email: str, phone: str):
        self.id = id
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.addresses: List[Address] = []

    def add_address(self, address: Address):
        self.addresses.append(address)

    def __str__(self):
        return f"User(id={self.id}, name={self.full_name}, email={self.email})"
