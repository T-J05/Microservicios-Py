
from .. import db



class Users(db.Model):
   
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    contraseña = db.Column(db.String,nullable=False)
    rol = db.Column(db.String(15),nullable=False)
    username = db.Column(db.String(60),unique=True,nullable=False)
    
    
    def __repr__(self):
        return (f"<User(id={self.id}, contraseña='{self.contraseña}', "
                f"rol='{self.rol}', username='{self.username}')>")
    

    def to_dict(self):
        return {
            'id': self.id,
            'contraseña': self.contraseña,
            'rol': self.rol,
            'username': self.username
        }