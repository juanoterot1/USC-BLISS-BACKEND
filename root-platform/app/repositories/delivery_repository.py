from app.models.delivery import Delivery
from app.extensions import db

class DeliveryRepository:
    @staticmethod
    def get_all():
        return Delivery.query.all()

    @staticmethod
    def get_by_id(delivery_id):
        return Delivery.query.get(delivery_id)

    @staticmethod
    def create(delivery):
        db.session.add(delivery)
        db.session.commit()
        return delivery

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(delivery):
        db.session.delete(delivery)
        db.session.commit()
