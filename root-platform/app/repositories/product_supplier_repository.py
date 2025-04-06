from app.models.product_supplier import ProductSupplier
from app.extensions import db

class ProductSupplierRepository:
    @staticmethod
    def get_all():
        return ProductSupplier.query.all()

    @staticmethod
    def get_by_id(product_supplier_id):
        return ProductSupplier.query.get(product_supplier_id)

    @staticmethod
    def create(product_supplier):
        db.session.add(product_supplier)
        db.session.commit()
        return product_supplier

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(product_supplier):
        db.session.delete(product_supplier)
        db.session.commit()
