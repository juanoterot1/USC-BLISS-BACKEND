from app.models.receipt import Receipt
from app.extensions import db

class ReceiptRepository:
    @staticmethod
    def get_all():
        return Receipt.query.all()

    @staticmethod
    def get_by_id(receipt_id):
        return Receipt.query.get(receipt_id)

    @staticmethod
    def create(receipt):
        db.session.add(receipt)
        db.session.commit()
        return receipt

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(receipt):
        db.session.delete(receipt)
        db.session.commit()
