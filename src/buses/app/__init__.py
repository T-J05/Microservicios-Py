
from flask import Blueprint, jsonify, request,Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Crear una instancia de la clase SQLAlchemy
db = SQLAlchemy()

def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar configuraciones desde config.py
    
    # Inicializar la extensión SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Importar modelos para registrar las tablas
    with app.app_context():
        
        from .models.buses_models import Buses
        from .models.itinerario_models import Itinerarios
        db.create_all()  # Crear las tablas en la base de datos

    # Importar y registrar el blueprint de rutas
    from .rutas.buses_routes import main
    app.register_blueprint(main)

    
    return app