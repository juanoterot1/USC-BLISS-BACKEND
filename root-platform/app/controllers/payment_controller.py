# app/controllers/payment_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.payment_service import PaymentService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
payment_bp = Blueprint('payments', __name__)

@payment_bp.route('/payments', methods=['GET'])
@inject
def get_all_payments(payment_service: PaymentService):
    try:
        payments = payment_service.get_all_payments()
        return api_response(True, result=payments, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@payment_bp.route('/payments/<int:payment_id>', methods=['GET'])
@inject
def get_payment_by_id(payment_id, payment_service: PaymentService):
    try:
        payment = payment_service.get_payment_by_id(payment_id)
        return api_response(True, result=[payment], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@payment_bp.route('/payments', methods=['POST'])
@inject
def create_payment(payment_service: PaymentService):
    try:
        data = request.json
        sale_id = data.get('sale_id')
        amount = data.get('amount')
        payment_date = data.get('payment_date')
        payment_method = data.get('payment_method')
        status = data.get('status', 'pending')
        if not sale_id or amount is None or not payment_date:
            raise BadRequest("sale_id, amount, and payment_date are required")
        payment = payment_service.create_payment(sale_id, amount, payment_date, payment_method, status)
        return api_response(True, result=[payment], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@payment_bp.route('/payments/<int:payment_id>', methods=['PUT'])
@inject
def update_payment(payment_id, payment_service: PaymentService):
    try:
        data = request.json
        payment = payment_service.update_payment(payment_id, **data)
        return api_response(True, result=[payment], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@payment_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
@inject
def delete_payment(payment_id, payment_service: PaymentService):
    try:
        resp = payment_service.delete_payment(payment_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
