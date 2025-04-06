from app.extensions import db
from datetime import datetime

class Supplier(db.Model):
    __tablename__ = 'supplier'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.Text)
    commission = db.Column(db.Numeric(5,2))  # Percentage or fixed amount
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    # Relaciones
    product_suppliers = db.relationship('ProductSupplier', backref='supplier', lazy=True)

    def __init__(self, name, contact=None, commission=None, created_by=None, created_at=None,
                 updated_by=None, updated_at=None):
        self.name = name
        self.contact = contact
        self.commission = commission
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'contact': self.contact,
            'commission': str(self.commission) if self.commission is not None else None,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
