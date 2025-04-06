from app.models.customer import Customer
from app.extensions import db

class CustomerRepository:
    @staticmethod
    def get_all():
        return Customer.query.all()

    @staticmethod
    def get_by_id(customer_id):
        return Customer.query.get(customer_id)

    @staticmethod
    def create(customer):
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def update():
        db.session.commit()

    @staticmethod
    def delete(customer):
        db.session.delete(customer)
        db.session.commit()
