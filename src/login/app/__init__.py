
from flask import Blueprint, jsonify, request,Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Crear una instancia de la clase SQLAlchemy
db = SQLAlchemy()

def ccrear_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Cargar configuraciones desde config.py
    
    # Inicializar la extensión SQLAlchemy con la aplicación
    db.init_app(app)
    
    # Importar modelos para registrar las tablas
    with app.app_context():
        
        from app.models.model_user import Users
        db.create_all()  # Crear las tablas en la base de datos

    # Importar y registrar el blueprint de rutas
    from app.rutas.ruta_users import userblue
    app.register_blueprint(userblue)
    
    return app