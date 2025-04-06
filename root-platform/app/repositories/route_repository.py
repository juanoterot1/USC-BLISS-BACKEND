from app.models.route import Route
from app.extensions import db

class RouteRepository:
    @staticmethod
    def get_all():
        return Route.query.all()

    @staticmethod
    def get_by_id(route_id):
        return Route.query.get(route_id)

    @staticmethod
    def create(route):
        db.session.add(route)
        db.session.commit()
        return route

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(route):
        db.session.delete(route)
        db.session.commit()
