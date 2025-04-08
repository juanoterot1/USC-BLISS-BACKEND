from flask import Flask, jsonify
from flask_cors import CORS
from flask_injector import FlaskInjector
from injector import singleton
import logging

from .extensions import db, init_logging, jwt  # Asegúrate de importar 'jwt'

# Controllers
from .controllers.user_controller import user_bp
from .controllers.product_controller import product_bp
from .controllers.inventory_movement_controller import inventory_movement_bp
from .controllers.customer_controller import customer_bp
from .controllers.route_controller import route_bp
from .controllers.customer_route_controller import customer_route_bp
from .controllers.sale_controller import sale_bp
from .controllers.sale_detail_controller import sale_detail_bp
from .controllers.receipt_controller import receipt_bp
from .controllers.delivery_controller import delivery_bp
from .controllers.payment_controller import payment_bp
from .controllers.supplier_controller import supplier_bp
from .controllers.product_supplier_controller import product_supplier_bp
from .controllers.auth_controller import auth_bp

# Services
from .services.user_service import UserService
from .services.product_service import ProductService
from .services.inventory_movement_service import InventoryMovementService
from .services.customer_service import CustomerService
from .services.route_service import RouteService
from .services.customer_route_service import CustomerRouteService
from .services.sale_service import SaleService
from .services.sale_detail_service import SaleDetailService
from .services.receipt_service import ReceiptService
from .services.delivery_service import DeliveryService
from .services.payment_service import PaymentService
from .services.supplier_service import SupplierService
from .services.product_supplier_service import ProductSupplierService
from .services.auth_service import AuthService

def configure(binder):
    binder.bind(UserService, to=UserService, scope=singleton)
    binder.bind(ProductService, to=ProductService, scope=singleton)
    binder.bind(InventoryMovementService, to=InventoryMovementService, scope=singleton)
    binder.bind(CustomerService, to=CustomerService, scope=singleton)
    binder.bind(RouteService, to=RouteService, scope=singleton)
    binder.bind(CustomerRouteService, to=CustomerRouteService, scope=singleton)
    binder.bind(SaleService, to=SaleService, scope=singleton)
    binder.bind(SaleDetailService, to=SaleDetailService, scope=singleton)
    binder.bind(ReceiptService, to=ReceiptService, scope=singleton)
    binder.bind(DeliveryService, to=DeliveryService, scope=singleton)
    binder.bind(PaymentService, to=PaymentService, scope=singleton)
    binder.bind(SupplierService, to=SupplierService, scope=singleton)
    binder.bind(ProductSupplierService, to=ProductSupplierService, scope=singleton)
    binder.bind(AuthService, to=AuthService, scope=singleton)

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('app.config.Config')
    
    # Inicializa la base de datos y JWTManager
    db.init_app(app)
    jwt.init_app(app)  # Inicializamos JWTManager
    
    logger = init_logging()
    logger.info("API Initialized")
    
    app.register_blueprint(user_bp, url_prefix='/api/v1')
    app.register_blueprint(product_bp, url_prefix='/api/v1')
    app.register_blueprint(inventory_movement_bp, url_prefix='/api/v1')
    app.register_blueprint(customer_bp, url_prefix='/api/v1')
    app.register_blueprint(route_bp, url_prefix='/api/v1')
    app.register_blueprint(customer_route_bp, url_prefix='/api/v1')
    app.register_blueprint(sale_bp, url_prefix='/api/v1')
    app.register_blueprint(sale_detail_bp, url_prefix='/api/v1')
    app.register_blueprint(receipt_bp, url_prefix='/api/v1')
    app.register_blueprint(delivery_bp, url_prefix='/api/v1')
    app.register_blueprint(payment_bp, url_prefix='/api/v1')
    app.register_blueprint(supplier_bp, url_prefix='/api/v1')
    app.register_blueprint(product_supplier_bp, url_prefix='/api/v1')
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')

    FlaskInjector(app=app, modules=[configure])

    @app.route('/health')
    def health_check():
        logger.info("Health check passed")
        return jsonify({'status': 'Healthy'}), 200

    return app
