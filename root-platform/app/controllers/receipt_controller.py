# app/controllers/receipt_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.receipt_service import ReceiptService
from werkzeug.exceptions import BadRequest, NotFound, Conflict
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
receipt_bp = Blueprint('receipts', __name__)

@receipt_bp.route('/receipts', methods=['GET'])
@inject
def get_all_receipts(receipt_service: ReceiptService):
    try:
        receipts = receipt_service.get_all_receipts()
        return api_response(True, result=receipts, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@receipt_bp.route('/receipts/<int:receipt_id>', methods=['GET'])
@inject
def get_receipt_by_id(receipt_id, receipt_service: ReceiptService):
    try:
        receipt = receipt_service.get_receipt_by_id(receipt_id)
        return api_response(True, result=[receipt], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@receipt_bp.route('/receipts', methods=['POST'])
@inject
def create_receipt(receipt_service: ReceiptService):
    try:
        data = request.json
        sale_id = data.get('sale_id')
        receipt_number = data.get('receipt_number')
        generation_date = data.get('generation_date')
        file_url = data.get('file_url')
        if not sale_id or not receipt_number or not generation_date:
            raise BadRequest("sale_id, receipt_number, and generation_date are required")
        receipt = receipt_service.create_receipt(sale_id, receipt_number, generation_date, file_url)
        return api_response(True, result=[receipt], status=201)
    except Conflict as e:
        return api_response(False, status=409, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@receipt_bp.route('/receipts/<int:receipt_id>', methods=['PUT'])
@inject
def update_receipt(receipt_id, receipt_service: ReceiptService):
    try:
        data = request.json
        receipt = receipt_service.update_receipt(receipt_id, **data)
        return api_response(True, result=[receipt], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@receipt_bp.route('/receipts/<int:receipt_id>', methods=['DELETE'])
@inject
def delete_receipt(receipt_id, receipt_service: ReceiptService):
    try:
        resp = receipt_service.delete_receipt(receipt_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
