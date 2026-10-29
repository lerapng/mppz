from datetime import datetime


class Payment:
    def __init__(self, id: int, order, payment_method: str, amount: float):
        self.id = id
        self.order = order
        self.payment_method = payment_method
        self.amount = amount
        self.status = "pending"
        self.paid_at = None

    def complete_payment(self):
        self.status = "completed"
        self.paid_at = datetime.now()

    def __str__(self):
        return f"Payment(id={self.id}, order_id={self.order.id}, method={self.payment_method}, amount=${self.amount:.2f}, status={self.status})"
