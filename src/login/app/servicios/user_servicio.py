from ..repositorios.repo_user import Userclass
from ..models.model_user import Users
from ..servicios.auth_servicio import Token
tokenclass = Token



userss = Userclass #funciones directas con la base de datos


class Userservice:
    def inicio():
        
        saludo = "hola"
        return saludo
    
    
    def registrar(user):
        user_name = user["username"]
        try:
            if userss.obtener_username(user_name):
                return f"El usuario {user_name} ya existe"
            campos_requeridos = ['username', 'contraseña']
            for campo in campos_requeridos:
             if campo not in user or not user[campo]:
                return f"Error: El campo '{campo}' es requerido y no puede estar vacío.",400
            username = user.get('username')
            contraseña= user.get('contraseña')
            

            modelouser = Users(username=username,contraseña=contraseña)
            # Asignar valores a los atributos directamente
           
           
            userss.agregar_user(modelouser)
            
        except Exception as e:
            return f"Error de  {e}"
        
        
    def iniciar_sesion (user):
        try:
            user_a_verificar = userss.obtener_username(user["username"])
            contraseña = user_a_verificar["contraseña"]
            username = user_a_verificar["username"]
            if username:
                if user["contraseña"] == contraseña:
                    token = tokenclass.generar_token(user)
                    return token
                else:
                    return f"Contraseña incorrecta",None
            else: 
                return f"Username {username} no registrado o mal escrito",None
        except Exception as e:
            return f"Error (i) {e}"
    