# app/controllers/inventory_movement_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.inventory_movement_service import InventoryMovementService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
inventory_movement_bp = Blueprint('inventory_movements', __name__)

@inventory_movement_bp.route('/inventory_movements', methods=['GET'])
@inject
def get_all_inventory_movements(inventory_movement_service: InventoryMovementService):
    try:
        movements = inventory_movement_service.get_all_movements()
        return api_response(True, result=movements, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@inventory_movement_bp.route('/inventory_movements/<int:movement_id>', methods=['GET'])
@inject
def get_inventory_movement_by_id(movement_id, inventory_movement_service: InventoryMovementService):
    try:
        movement = inventory_movement_service.get_movement_by_id(movement_id)
        return api_response(True, result=[movement], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@inventory_movement_bp.route('/inventory_movements', methods=['POST'])
@inject
def create_inventory_movement(inventory_movement_service: InventoryMovementService):
    try:
        data = request.json
        product_id = data.get('product_id')
        movement_type = data.get('movement_type')
        quantity = data.get('quantity')
        description = data.get('description')
        movement_date = data.get('movement_date')
        if not product_id or not movement_type or not quantity or not movement_date:
            raise BadRequest("product_id, movement_type, quantity, and movement_date are required")
        movement = inventory_movement_service.create_movement(product_id, movement_type, quantity, description, movement_date)
        return api_response(True, result=[movement], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@inventory_movement_bp.route('/inventory_movements/<int:movement_id>', methods=['PUT'])
@inject
def update_inventory_movement(movement_id, inventory_movement_service: InventoryMovementService):
    try:
        data = request.json
        movement = inventory_movement_service.update_movement(movement_id, **data)
        return api_response(True, result=[movement], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@inventory_movement_bp.route('/inventory_movements/<int:movement_id>', methods=['DELETE'])
@inject
def delete_inventory_movement(movement_id, inventory_movement_service: InventoryMovementService):
    try:
        resp = inventory_movement_service.delete_movement(movement_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
