# app/controllers/sale_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.sale_service import SaleService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
sale_bp = Blueprint('sales', __name__)

@sale_bp.route('/sales', methods=['GET'])
@inject
def get_all_sales(sale_service: SaleService):
    try:
        sales = sale_service.get_all_sales()
        return api_response(True, result=sales, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_bp.route('/sales/<int:sale_id>', methods=['GET'])
@inject
def get_sale_by_id(sale_id, sale_service: SaleService):
    try:
        sale = sale_service.get_sale_by_id(sale_id)
        return api_response(True, result=[sale], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_bp.route('/sales', methods=['POST'])
@inject
def create_sale(sale_service: SaleService):
    try:
        data = request.json
        customer_id = data.get('customer_id')
        total = data.get('total')
        sale_date = data.get('sale_date')
        payment_status = data.get('payment_status', 'pending')
        if not customer_id or total is None or not sale_date:
            raise BadRequest("customer_id, total, and sale_date are required")
        sale = sale_service.create_sale(customer_id, total, sale_date, payment_status)
        return api_response(True, result=[sale], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_bp.route('/sales/<int:sale_id>', methods=['PUT'])
@inject
def update_sale(sale_id, sale_service: SaleService):
    try:
        data = request.json
        sale = sale_service.update_sale(sale_id, **data)
        return api_response(True, result=[sale], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_bp.route('/sales/<int:sale_id>', methods=['DELETE'])
@inject
def delete_sale(sale_id, sale_service: SaleService):
    try:
        resp = sale_service.delete_sale(sale_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
