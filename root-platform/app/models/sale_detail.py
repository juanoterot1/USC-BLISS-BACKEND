from app.extensions import db
from datetime import datetime

class SaleDetail(db.Model):
    __tablename__ = 'sale_detail'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10,2), nullable=False)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, sale_id, product_id, quantity, unit_price, created_by=None,
                 created_at=None, updated_by=None, updated_at=None):
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'sale_id': self.sale_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'unit_price': str(self.unit_price),
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }