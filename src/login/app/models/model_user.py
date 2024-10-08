
from .. import db



class Users(db.Model):
   
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    contraseña = db.Column(db.String,nullable=False)
    username = db.Column(db.String(60),unique=True,nullable=False)
    
    
    def __repr__(self):
        return (f"<User(id={self.id},contraseña={self.contraseña},"f"username={self.username})>")
    

    def to_dict(self):
        return {
            'id': self.id,
            'contraseña': self.contraseña,
            'username': self.username
        }