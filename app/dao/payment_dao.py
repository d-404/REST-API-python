from app.model.payment_model import payments
from app.config.db import conn

class PaymentDAO:
    @staticmethod
    def get_all_payments():
        return conn.execute(payments.select()).fetchall()

    @staticmethod
    def get_payment_by_id(payment_id):
        return conn.execute(payments.select().where(payments.c.id == payment_id)).fetchone()

    @staticmethod
    def create_payment(payment_data):
        print(payment_data)
        conn.execute(payments.insert().values(payment_data))
        conn.commit()
        return "Payment Created Successfully"

    @staticmethod
    def update_payment(payment_id, payment_data):
        conn.execute(payments.update().values(payment_data).where(payments.c.id == payment_id))
        return "Payment Updated Successfully"

    @staticmethod
    def delete_payment(payment_id):
        conn.execute(payments.delete().where(payments.c.id == payment_id))
        return "Payment Deleted Successfully"