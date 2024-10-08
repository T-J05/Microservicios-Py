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
       
        
        return user.iniciar_sesion(data_user)
    except Exception as e:
        return jsonify(f"Error (r,i) {e}")

    

@userblue.route("/registrar_user",methods=["POST"])
def registrarse():
    try:
        userr = request.get_json()
        registrado = user.registrar(userr)
        return  jsonify(registrado)
    except Exception as e:
        return jsonify(f"Error (r)  {e}")
    
@userblue.route("/verificar_token",methods=["POST"])
def verificar_jwt():
    try:
        token = request.authorization
        tokenverficado = tokenclass.verificar_token(token)
    except Exception as e:
        return jsonify(f"Error (v) {e}")