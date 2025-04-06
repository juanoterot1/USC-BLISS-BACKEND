from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.delivery import Delivery
from app.repositories.delivery_repository import DeliveryRepository

logger = logging.getLogger(__name__)

class DeliveryService:
    @inject
    def __init__(self, delivery_repository: DeliveryRepository):
        self.delivery_repository = delivery_repository

    def get_all_deliveries(self):
        try:
            deliveries = self.delivery_repository.get_all()
            return [delivery.as_dict() for delivery in deliveries]
        except Exception as e:
            logger.error(f"Error retrieving deliveries: {e}")
            raise BadRequest(f"Error retrieving deliveries: {str(e)}")

    def get_delivery_by_id(self, delivery_id):
        delivery = self.delivery_repository.get_by_id(delivery_id)
        if not delivery:
            logger.warning(f"Delivery not found with ID: {delivery_id}")
            raise NotFound(f"Delivery with ID {delivery_id} not found")
        return delivery.as_dict()

    def create_delivery(self, sale_id, delivery_person_id, delivery_status='pending', delivery_date=None, created_by=None):
        delivery = Delivery(sale_id, delivery_person_id, delivery_status, delivery_date, created_by)
        new_delivery = self.delivery_repository.create(delivery)
        return new_delivery.as_dict()

    def update_delivery(self, delivery_id, **kwargs):
        delivery = self.delivery_repository.get_by_id(delivery_id)
        if not delivery:
            logger.warning(f"Delivery not found with ID: {delivery_id}")
            raise NotFound(f"Delivery with ID {delivery_id} not found")
        for key, value in kwargs.items():
            setattr(delivery, key, value)
        self.delivery_repository.update()
        return delivery.as_dict()

    def delete_delivery(self, delivery_id):
        delivery = self.delivery_repository.get_by_id(delivery_id)
        if not delivery:
            logger.warning(f"Delivery not found with ID: {delivery_id}")
            raise NotFound(f"Delivery with ID {delivery_id} not found")
        self.delivery_repository.delete(delivery)
        return {"message": f"Delivery with ID {delivery_id} deleted"}
