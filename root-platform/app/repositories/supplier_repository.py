from app.models.supplier import Supplier
from app.extensions import db

class SupplierRepository:
    @staticmethod
    def get_all():
        return Supplier.query.all()

    @staticmethod
    def get_by_id(supplier_id):
        return Supplier.query.get(supplier_id)

    @staticmethod
    def create(supplier):
        db.session.add(supplier)
        db.session.commit()
        return supplier

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(supplier):
        db.session.delete(supplier)
        db.session.commit()
