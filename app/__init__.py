from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from app.models.user import User
        return User.query.get(int(user_id))

    from app.routes import administrador_routes, bebida_routes,cliente_routes, empleado_routes, factura_routes,ingrediente_routes, mesa_routes, orden_detalle_routes, plato_routes, proveedor_routes, reserva_routes, rol_routes, auth, carrito_routes
    
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(bebida_routes.bp)
    app.register_blueprint(cliente_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(factura_routes.bp)
    app.register_blueprint(ingrediente_routes.bp)
    app.register_blueprint(mesa_routes.bp)
    app.register_blueprint(orden_detalle_routes.bp)
    app.register_blueprint(plato_routes.bp)
    app.register_blueprint(proveedor_routes.bp)
    app.register_blueprint(reserva_routes.bp)
    app.register_blueprint(rol_routes.bp) 
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(carrito_routes.bp)


    return app