
from app import db

class Itinerarios(db.Model):
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    inicio = db.Column(db.String,nullable=False)
    fin = db.Column(db.String,nullable=False )
    parada1 = db.Column(db.String ,nullable=False)
    parada2 = db.Column(db.String ,nullable=False)
    parada3 = db.Column(db.String ,nullable=False)
    def __repr__(self):
        return (f"<Itinerario(id={self.id}, inicio='{self.inicio}', "
                f"fin='{self.fin}', parada1='{self.parada1}', "
                f"parada2='{self.parada2}', parada3='{self.parada3}')>")

    
