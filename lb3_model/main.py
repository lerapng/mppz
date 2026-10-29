from system import StoreAutomationSystem


def main():
    print("Store Automation System Demo\n")

    store = StoreAutomationSystem()

    print("\n--- Admin Setup ---")
    electronics = store.admin_add_category("Electronics", "Electronic devices and gadgets")
    books = store.admin_add_category("Books", "Physical and digital books")
    clothing = store.admin_add_category("Clothing", "Apparel and accessories")

    laptop = store.admin_add_product(electronics, "Gaming Laptop", 1299.99, 15)
    headphones = store.admin_add_product(electronics, "Wireless Headphones", 89.99, 50)
    mouse = store.admin_add_product(electronics, "Gaming Mouse", 49.99, 100)
    python_book = store.admin_add_product(books, "Python Programming Guide", 39.99, 30)
    scifi_novel = store.admin_add_product(books, "Sci-Fi Novel Collection", 24.99, 20)
    tshirt = store.admin_add_product(clothing, "Cotton T-Shirt", 19.99, 200)
    jeans = store.admin_add_product(clothing, "Blue Jeans", 59.99, 75)

    print("\n--- Customer Registration ---")
    customer = store.customer_register(
        full_name="Alice Johnson",
        email="alice.johnson@email.com",
        phone="+1-555-0123"
    )

    shipping_address = store.customer_add_address(
        customer,
        city="San Francisco",
        street="123 Market Street, Apt 4B",
        postal_code="94102"
    )

    print("\n--- Browsing Products ---")
    all_products = store.customer_view_products()

    print("\nFiltering by Electronics:")
    electronics_products = store.customer_view_products(category=electronics)

    print("\n--- Placing Order ---")
    order_items = [
        (laptop, 1),
        (headphones, 2),
        (python_book, 1),
        (tshirt, 3),
    ]

    order = store.customer_create_order(customer, shipping_address, order_items)

    if not order:
        print("Order creation failed!")
        return

    print(f"\nOrder Summary:")
    print(f"  Order ID: {order.id}")
    print(f"  Customer: {order.user.full_name}")
    print(f"  Shipping to: {order.shipping_address}")
    print(f"  Items:")
    for item in order.items:
        print(f"    {item}")
    print(f"  Total: ${order.total_amount:.2f}")
    print(f"  Status: {order.status}")

    print("\n--- Payment ---")
    payment = store.customer_make_payment(order, payment_method="credit_card")

    if not payment:
        print("Payment failed!")
        return

    print(f"\nPayment details: {payment}")

    print("\n--- Order Fulfillment ---")
    store.admin_update_order_status(order, "processing")
    store.admin_update_order_status(order, "shipped")

    print("\n--- Customer Reviews ---")
    review1 = store.customer_leave_review(
        customer,
        laptop,
        rating=5,
        comment="Amazing laptop! Runs all my games smoothly. Highly recommend!"
    )

    review2 = store.customer_leave_review(
        customer,
        headphones,
        rating=4,
        comment="Great sound quality, but battery life could be better."
    )

    review3 = store.customer_leave_review(
        customer,
        python_book,
        rating=5,
        comment="Excellent guide for beginners and intermediate programmers."
    )

    print("\n--- Final Summary ---")
    print(f"\nTotal categories: {len(store.categories)}")
    print(f"Total products: {len(store.products)}")
    print(f"Total users: {len(store.users)}")
    print(f"Total orders: {len(store.orders)}")
    print(f"Total payments: {len(store.payments)}")
    print(f"Total reviews: {len(store.reviews)}")

    print(f"\nUpdated stock levels:")
    for product in [laptop, headphones, mouse, python_book, tshirt]:
        print(f"  {product.name}: {product.stock_quantity} units")

    print("\nDemo completed successfully!")


if __name__ == "__main__":
    main()
