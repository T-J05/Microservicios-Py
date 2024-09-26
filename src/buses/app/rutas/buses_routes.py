from flask import Blueprint, jsonify, request
from ..models.buses_models import Buses
from ..models.itinerario_models import Itinerarios
from ..servicios.bus_service import Colectivo

from .. import db
colectivo = Colectivo
# Crear un blueprint para las rutas
main = Blueprint('main', __name__)



@main.get("/")
def inicioo():
    return colectivo.inicio()