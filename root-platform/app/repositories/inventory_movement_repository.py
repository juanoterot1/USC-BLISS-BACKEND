from app.models.inventory_movement import InventoryMovement
from app.extensions import db

class InventoryMovementRepository:
    @staticmethod
    def get_all():
        return InventoryMovement.query.all()

    @staticmethod
    def get_by_id(movement_id):
        return InventoryMovement.query.get(movement_id)

    @staticmethod
    def create(inventory_movement):
        db.session.add(inventory_movement)
        db.session.commit()
        return inventory_movement

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(inventory_movement):
        db.session.delete(inventory_movement)
        db.session.commit()
