from task3 import ShopRepository
from task4 import ShopPrinterService

if __name__ == "__main__":
    repo = ShopRepository("shop.db")

    cat_electronics = repo.add_category("Електроніка")
    cat_appliances = repo.add_category("Побутова техніка")
    cat_accessories = repo.add_category("Аксесуари")

    p1_id = repo.add_product(
        name="Ноутбук Lenovo IdeaPad", 
        price=25000.0, 
        category_id=cat_electronics, 
        description="16GB RAM, SSD 512GB, AMD Ryzen 5", 
        weight=1.8
    )

    p2_id = repo.add_product(
        name="Смартфон Samsung Galaxy", 
        price=18500.0, 
        category_id=cat_electronics, 
        description="AMOLED 120Hz, 128GB, Camera 50MP", 
        weight=0.19
    )

    p3_id = repo.add_product(
        name="Кавомашина DeLonghi", 
        price=14200.0, 
        category_id=cat_appliances, 
        description="Автоматичний капучинатор, тиск 15 бар", 
        weight=9.2
    )

    p4_id = repo.add_product(
        name="Бездротова миша", 
        price=850.0, 
        category_id=cat_accessories, 
        description="Оптичний датчик 1600 DPI, Bluetooth/USB", 
        weight=0.08
    )

    order1_id = repo.create_order("2026-09-25")
    repo.add_product_to_order(order_id=order1_id, product_id=p1_id, quantity=1)
    repo.add_product_to_order(order_id=order1_id, product_id=p4_id, quantity=2)

    order2_id = repo.create_order("2026-09-25")
    repo.add_product_to_order(order_id=order2_id, product_id=p2_id, quantity=1)
    repo.add_product_to_order(order_id=order2_id, product_id=p3_id, quantity=1)

    printer = ShopPrinterService(repo)
    printer.print_catalog()
    printer.print_order_details(order1_id)
    