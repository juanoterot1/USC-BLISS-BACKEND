from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.route import Route
from app.repositories.route_repository import RouteRepository

logger = logging.getLogger(__name__)

class RouteService:
    @inject
    def __init__(self, route_repository: RouteRepository):
        self.route_repository = route_repository

    def get_all_routes(self):
        try:
            routes = self.route_repository.get_all()
            return [route.as_dict() for route in routes]
        except Exception as e:
            logger.error(f"Error retrieving routes: {e}")
            raise BadRequest(f"Error retrieving routes: {str(e)}")

    def get_route_by_id(self, route_id):
        route = self.route_repository.get_by_id(route_id)
        if not route:
            logger.warning(f"Route not found with ID: {route_id}")
            raise NotFound(f"Route with ID {route_id} not found")
        return route.as_dict()

    def create_route(self, name, description, delivery_person_id, created_by=None):
        route = Route(name, description, delivery_person_id, created_by)
        new_route = self.route_repository.create(route)
        return new_route.as_dict()

    def update_route(self, route_id, **kwargs):
        route = self.route_repository.get_by_id(route_id)
        if not route:
            logger.warning(f"Route not found with ID: {route_id}")
            raise NotFound(f"Route with ID {route_id} not found")
        for key, value in kwargs.items():
            setattr(route, key, value)
        self.route_repository.update()
        return route.as_dict()

    def delete_route(self, route_id):
        route = self.route_repository.get_by_id(route_id)
        if not route:
            logger.warning(f"Route not found with ID: {route_id}")
            raise NotFound(f"Route with ID {route_id} not found")
        self.route_repository.delete(route)
        return {"message": f"Route with ID {route_id} deleted"}
