# app/controllers/customer_route_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.customer_route_service import CustomerRouteService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
customer_route_bp = Blueprint('customer_routes', __name__)

@customer_route_bp.route('/customer_routes', methods=['GET'])
@inject
def get_all_customer_routes(customer_route_service: CustomerRouteService):
    try:
        routes = customer_route_service.get_all_customer_routes()
        return api_response(True, result=routes, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_route_bp.route('/customer_routes/<int:customer_route_id>', methods=['GET'])
@inject
def get_customer_route_by_id(customer_route_id, customer_route_service: CustomerRouteService):
    try:
        route = customer_route_service.get_customer_route_by_id(customer_route_id)
        return api_response(True, result=[route], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_route_bp.route('/customer_routes', methods=['POST'])
@inject
def create_customer_route(customer_route_service: CustomerRouteService):
    try:
        data = request.json
        route_id = data.get('route_id')
        customer_id = data.get('customer_id')
        if not route_id or not customer_id:
            raise BadRequest("route_id and customer_id are required")
        route = customer_route_service.create_customer_route(route_id, customer_id)
        return api_response(True, result=[route], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_route_bp.route('/customer_routes/<int:customer_route_id>', methods=['PUT'])
@inject
def update_customer_route(customer_route_id, customer_route_service: CustomerRouteService):
    try:
        data = request.json
        route = customer_route_service.update_customer_route(customer_route_id, **data)
        return api_response(True, result=[route], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@customer_route_bp.route('/customer_routes/<int:customer_route_id>', methods=['DELETE'])
@inject
def delete_customer_route(customer_route_id, customer_route_service: CustomerRouteService):
    try:
        resp = customer_route_service.delete_customer_route(customer_route_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
