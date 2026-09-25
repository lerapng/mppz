from task3 import ShopRepository

class ShopPrinterService:
    def __init__(self, repository: ShopRepository):
        self.repo = repository

    def print_catalog(self):
        products = self.repo.get_all_products()
        print("\nКаталог товарів магзаину")
        for p in products:
            print(f"ID: {p.id} \n Товар: {p.name} \n Ціна: {p.price} грн")
            if p.detail:
                print(f"Опис: {p.detail.description} (Вага: {p.detail.weight} кг)")
            print("-" * 45)

    def print_order_details(self, order_id: int):
        cursor = self.repo.conn.cursor()
        query = """
        SELECT o.id, o.order_date, p.name, p.price, op.quantity
        FROM Orders o
        JOIN OrderProducts op ON o.id = op.order_id
        JOIN Products p ON op.product_id = p.id
        WHERE o.id = ?
        """
        cursor.execute(query, (order_id,))
        rows = cursor.fetchall()

        if not rows:
            print(f"\nЗамовлення №{order_id} не знайдено.")
            return

        print(f"\nДеталі замовлення №{order_id} (дата: {rows[0][1]})")
        total_sum = 0
        for row in rows:
            p_name, price, qty = row[2], row[3], row[4]
            item_sum = price * qty
            total_sum += item_sum
            print(f" • {p_name} — {qty} шт. x {price} грн = {item_sum} грн")
        print(f"До сплати: {total_sum} грн")
        print("=" * 45)