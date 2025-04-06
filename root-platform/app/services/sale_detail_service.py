from flask_injector import inject
from werkzeug.exceptions import BadRequest, NotFound
import logging
from app.models.sale_detail import SaleDetail
from app.repositories.sale_detail_repository import SaleDetailRepository

logger = logging.getLogger(__name__)

class SaleDetailService:
    @inject
    def __init__(self, sale_detail_repository: SaleDetailRepository):
        self.sale_detail_repository = sale_detail_repository

    def get_all_sale_details(self):
        try:
            details = self.sale_detail_repository.get_all()
            return [detail.as_dict() for detail in details]
        except Exception as e:
            logger.error(f"Error retrieving sale details: {e}")
            raise BadRequest(f"Error retrieving sale details: {str(e)}")

    def get_sale_detail_by_id(self, sale_detail_id):
        detail = self.sale_detail_repository.get_by_id(sale_detail_id)
        if not detail:
            logger.warning(f"SaleDetail not found with ID: {sale_detail_id}")
            raise NotFound(f"SaleDetail with ID {sale_detail_id} not found")
        return detail.as_dict()

    def create_sale_detail(self, sale_id, product_id, quantity, unit_price, created_by=None):
        detail = SaleDetail(sale_id, product_id, quantity, unit_price, created_by)
        new_detail = self.sale_detail_repository.create(detail)
        return new_detail.as_dict()

    def update_sale_detail(self, sale_detail_id, **kwargs):
        detail = self.sale_detail_repository.get_by_id(sale_detail_id)
        if not detail:
            logger.warning(f"SaleDetail not found with ID: {sale_detail_id}")
            raise NotFound(f"SaleDetail with ID {sale_detail_id} not found")
        for key, value in kwargs.items():
            setattr(detail, key, value)
        self.sale_detail_repository.update()
        return detail.as_dict()

    def delete_sale_detail(self, sale_detail_id):
        detail = self.sale_detail_repository.get_by_id(sale_detail_id)
        if not detail:
            logger.warning(f"SaleDetail not found with ID: {sale_detail_id}")
            raise NotFound(f"SaleDetail with ID {sale_detail_id} not found")
        self.sale_detail_repository.delete(detail)
        return {"message": f"SaleDetail with ID {sale_detail_id} deleted"}
