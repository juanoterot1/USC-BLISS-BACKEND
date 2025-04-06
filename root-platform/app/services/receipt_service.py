from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.receipt import Receipt
from app.repositories.receipt_repository import ReceiptRepository

logger = logging.getLogger(__name__)

class ReceiptService:
    @inject
    def __init__(self, receipt_repository: ReceiptRepository):
        self.receipt_repository = receipt_repository

    def get_all_receipts(self):
        try:
            receipts = self.receipt_repository.get_all()
            return [receipt.as_dict() for receipt in receipts]
        except Exception as e:
            logger.error(f"Error retrieving receipts: {e}")
            raise BadRequest(f"Error retrieving receipts: {str(e)}")

    def get_receipt_by_id(self, receipt_id):
        receipt = self.receipt_repository.get_by_id(receipt_id)
        if not receipt:
            logger.warning(f"Receipt not found with ID: {receipt_id}")
            raise NotFound(f"Receipt with ID {receipt_id} not found")
        return receipt.as_dict()

    def create_receipt(self, sale_id, receipt_number, generation_date, file_url=None, created_by=None):
        receipt = Receipt(sale_id, receipt_number, generation_date, file_url, created_by)
        new_receipt = self.receipt_repository.create(receipt)
        return new_receipt.as_dict()

    def update_receipt(self, receipt_id, **kwargs):
        receipt = self.receipt_repository.get_by_id(receipt_id)
        if not receipt:
            logger.warning(f"Receipt not found with ID: {receipt_id}")
            raise NotFound(f"Receipt with ID {receipt_id} not found")
        for key, value in kwargs.items():
            setattr(receipt, key, value)
        self.receipt_repository.update()
        return receipt.as_dict()

    def delete_receipt(self, receipt_id):
        receipt = self.receipt_repository.get_by_id(receipt_id)
        if not receipt:
            logger.warning(f"Receipt not found with ID: {receipt_id}")
            raise NotFound(f"Receipt with ID {receipt_id} not found")
        self.receipt_repository.delete(receipt)
        return {"message": f"Receipt with ID {receipt_id} deleted"}
