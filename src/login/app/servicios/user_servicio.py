from ..repositorios.repo_user import Userclass
from ..models.model_user import Users
from auth_servicio import Token
tokenclass = Token



userss = Userclass #funciones directas con la base de datos


class Userservice:
    def inicio():
        
        saludo = "hola"
        return saludo
    
    
    def registrar(user):
        username = user["username"]
        try:
            if userss.obtener_username(username):
                return f"El usuario {username} ya existe"
            if user["username"] and user["contraseña"]:
                userss.agregar_user()
            else:
                return f"F no pusiste todos los parametros"
        except Exception as e:
            return f"Error de  {e}"
        
        
    def iniciar_sesion (user):
        try:
            user_a_verificar = userss.iniciar_sesion(user["username"])
            contraseña = user_a_verificar["contraseña"]
            username = user_a_verificar["username"]
            if username:
                if user["contraseña"] == contraseña:
                    token = tokenclass.generar_token(user)
                    return token
                else:
                    return f"Contraseña incorrecta"
            else: 
                return f"Username {username} no registrado o mal escrito"
        except Exception as e:
            return f"Error (i) {e}"
    