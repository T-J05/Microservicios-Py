from flask import Blueprint, jsonify, request
from ..servicios.bus_service import Colectivo

colectivo = Colectivo
# Crear un blueprint para las rutas
main = Blueprint('main', __name__)



@main.get("/")
def inicioo():
    return colectivo.inicio()



@main.route("/crear_bus",methods=['PUT'])
def crear_bus():
    try:
        bus = request.get_json()
        print(bus)
        return  colectivo.crear_bus(bus)
    except Exception as e:
        return jsonify(f'error r {e} demonos')
    

@main.route("/ver_bus",methods=['POST',"GET"])
def ver_bus():
    try:
        data = request.get_json()
        datachapa = data['chapa']
        return colectivo.bus_ver(datachapa)
    except Exception as e:
        return jsonify(f'Error {e}')
    
@main.route("/ver_todo",methods = ["GET"])
def ver_todo ():
    try:
        return jsonify(colectivo.ver_todo())
    except Exception as e:
        return jsonify(f"Error de: {e}")
    
    
@main.route("/editar_bus",methods=['PATCH'])
def editar_bus():
    try:
        data = request.get_json()
        colectivo.editar_bus(data)
        return colectivo.editar_bus(data)
    except Exception as e:
        return jsonify(f'Error {e}')


@main.route("/eliminar_bus",methods=["DELETE"])
def eliminar_bus():
    try:
        data = request.get_json()
        if data:
            return colectivo.delete_bus(data)
        else:
            return f"Mensaje vacio capo"
    except Exception as e:
        return f"Errorr de: {e}"
           