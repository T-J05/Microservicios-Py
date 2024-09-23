
from app import db



class Bus(db.Model):
    __tablename__ = 'buses'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    linea = db.Column(db.String,nullable=False)
    estado = db.Column(db.String,nullable=False )
    chapa = db.Column(db.String ,unique=True)
    
    
