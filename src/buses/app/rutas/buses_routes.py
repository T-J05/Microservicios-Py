from flask import Blueprint, jsonify, request
from ..servicios.bus_service import Colectivo
from ..servicios.common import tt, publicar_evento
import asyncio

colectivo = Colectivo
# Crear un blueprint para las rutas
main = Blueprint('main', __name__)



@main.get("/")
@tt.enviar_token
def inicioo():
    evento = {"tipo":"prueba",
              "estado":"good"}
    asyncio.run(publicar_evento(evento))
    return jsonify(colectivo.inicio())


@main.route("/crear_bus",methods=['PUT'])
@tt.enviar_token
def crear_bus():
    try:
        bus = request.get_json()
        evento = {"tipo":"crear_bus",
                  "estado":"good",
                  "dato":bus}
        asyncio.run(publicar_evento(evento))
        return  colectivo.crear_bus(bus)
    except Exception as e:
        evento = {"tipo":"crear_bus",
                "estado":f"Error: {str(e)}",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(f'error r {e} demonos')
    

@main.route("/ver_bus",methods=['POST',"GET"])
@tt.enviar_token
def ver_bus():
    try:
        data = request.get_json()
        datachapa = data['chapa']
        bus = colectivo.bus_ver(datachapa)
        evento = {"tipo":"ver_bus",
                "estado":"good",
                "dato":bus}
        asyncio.run(publicar_evento(evento))
        return colectivo.bus_ver(datachapa)
    except Exception as e:
        evento = {"tipo":"ver_bus",
                "estado":f"Error: {str(e)}",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(f'Error {e}')
    
@main.route("/ver_todo",methods = ["GET"])
@tt.enviar_token
def ver_todo ():
    try:
        evento = {"tipo":"ver_todo",
                "estado":"good",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(colectivo.ver_todo())
    except Exception as e:
        evento = {"tipo":"ver_todo",
                "estado":f"Error: {str(e)}",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(f"Error de: {e}")
    
    
@main.route("/editar_bus",methods=['PATCH'])
@tt.enviar_token
def editar_bus():
    try:
        data = request.get_json()
        colectivo.editar_bus(data)
        evento = {"tipo":"editar_bus",
                "estado":"good",
                }
        asyncio.run(publicar_evento(evento))
        return colectivo.editar_bus(data)
    except Exception as e:
        evento = {"tipo":"editar_bus",
                "estado":f"Error: {str(e)}",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(f'Error {e}')


@main.route("/eliminar_bus",methods=["DELETE"])
@tt.enviar_token
def eliminar_bus():
    try:
        data = request.get_json()
        if data:
            evento = {"tipo":"eliminar",
                     "estado":"good",
                }
            asyncio.run(publicar_evento(evento))
            return colectivo.delete_bus(data)
        else:
            return jsonify(f"Mensaje vacio capo")
    except Exception as e:
        evento = {"tipo":"ver_todo",
                "estado":f"Error: {str(e)}",
                }
        asyncio.run(publicar_evento(evento))
        return jsonify(f"Errorr de: {e}")
           
