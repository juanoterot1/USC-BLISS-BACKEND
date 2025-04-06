from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound, Conflict
import logging
from app.models.supplier import Supplier
from app.repositories.supplier_repository import SupplierRepository

logger = logging.getLogger(__name__)

class SupplierService:
    @inject
    def __init__(self, supplier_repository: SupplierRepository):
        self.supplier_repository = supplier_repository

    def get_all_suppliers(self):
        try:
            suppliers = self.supplier_repository.get_all()
            return [supplier.as_dict() for supplier in suppliers]
        except Exception as e:
            logger.error(f"Error retrieving suppliers: {e}")
            raise BadRequest(f"Error retrieving suppliers: {str(e)}")

    def get_supplier_by_id(self, supplier_id):
        supplier = self.supplier_repository.get_by_id(supplier_id)
        if not supplier:
            logger.warning(f"Supplier not found with ID: {supplier_id}")
            raise NotFound(f"Supplier with ID {supplier_id} not found")
        return supplier.as_dict()

    def create_supplier(self, name, contact=None, commission=None, created_by=None):
        supplier = Supplier(name, contact, commission, created_by)
        new_supplier = self.supplier_repository.create(supplier)
        return new_supplier.as_dict()

    def update_supplier(self, supplier_id, **kwargs):
        supplier = self.supplier_repository.get_by_id(supplier_id)
        if not supplier:
            logger.warning(f"Supplier not found with ID: {supplier_id}")
            raise NotFound(f"Supplier with ID {supplier_id} not found")
        for key, value in kwargs.items():
            setattr(supplier, key, value)
        self.supplier_repository.update()
        return supplier.as_dict()

    def delete_supplier(self, supplier_id):
        supplier = self.supplier_repository.get_by_id(supplier_id)
        if not supplier:
            logger.warning(f"Supplier not found with ID: {supplier_id}")
            raise NotFound(f"Supplier with ID {supplier_id} not found")
        self.supplier_repository.delete(supplier)
        return {"message": f"Supplier with ID {supplier_id} deleted"}
