from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.inventory_movement import InventoryMovement
from app.repositories.inventory_movement_repository import InventoryMovementRepository

logger = logging.getLogger(__name__)

class InventoryMovementService:
    @inject
    def __init__(self, inventory_movement_repository: InventoryMovementRepository):
        self.inventory_movement_repository = inventory_movement_repository

    def get_all_movements(self):
        try:
            movements = self.inventory_movement_repository.get_all()
            return [movement.as_dict() for movement in movements]
        except Exception as e:
            logger.error(f"Error retrieving movements: {e}")
            raise BadRequest(f"Error retrieving movements: {str(e)}")

    def get_movement_by_id(self, movement_id):
        movement = self.inventory_movement_repository.get_by_id(movement_id)
        if not movement:
            logger.warning(f"Movement not found with ID: {movement_id}")
            raise NotFound(f"Movement with ID {movement_id} not found")
        return movement.as_dict()

    def create_movement(self, product_id, movement_type, quantity, description, movement_date, created_by=None):
        movement = InventoryMovement(product_id, movement_type, quantity, description, movement_date, created_by)
        new_movement = self.inventory_movement_repository.create(movement)
        return new_movement.as_dict()

    def update_movement(self, movement_id, **kwargs):
        movement = self.inventory_movement_repository.get_by_id(movement_id)
        if not movement:
            logger.warning(f"Movement not found with ID: {movement_id}")
            raise NotFound(f"Movement with ID {movement_id} not found")
        for key, value in kwargs.items():
            setattr(movement, key, value)
        self.inventory_movement_repository.update()
        return movement.as_dict()

    def delete_movement(self, movement_id):
        movement = self.inventory_movement_repository.get_by_id(movement_id)
        if not movement:
            logger.warning(f"Movement not found with ID: {movement_id}")
            raise NotFound(f"Movement with ID {movement_id} not found")
        self.inventory_movement_repository.delete(movement)
        return {"message": f"Movement with ID {movement_id} deleted"}
