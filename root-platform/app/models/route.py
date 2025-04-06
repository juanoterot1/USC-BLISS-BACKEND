from app.extensions import db
from datetime import datetime

class Route(db.Model):
    __tablename__ = 'route'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    delivery_person_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # User with role 'delivery'
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    # Relaciones
    customer_routes = db.relationship('CustomerRoute', backref='route', lazy=True)

    def __init__(self, name, description, delivery_person_id, created_by=None, created_at=None,
                 updated_by=None, updated_at=None):
        self.name = name
        self.description = description
        self.delivery_person_id = delivery_person_id
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'delivery_person_id': self.delivery_person_id,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }