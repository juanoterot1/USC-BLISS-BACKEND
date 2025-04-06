from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.customer_route import CustomerRoute
from app.repositories.customer_route_repository import CustomerRouteRepository

logger = logging.getLogger(__name__)

class CustomerRouteService:
    @inject
    def __init__(self, customer_route_repository: CustomerRouteRepository):
        self.customer_route_repository = customer_route_repository

    def get_all_customer_routes(self):
        try:
            routes = self.customer_route_repository.get_all()
            return [cr.as_dict() for cr in routes]
        except Exception as e:
            logger.error(f"Error retrieving customer routes: {e}")
            raise BadRequest(f"Error retrieving customer routes: {str(e)}")

    def get_customer_route_by_id(self, customer_route_id):
        cr = self.customer_route_repository.get_by_id(customer_route_id)
        if not cr:
            logger.warning(f"CustomerRoute not found with ID: {customer_route_id}")
            raise NotFound(f"CustomerRoute with ID {customer_route_id} not found")
        return cr.as_dict()

    def create_customer_route(self, route_id, customer_id, created_by=None):
        cr = CustomerRoute(route_id, customer_id, created_by)
        new_cr = self.customer_route_repository.create(cr)
        return new_cr.as_dict()

    def update_customer_route(self, customer_route_id, **kwargs):
        cr = self.customer_route_repository.get_by_id(customer_route_id)
        if not cr:
            logger.warning(f"CustomerRoute not found with ID: {customer_route_id}")
            raise NotFound(f"CustomerRoute with ID {customer_route_id} not found")
        for key, value in kwargs.items():
            setattr(cr, key, value)
        self.customer_route_repository.update()
        return cr.as_dict()

    def delete_customer_route(self, customer_route_id):
        cr = self.customer_route_repository.get_by_id(customer_route_id)
        if not cr:
            logger.warning(f"CustomerRoute not found with ID: {customer_route_id}")
            raise NotFound(f"CustomerRoute with ID {customer_route_id} not found")
        self.customer_route_repository.delete(cr)
        return {"message": f"CustomerRoute with ID {customer_route_id} deleted"}
