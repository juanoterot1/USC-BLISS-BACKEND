from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.sale import Sale
from app.repositories.sale_repository import SaleRepository

logger = logging.getLogger(__name__)

class SaleService:
    @inject
    def __init__(self, sale_repository: SaleRepository):
        self.sale_repository = sale_repository

    def get_all_sales(self):
        try:
            sales = self.sale_repository.get_all()
            return [sale.as_dict() for sale in sales]
        except Exception as e:
            logger.error(f"Error retrieving sales: {e}")
            raise BadRequest(f"Error retrieving sales: {str(e)}")

    def get_sale_by_id(self, sale_id):
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            logger.warning(f"Sale not found with ID: {sale_id}")
            raise NotFound(f"Sale with ID {sale_id} not found")
        return sale.as_dict()

    def create_sale(self, customer_id, total, sale_date, payment_status='pending', created_by=None):
        sale = Sale(customer_id, total, sale_date, payment_status, created_by)
        new_sale = self.sale_repository.create(sale)
        return new_sale.as_dict()

    def update_sale(self, sale_id, **kwargs):
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            logger.warning(f"Sale not found with ID: {sale_id}")
            raise NotFound(f"Sale with ID {sale_id} not found")
        for key, value in kwargs.items():
            setattr(sale, key, value)
        self.sale_repository.update()
        return sale.as_dict()

    def delete_sale(self, sale_id):
        sale = self.sale_repository.get_by_id(sale_id)
        if not sale:
            logger.warning(f"Sale not found with ID: {sale_id}")
            raise NotFound(f"Sale with ID {sale_id} not found")
        self.sale_repository.delete(sale)
        return {"message": f"Sale with ID {sale_id} deleted"}
