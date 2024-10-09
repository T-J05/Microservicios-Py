from flask import jsonify, request
from functools import wraps
import requests  
from circuitbreaker import circuit 
from tenacity import retry, stop_after_attempt, wait_fixed 
url = "http://localhost:5001/verificar_token"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def hacer_solicitud(token):
        headers = {'Authorization': token}
        respuesta = requests.post(url, headers=headers)
        return respuesta
    
    
class tt:
        
    @circuit(failure_threshold=5, recovery_timeout=30,)
    @staticmethod
    def enviar_token(funcion):
        @wraps(funcion)
        def decorador(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                encabezado = request.headers['Authorization']
        
                token = encabezado.split(" ")[1] if len(encabezado.split(" ")) > 1 else None

            if not token:
                return jsonify({'error': 'Token no encontrado'}), 403
            try:
                respuesta = hacer_solicitud(token)
                if respuesta.status_code == 200:
                    return funcion(*args, **kwargs)
                else:
                    return jsonify({'error': 'Token inválido o no autorizado'}), respuesta.status_code

            except Exception as e:
                return jsonify({'error': f"Error en la verificación del token: {str(e)}"}), 500

        return decorador
