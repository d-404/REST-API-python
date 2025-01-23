from app.dao.payment_dao import PaymentDAO

class PaymentService:
    @staticmethod
    def fetch_all_payments():
        return PaymentDAO.get_all_payments()

    @staticmethod
    def fetch_payment_by_id(payment_id):
        return PaymentDAO.get_payment_by_id(payment_id)

    @staticmethod
    def add_payment(payment_data):
        return PaymentDAO.create_payment(payment_data)

    @staticmethod
    def modify_payment(payment_id, payment_data):
        return PaymentDAO.update_payment(payment_id, payment_data)

    @staticmethod
    def remove_payment(payment_id):
        return PaymentDAO.delete_payment(payment_id)