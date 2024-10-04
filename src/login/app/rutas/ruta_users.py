from flask import Blueprint, jsonify, request,redirect,url_for
from ..servicios.user_servicio import Userservice
from ..servicios.auth_servicio import Token
tokenclass = Token
user = Userservice #proviene del servicio
# Crear un blueprint para las rutas
userblue= Blueprint('user', __name__)

@userblue.get("/")
def inicioo():
    return jsonify(user.inicio())

@userblue.route("/generar_token",methods= "GET")
def generar_token ():
    try:
        
        
        
    except Exception as e:
        return jsonify(f"")
    
    
@userblue.route("/iniciar_sesion",methods= "POST")
def iniciar_sesion():
    try:
        data_user = request.get_json()
        userr= user.iniciar_sesion(data_user)
        return jsonify(f"{data_user["username"]} bienvenido"),redirect(url_for('generar_token'))
    except Exception as e:
        return jsonify(f"Error {e}")

    

@userblue.route("/registrar_user",methods="POST")
def registrarse():
    try:
        userr = request.get_json()
        registrado = user.registrar(userr)
        if registrado:
            return redirect(url_for("iniciar_sesion"))
    except Exception as e:
        return jsonify(f"Error (r)  {e}")