from flask import Blueprint, jsonify, request
from ..servicios.user_servicio import Userservice

user = Userservice #proviene del servicio
# Crear un blueprint para las rutas
userblue= Blueprint('user', __name__)

@userblue.get("/")
def inicioo():
    return jsonify(user.inicio())