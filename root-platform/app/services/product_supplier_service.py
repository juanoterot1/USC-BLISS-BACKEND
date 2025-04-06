from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.product_supplier import ProductSupplier
from app.repositories.product_supplier_repository import ProductSupplierRepository

logger = logging.getLogger(__name__)

class ProductSupplierService:
    @inject
    def __init__(self, product_supplier_repository: ProductSupplierRepository):
        self.product_supplier_repository = product_supplier_repository

    def get_all_product_suppliers(self):
        try:
            ps_list = self.product_supplier_repository.get_all()
            return [ps.as_dict() for ps in ps_list]
        except Exception as e:
            logger.error(f"Error retrieving product suppliers: {e}")
            raise BadRequest(f"Error retrieving product suppliers: {str(e)}")

    def get_product_supplier_by_id(self, ps_id):
        ps = self.product_supplier_repository.get_by_id(ps_id)
        if not ps:
            logger.warning(f"ProductSupplier not found with ID: {ps_id}")
            raise NotFound(f"ProductSupplier with ID {ps_id} not found")
        return ps.as_dict()

    def create_product_supplier(self, product_id, supplier_id, cost, created_by=None):
        ps = ProductSupplier(product_id, supplier_id, cost, created_by)
        new_ps = self.product_supplier_repository.create(ps)
        return new_ps.as_dict()

    def update_product_supplier(self, ps_id, **kwargs):
        ps = self.product_supplier_repository.get_by_id(ps_id)
        if not ps:
            logger.warning(f"ProductSupplier not found with ID: {ps_id}")
            raise NotFound(f"ProductSupplier with ID {ps_id} not found")
        for key, value in kwargs.items():
            setattr(ps, key, value)
        self.product_supplier_repository.update()
        return ps.as_dict()

    def delete_product_supplier(self, ps_id):
        ps = self.product_supplier_repository.get_by_id(ps_id)
        if not ps:
            logger.warning(f"ProductSupplier not found with ID: {ps_id}")
            raise NotFound(f"ProductSupplier with ID {ps_id} not found")
        self.product_supplier_repository.delete(ps)
        return {"message": f"ProductSupplier with ID {ps_id} deleted"}
