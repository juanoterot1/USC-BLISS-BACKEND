from app.extensions import db
from datetime import datetime

class InventoryMovement(db.Model):
    __tablename__ = 'inventory_movement'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    movement_type = db.Column(db.String(20), nullable=False)  # Values: 'in', 'out'
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)  # Details of the movement (sale, promotion, giveaway, etc.)
    movement_date = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, product_id, movement_type, quantity, description, movement_date,
                 created_by=None, created_at=None, updated_by=None, updated_at=None):
        self.product_id = product_id
        self.movement_type = movement_type
        self.quantity = quantity
        self.description = description
        self.movement_date = movement_date
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'movement_type': self.movement_type,
            'quantity': self.quantity,
            'description': self.description,
            'movement_date': self.movement_date.isoformat() if self.movement_date else None,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }