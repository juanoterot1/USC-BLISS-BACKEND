from app.models.sale_detail import SaleDetail
from app.extensions import db

class SaleDetailRepository:
    @staticmethod
    def get_all():
        return SaleDetail.query.all()

    @staticmethod
    def get_by_id(sale_detail_id):
        return SaleDetail.query.get(sale_detail_id)

    @staticmethod
    def create(sale_detail):
        db.session.add(sale_detail)
        db.session.commit()
        return sale_detail

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(sale_detail):
        db.session.delete(sale_detail)
        db.session.commit()
