from typing import List, Optional
from models import User, Address, Category, Product, Order, Payment, Review
from services import PaymentGateway


class StoreAutomationSystem:
    def __init__(self):
        self.categories: List[Category] = []
        self.products: List[Product] = []
        self.users: List[User] = []
        self.orders: List[Order] = []
        self.payments: List[Payment] = []
        self.reviews: List[Review] = []

        self._next_category_id = 1
        self._next_product_id = 1
        self._next_user_id = 1
        self._next_address_id = 1
        self._next_order_id = 1
        self._next_payment_id = 1
        self._next_review_id = 1

    def admin_add_category(self, name: str, description: str = ""):
        category = Category(self._next_category_id, name, description)
        self._next_category_id += 1
        self.categories.append(category)
        print(f"Added category: {category}")
        return category

    def admin_add_product(self, category: Category, name: str, price: float, stock_quantity: int):
        product = Product(self._next_product_id, category, name, price, stock_quantity)
        self._next_product_id += 1
        self.products.append(product)
        print(f"Added product: {product}")
        return product

    def admin_update_order_status(self, order: Order, new_status: str):
        old_status = order.status
        order.status = new_status
        print(f"Order #{order.id} status updated: {old_status} -> {new_status}")

    def customer_register(self, full_name: str, email: str, phone: str):
        user = User(self._next_user_id, full_name, email, phone)
        self._next_user_id += 1
        self.users.append(user)
        print(f"Registered user: {user}")
        return user

    def customer_add_address(self, user: User, city: str, street: str, postal_code: str):
        address = Address(self._next_address_id, city, street, postal_code)
        self._next_address_id += 1
        user.add_address(address)
        print(f"{user.full_name} added address: {address}")
        return address

    def customer_view_products(self, category: Optional[Category] = None):
        available_products = [p for p in self.products if p.stock_quantity > 0]

        if category:
            available_products = [p for p in available_products if p.category.id == category.id]

        print(f"\nAvailable products ({len(available_products)}):")
        for product in available_products:
            print(f"  {product}")

        return available_products

    def customer_create_order(self, user: User, shipping_address: Address, items: List[tuple]):
        order = Order(self._next_order_id, user, shipping_address)
        self._next_order_id += 1

        print(f"\nCreating order #{order.id} for {user.full_name}...")

        for product, quantity in items:
            if not order.add_item(product, quantity):
                print(f"  Failed: insufficient stock for {product.name} (requested: {quantity}, available: {product.stock_quantity})")
                return None
            print(f"  Added: {product.name} x{quantity}")

        order.calculate_total()
        self.orders.append(order)
        print(f"Order #{order.id} created. Total: ${order.total_amount:.2f}")
        return order

    def customer_make_payment(self, order: Order, payment_method: str):
        payment = Payment(self._next_payment_id, order, payment_method, order.total_amount)
        self._next_payment_id += 1

        print(f"\nInitiating payment for order #{order.id}...")

        if PaymentGateway.process_payment(payment):
            self.payments.append(payment)
            order.status = "paid"
            print(f"Payment successful. Order status updated to 'paid'")
            return payment
        else:
            print(f"Payment failed")
            return None

    def customer_leave_review(self, user: User, product: Product, rating: int, comment: str = ""):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        review = Review(self._next_review_id, user, product, rating, comment)
        self._next_review_id += 1
        self.reviews.append(review)

        print(f"\n{user.full_name} left a review for {product.name}: {rating}/5 stars")
        if comment:
            print(f"  Comment: \"{comment}\"")

        return review
