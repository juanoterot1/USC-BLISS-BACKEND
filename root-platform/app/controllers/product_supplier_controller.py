# app/controllers/product_supplier_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.product_supplier_service import ProductSupplierService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
product_supplier_bp = Blueprint('product_suppliers', __name__)

@product_supplier_bp.route('/product_suppliers', methods=['GET'])
@inject
def get_all_product_suppliers(product_supplier_service: ProductSupplierService):
    try:
        ps_list = product_supplier_service.get_all_product_suppliers()
        return api_response(True, result=ps_list, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@product_supplier_bp.route('/product_suppliers/<int:ps_id>', methods=['GET'])
@inject
def get_product_supplier_by_id(ps_id, product_supplier_service: ProductSupplierService):
    try:
        ps = product_supplier_service.get_product_supplier_by_id(ps_id)
        return api_response(True, result=[ps], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@product_supplier_bp.route('/product_suppliers', methods=['POST'])
@inject
def create_product_supplier(product_supplier_service: ProductSupplierService):
    try:
        data = request.json
        product_id = data.get('product_id')
        supplier_id = data.get('supplier_id')
        cost = data.get('cost')
        if not product_id or not supplier_id or cost is None:
            raise BadRequest("product_id, supplier_id, and cost are required")
        ps = product_supplier_service.create_product_supplier(product_id, supplier_id, cost)
        return api_response(True, result=[ps], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@product_supplier_bp.route('/product_suppliers/<int:ps_id>', methods=['PUT'])
@inject
def update_product_supplier(ps_id, product_supplier_service: ProductSupplierService):
    try:
        data = request.json
        ps = product_supplier_service.update_product_supplier(ps_id, **data)
        return api_response(True, result=[ps], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@product_supplier_bp.route('/product_suppliers/<int:ps_id>', methods=['DELETE'])
@inject
def delete_product_supplier(ps_id, product_supplier_service: ProductSupplierService):
    try:
        resp = product_supplier_service.delete_product_supplier(ps_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
