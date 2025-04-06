# app/controllers/customer_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.customer_service import CustomerService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
customer_bp = Blueprint('customers', __name__)

@customer_bp.route('/customers', methods=['GET'])
@inject
def get_all_customers(customer_service: CustomerService):
    try:
        customers = customer_service.get_all_customers()
        return api_response(True, result=customers, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@inject
def get_customer_by_id(customer_id, customer_service: CustomerService):
    try:
        customer = customer_service.get_customer_by_id(customer_id)
        return api_response(True, result=[customer], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_bp.route('/customers', methods=['POST'])
@inject
def create_customer(customer_service: CustomerService):
    try:
        data = request.json
        user_id = data.get('user_id')
        name = data.get('name')
        address = data.get('address')
        phone = data.get('phone')
        if not user_id or not name or not address:
            raise BadRequest("user_id, name, and address are required")
        customer = customer_service.create_customer(user_id, name, address, phone)
        return api_response(True, result=[customer], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@inject
def update_customer(customer_id, customer_service: CustomerService):
    try:
        data = request.json
        customer = customer_service.update_customer(customer_id, **data)
        return api_response(True, result=[customer], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@inject
def delete_customer(customer_id, customer_service: CustomerService):
    try:
        resp = customer_service.delete_customer(customer_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
