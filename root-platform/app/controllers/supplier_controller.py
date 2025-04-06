# app/controllers/supplier_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.supplier_service import SupplierService
from werkzeug.exceptions import BadRequest, NotFound, Conflict
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
supplier_bp = Blueprint('suppliers', __name__)

@supplier_bp.route('/suppliers', methods=['GET'])
@inject
def get_all_suppliers(supplier_service: SupplierService):
    try:
        suppliers = supplier_service.get_all_suppliers()
        return api_response(True, result=suppliers, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['GET'])
@inject
def get_supplier_by_id(supplier_id, supplier_service: SupplierService):
    try:
        supplier = supplier_service.get_supplier_by_id(supplier_id)
        return api_response(True, result=[supplier], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@supplier_bp.route('/suppliers', methods=['POST'])
@inject
def create_supplier(supplier_service: SupplierService):
    try:
        data = request.json
        name = data.get('name')
        contact = data.get('contact')
        commission = data.get('commission')
        if not name:
            raise BadRequest("name is required")
        supplier = supplier_service.create_supplier(name, contact, commission)
        return api_response(True, result=[supplier], status=201)
    except Conflict as e:
        return api_response(False, status=409, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['PUT'])
@inject
def update_supplier(supplier_id, supplier_service: SupplierService):
    try:
        data = request.json
        supplier = supplier_service.update_supplier(supplier_id, **data)
        return api_response(True, result=[supplier], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@supplier_bp.route('/suppliers/<int:supplier_id>', methods=['DELETE'])
@inject
def delete_supplier(supplier_id, supplier_service: SupplierService):
    try:
        resp = supplier_service.delete_supplier(supplier_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
