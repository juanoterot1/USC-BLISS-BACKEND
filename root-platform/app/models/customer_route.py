from app.extensions import db
from datetime import datetime

class CustomerRoute(db.Model):
    __tablename__ = 'customer_route'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, route_id, customer_id, created_by=None, created_at=None,
                 updated_by=None, updated_at=None):
        self.route_id = route_id
        self.customer_id = customer_id
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'route_id': self.route_id,
            'customer_id': self.customer_id,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }