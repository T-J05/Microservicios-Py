
from app import db

class Itinerario(db.Model):
    __tablename__ = 'itinerarios'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    inicio = db.Column(db.String,nullable=False)
    fin = db.Column(db.String,nullable=False )
    parada1 = db.Column(db.String ,nullable=False)
    parada2 = db.Column(db.String ,nullable=False)
    parada3 = db.Column(db.String ,nullable=False)
    
    
