from app.extensions import db
from datetime import datetime

class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sale.id'), nullable=False)
    receipt_number = db.Column(db.String(50), unique=True, nullable=False)
    generation_date = db.Column(db.DateTime, nullable=False)
    file_url = db.Column(db.String(255))  # File path of the generated receipt
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_by = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime)

    def __init__(self, sale_id, receipt_number, generation_date, file_url=None, created_by=None,
                 created_at=None, updated_by=None, updated_at=None):
        self.sale_id = sale_id
        self.receipt_number = receipt_number
        self.generation_date = generation_date
        self.file_url = file_url
        self.created_by = created_by
        self.created_at = created_at if created_at is not None else datetime.utcnow()
        self.updated_by = updated_by
        self.updated_at = updated_at

    def as_dict(self):
        return {
            'id': self.id,
            'sale_id': self.sale_id,
            'receipt_number': self.receipt_number,
            'generation_date': self.generation_date.isoformat() if self.generation_date else None,
            'file_url': self.file_url,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_by': self.updated_by,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }