from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Category:
    id: int
    name: str

@dataclass
class ProductDetail:
    id: int
    product_id: int
    description: str
    weight: float

@dataclass
class Product:
    id: int
    name: str
    price: float
    category_id: int
    detail: Optional[ProductDetail] = None

@dataclass
class OrderProduct:
    order_id: int
    product_id: int
    quantity: int

@dataclass
class Order:
    id: int
    order_date: str
    items: List[OrderProduct] = field(default_factory=list)