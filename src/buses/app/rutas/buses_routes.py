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



@main.route("/crear_bus",methods=['POST'])
def crear_bus():
    try:
        bus = request.get_json()
        colectivo.crear_bus(bus)
        return f'{bus} creado con exito'
    except Exception as e:
        return jsonify(f'error {e} demonos')
    

@main.route("/ver_bus",methods=['POST'])
def ver_bus():
    try:
        data = request.get_json()
        datachapa = data['chapa']
        return colectivo.bus_ver(datachapa)
    except Exception as e:
        return jsonify(f'Error {e}')
    
@main.route("/editar_bus",methods=['POST'])



