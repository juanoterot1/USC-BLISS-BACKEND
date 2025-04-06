from app.models.customer_route import CustomerRoute
from app.extensions import db

class CustomerRouteRepository:
    @staticmethod
    def get_all():
        return CustomerRoute.query.all()

    @staticmethod
    def get_by_id(customer_route_id):
        return CustomerRoute.query.get(customer_route_id)

    @staticmethod
    def create(customer_route):
        db.session.add(customer_route)
        db.session.commit()
        return customer_route

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(customer_route):
        db.session.delete(customer_route)
        db.session.commit()
