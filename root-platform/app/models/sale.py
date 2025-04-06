from app.extensions import db
from datetime import datetime

class Sale(db.Model):
    __tablename__ = 'sale'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    total = db.Column(db.Numeric(10,2), nullable=False)
    payment_status = db.Column(db.String(20), default='pending')  # e.g., 'pending', 'completed', 'failed'
    sale_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    # Relaciones
    sale_details = db.relationship('SaleDetail', backref='sale', lazy=True)
    receipts = db.relationship('Receipt', backref='sale', lazy=True)
    deliveries = db.relationship('Delivery', backref='sale', lazy=True)
    payments = db.relationship('Payment', backref='sale', lazy=True)

    def __init__(self, customer_id, total, sale_date, payment_status='pending', created_by=None,
                 created_at=None, updated_by=None, updated_at=None):
        self.customer_id = customer_id
        self.total = total
        self.payment_status = payment_status
        self.sale_date = sale_date
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'total': str(self.total),
            'payment_status': self.payment_status,
            'sale_date': self.sale_date.isoformat() if self.sale_date else None,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }