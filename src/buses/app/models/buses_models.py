
from app import db



class Buses(db.Model):
   
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    linea = db.Column(db.String,nullable=False)
    estado = db.Column(db.String,nullable=False )
    chapa = db.Column(db.String ,unique=True,nullable=False)
    
    
    def __repr__(self):
        return (f"<Bus(id={self.id}, linea='{self.linea}', "
                f"estado='{self.estado}', chapa='{self.chapa}')>")
    

    def to_dict(self):
        return {
            'id': self.id,
            'linea': self.linea,
            'estado': self.estado,
            'chapa': self.chapa
        }