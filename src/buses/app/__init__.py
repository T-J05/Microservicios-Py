
from flask import Flask
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
        
        from .models.buses_models import Bus
        from .  models.itinerario_models import Itinerario
        db.create_all()  # Crear las tablas en la base de datos

    # Aquí puedes registrar blueprintsflask_sqlalchemy
    # from .routes import main
    # app.register_blueprint(main)

    return app