# app/controllers/sale_detail_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.sale_detail_service import SaleDetailService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
sale_detail_bp = Blueprint('sale_details', __name__)

@sale_detail_bp.route('/sale_details', methods=['GET'])
@inject
def get_all_sale_details(sale_detail_service: SaleDetailService):
    try:
        details = sale_detail_service.get_all_sale_details()
        return api_response(True, result=details, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_detail_bp.route('/sale_details/<int:sale_detail_id>', methods=['GET'])
@inject
def get_sale_detail_by_id(sale_detail_id, sale_detail_service: SaleDetailService):
    try:
        detail = sale_detail_service.get_sale_detail_by_id(sale_detail_id)
        return api_response(True, result=[detail], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_detail_bp.route('/sale_details', methods=['POST'])
@inject
def create_sale_detail(sale_detail_service: SaleDetailService):
    try:
        data = request.json
        sale_id = data.get('sale_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity')
        unit_price = data.get('unit_price')
        if not sale_id or not product_id or quantity is None or unit_price is None:
            raise BadRequest("sale_id, product_id, quantity, and unit_price are required")
        detail = sale_detail_service.create_sale_detail(sale_id, product_id, quantity, unit_price)
        return api_response(True, result=[detail], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_detail_bp.route('/sale_details/<int:sale_detail_id>', methods=['PUT'])
@inject
def update_sale_detail(sale_detail_id, sale_detail_service: SaleDetailService):
    try:
        data = request.json
        detail = sale_detail_service.update_sale_detail(sale_detail_id, **data)
        return api_response(True, result=[detail], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@sale_detail_bp.route('/sale_details/<int:sale_detail_id>', methods=['DELETE'])
@inject
def delete_sale_detail(sale_detail_id, sale_detail_service: SaleDetailService):
    try:
        resp = sale_detail_service.delete_sale_detail(sale_detail_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
