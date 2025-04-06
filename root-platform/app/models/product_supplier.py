from app.extensions import db
from datetime import datetime

class ProductSupplier(db.Model):
    __tablename__ = 'product_supplier'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    cost = db.Column(db.Numeric(10,2), nullable=False)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, product_id, supplier_id, cost, created_by=None, created_at=None,
                 updated_by=None, updated_at=None):
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.cost = cost
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'supplier_id': self.supplier_id,
            'cost': str(self.cost),
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }