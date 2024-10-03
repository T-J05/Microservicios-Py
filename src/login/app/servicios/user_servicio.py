from ..repositorios.repo_user import Userclass
from ..models.model_user import Users




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
            userss.agregar_user()
        except Exception as e:
            return f"Error de  {e}"
    def 