class PaymentGateway:
    @staticmethod
    def process_payment(payment):
        print(f"Processing payment #{payment.id} for ${payment.amount:.2f} via {payment.payment_method}...")
        payment.complete_payment()
        print(f"Payment #{payment.id} completed successfully")
        return True
