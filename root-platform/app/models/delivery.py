from app.extensions import db
from datetime import datetime

class Delivery(db.Model):
    __tablename__ = 'delivery'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    delivery_person_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    delivery_status = db.Column(db.String(20), default='pending')  # e.g., 'pending', 'delivered', 'failed'
    delivery_date = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, sale_id, delivery_person_id, delivery_status='pending', delivery_date=None,
                 created_by=None, created_at=None, updated_by=None, updated_at=None):
        self.sale_id = sale_id
        self.delivery_person_id = delivery_person_id
        self.delivery_status = delivery_status
        self.delivery_date = delivery_date
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'sale_id': self.sale_id,
            'delivery_person_id': self.delivery_person_id,
            'delivery_status': self.delivery_status,
            'delivery_date': self.delivery_date.isoformat() if self.delivery_date else None,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }