# app/controllers/delivery_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.delivery_service import DeliveryService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
delivery_bp = Blueprint('deliveries', __name__)

@delivery_bp.route('/deliveries', methods=['GET'])
@inject
def get_all_deliveries(delivery_service: DeliveryService):
    try:
        deliveries = delivery_service.get_all_deliveries()
        return api_response(True, result=deliveries, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['GET'])
@inject
def get_delivery_by_id(delivery_id, delivery_service: DeliveryService):
    try:
        delivery = delivery_service.get_delivery_by_id(delivery_id)
        return api_response(True, result=[delivery], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@delivery_bp.route('/deliveries', methods=['POST'])
@inject
def create_delivery(delivery_service: DeliveryService):
    try:
        data = request.json
        sale_id = data.get('sale_id')
        delivery_person_id = data.get('delivery_person_id')
        delivery_status = data.get('delivery_status', 'pending')
        delivery_date = data.get('delivery_date')
        if not sale_id or not delivery_person_id:
            raise BadRequest("sale_id and delivery_person_id are required")
        delivery = delivery_service.create_delivery(sale_id, delivery_person_id, delivery_status, delivery_date)
        return api_response(True, result=[delivery], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['PUT'])
@inject
def update_delivery(delivery_id, delivery_service: DeliveryService):
    try:
        data = request.json
        delivery = delivery_service.update_delivery(delivery_id, **data)
        return api_response(True, result=[delivery], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
@inject
def delete_delivery(delivery_id, delivery_service: DeliveryService):
    try:
        resp = delivery_service.delete_delivery(delivery_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
