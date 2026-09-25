import sqlite3
from typing import List
from task2 import Product, ProductDetail

class ShopRepository:
    def __init__(self, db_name="shop.db", schema_file="task1.sql"):
        self.conn = sqlite3.connect(db_name)
        self.init_db(schema_file)

    def init_db(self, schema_file: str):
        with open(schema_file, "r", encoding="utf-8") as f:
            sql_script = f.read()
        with self.conn:
            self.conn.executescript(sql_script)

    def add_category(self, name: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Categories (name) VALUES (?)", (name,))
        self.conn.commit()
        return cursor.lastrowid

    def add_product(self, name: str, price: float, category_id: int, description: str, weight: float) -> int:
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Products (name, price, category_id) VALUES (?, ?, ?)", 
            (name, price, category_id)
        )
        product_id = cursor.lastrowid
        
        cursor.execute(
            "INSERT INTO ProductDetails (product_id, description, weight) VALUES (?, ?, ?)", 
            (product_id, description, weight)
        )
        self.conn.commit()
        return product_id

    def create_order(self, order_date: str) -> int:
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Orders (order_date) VALUES (?)", (order_date,))
        self.conn.commit()
        return cursor.lastrowid

    def add_product_to_order(self, order_id: int, product_id: int, quantity: int):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO OrderProducts (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, product_id, quantity)
        )
        self.conn.commit()

    def get_all_products(self) -> List[Product]:
        cursor = self.conn.cursor()
        query = """
        SELECT p.id, p.name, p.price, p.category_id, pd.id, pd.description, pd.weight
        FROM Products p
        LEFT JOIN ProductDetails pd ON p.id = pd.product_id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        products = []
        for r in rows:
            detail = ProductDetail(id=r[4], product_id=r[0], description=r[5], weight=r[6]) if r[4] else None
            products.append(Product(id=r[0], name=r[1], price=r[2], category_id=r[3], detail=detail))
        return products