from datetime import datetime
from typing import List


class OrderItem:
    def __init__(self, product, quantity: int, unit_price: float):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name} x{self.quantity} @ ${self.unit_price:.2f} = ${self.get_total_price():.2f}"


class Order:
    def __init__(self, id: int, user, shipping_address):
        self.id = id
        self.user = user
        self.shipping_address = shipping_address
        self.items: List[OrderItem] = []
        self.status = "pending"
        self.total_amount = 0.0
        self.created_at = datetime.now()

    def add_item(self, product, quantity: int):
        if product.stock_quantity < quantity:
            return False

        product.stock_quantity -= quantity
        order_item = OrderItem(product, quantity, product.price)
        self.items.append(order_item)
        return True

    def calculate_total(self):
        self.total_amount = sum(item.get_total_price() for item in self.items)
        return self.total_amount

    def __str__(self):
        return f"Order(id={self.id}, user={self.user.full_name}, status={self.status}, total=${self.total_amount:.2f})"
