class Category:
    def __init__(self, id: int, name: str, description: str = ""):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Category(id={self.id}, name={self.name})"


class Product:
    def __init__(self, id: int, category, name: str, price: float, stock_quantity: int):
        self.id = id
        self.category = category
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price=${self.price:.2f}, stock={self.stock_quantity})"
