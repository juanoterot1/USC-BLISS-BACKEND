from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.payment import Payment
from app.repositories.payment_repository import PaymentRepository

logger = logging.getLogger(__name__)

class PaymentService:
    @inject
    def __init__(self, payment_repository: PaymentRepository):
        self.payment_repository = payment_repository

    def get_all_payments(self):
        try:
            payments = self.payment_repository.get_all()
            return [payment.as_dict() for payment in payments]
        except Exception as e:
            logger.error(f"Error retrieving payments: {e}")
            raise BadRequest(f"Error retrieving payments: {str(e)}")

    def get_payment_by_id(self, payment_id):
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            logger.warning(f"Payment not found with ID: {payment_id}")
            raise NotFound(f"Payment with ID {payment_id} not found")
        return payment.as_dict()

    def create_payment(self, sale_id, amount, payment_date, payment_method=None, status='pending', created_by=None):
        payment = Payment(sale_id, amount, payment_date, payment_method, status, created_by)
        new_payment = self.payment_repository.create(payment)
        return new_payment.as_dict()

    def update_payment(self, payment_id, **kwargs):
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            logger.warning(f"Payment not found with ID: {payment_id}")
            raise NotFound(f"Payment with ID {payment_id} not found")
        for key, value in kwargs.items():
            setattr(payment, key, value)
        self.payment_repository.update()
        return payment.as_dict()

    def delete_payment(self, payment_id):
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            logger.warning(f"Payment not found with ID: {payment_id}")
            raise NotFound(f"Payment with ID {payment_id} not found")
        self.payment_repository.delete(payment)
        return {"message": f"Payment with ID {payment_id} deleted"}
