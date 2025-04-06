# app/controllers/route_controller.py
from flask import Blueprint, request
from flask_injector import inject
from app.services.route_service import RouteService
from werkzeug.exceptions import BadRequest, NotFound
from app.utils.response import api_response
import logging
logger = logging.getLogger(__name__)
route_bp = Blueprint('routes', __name__)

@route_bp.route('/routes', methods=['GET'])
@inject
def get_all_routes(route_service: RouteService):
    try:
        routes = route_service.get_all_routes()
        return api_response(True, result=routes, status=200)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@route_bp.route('/routes/<int:route_id>', methods=['GET'])
@inject
def get_route_by_id(route_id, route_service: RouteService):
    try:
        route = route_service.get_route_by_id(route_id)
        return api_response(True, result=[route], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@route_bp.route('/routes', methods=['POST'])
@inject
def create_route(route_service: RouteService):
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description')
        delivery_person_id = data.get('delivery_person_id')
        if not name or not delivery_person_id:
            raise BadRequest("name and delivery_person_id are required")
        route = route_service.create_route(name, description, delivery_person_id)
        return api_response(True, result=[route], status=201)
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@route_bp.route('/routes/<int:route_id>', methods=['PUT'])
@inject
def update_route(route_id, route_service: RouteService):
    try:
        data = request.json
        route = route_service.update_route(route_id, **data)
        return api_response(True, result=[route], status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except BadRequest as e:
        return api_response(False, status=400, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")

@route_bp.route('/routes/<int:route_id>', methods=['DELETE'])
@inject
def delete_route(route_id, route_service: RouteService):
    try:
        resp = route_service.delete_route(route_id)
        return api_response(True, result=resp, status=200)
    except NotFound as e:
        return api_response(False, status=404, message=str(e))
    except Exception as e:
        return api_response(False, status=500, message="An internal error occurred")
