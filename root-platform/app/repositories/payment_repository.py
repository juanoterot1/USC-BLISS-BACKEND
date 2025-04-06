from app.models.payment import Payment
from app.extensions import db

class PaymentRepository:
    @staticmethod
    def get_all():
        return Payment.query.all()

    @staticmethod
    def get_by_id(payment_id):
        return Payment.query.get(payment_id)

    @staticmethod
    def create(payment):
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(payment):
        db.session.delete(payment)
        db.session.commit()
