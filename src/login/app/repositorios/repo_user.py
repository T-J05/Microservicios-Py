# Importar la clase Bus y la base de datos
from ..models.model_user import Users
from .. import db

class Userclass:
     def obtener_username(username):
        user = Users.query.filter_by(username=username).first()
        return user
        
        
     def obtener_todo():
        users = Users.query.all()
        return users
    
    
     def agregar_user(user):
        db.session.add(user)
        db.session.commit()
        return f"{user}registrado con exito"
     
     
     def iniciar_sesion(username):
        user = Users.query.filter_by(username=username)
        return user