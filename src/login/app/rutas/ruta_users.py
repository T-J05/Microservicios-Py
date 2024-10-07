from flask import Blueprint, jsonify, request,redirect,url_for
from ..servicios.user_servicio import Userservice
from  ..servicios.auth_servicio import Token


tokenclass = Token
user = Userservice #proviene del servicio
# Crear un blueprint para las rutas
userblue= Blueprint('user', __name__)

@userblue.get("/")
def inicioo():
    return jsonify(user.inicio())

    
    
@userblue.route("/iniciar_sesion",methods= ["POST"])
def iniciar_sesion():
    try:
        data_user = request.get_json()
        if user.iniciar_sesion(data_user):
            token = user.iniciar_sesion(data_user)
            print(token)
            return jsonify(f"{data_user["username"]} bienvenido,{token} ")
    except Exception as e:
        return jsonify(f"Error {e}")

    

@userblue.route("/registrar_user",methods=["POST"])
def registrarse():
    try:
        userr = request.get_json()
        registrado = user.registrar(userr)
        return  jsonify(registrado)
    except Exception as e:
        return jsonify(f"Error (r)  {e}")