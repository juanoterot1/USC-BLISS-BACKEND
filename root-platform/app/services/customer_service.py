from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository

logger = logging.getLogger(__name__)

class CustomerService:
    @inject
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository = customer_repository

    def get_all_customers(self):
        try:
            customers = self.customer_repository.get_all()
            return [customer.as_dict() for customer in customers]
        except Exception as e:
            logger.error(f"Error retrieving customers: {e}")
            raise BadRequest(f"Error retrieving customers: {str(e)}")

    def get_customer_by_id(self, customer_id):
        customer = self.customer_repository.get_by_id(customer_id)
        if not customer:
            logger.warning(f"Customer not found with ID: {customer_id}")
            raise NotFound(f"Customer with ID {customer_id} not found")
        return customer.as_dict()

    def create_customer(self, user_id, name, address, phone=None, created_by=None):
        customer = Customer(user_id, name, address, phone, created_by)
        new_customer = self.customer_repository.create(customer)
        return new_customer.as_dict()

    def update_customer(self, customer_id, **kwargs):
        customer = self.customer_repository.get_by_id(customer_id)
        if not customer:
            logger.warning(f"Customer not found with ID: {customer_id}")
            raise NotFound(f"Customer with ID {customer_id} not found")
        for key, value in kwargs.items():
            setattr(customer, key, value)
        self.customer_repository.update()
        return customer.as_dict()

    def delete_customer(self, customer_id):
        customer = self.customer_repository.get_by_id(customer_id)
        if not customer:
            logger.warning(f"Customer not found with ID: {customer_id}")
            raise NotFound(f"Customer with ID {customer_id} not found")
        self.customer_repository.delete(customer)
        return {"message": f"Customer with ID {customer_id} deleted"}
