from app.models.sale import Sale
from app.extensions import db

class SaleRepository:
    @staticmethod
    def get_all():
        return Sale.query.all()

    @staticmethod
    def get_by_id(sale_id):
        return Sale.query.get(sale_id)

    @staticmethod
    def create(sale):
        db.session.add(sale)
        db.session.commit()
        return sale

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(sale):
        db.session.delete(sale)
        db.session.commit()
