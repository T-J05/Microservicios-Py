# Importar la clase Bus y la base de datos
from ..models.buses_models import Buses
from app import db

class Busclass:
    def saludar ():
        
        return "hola"

    def obtener_por_chapa(chapa):
        bus_existe = Buses.query.filter_by(chapa=chapa).first()
        return bus_existe
        
    def obtener_todo():
        buses = Buses.query.all()
        return buses
    
    def agregar_bus(bus):
        
        db.session.add(bus)
        db.session.commit()
        return f"{bus} creado con exito"
        
    def eliminar_bus(chapa):
        db.session.delete(chapa)
        db.session.commit()
        return f'Bus: {chapa} fue eliminado'
    
    def editar(bus):
        db.session.commit()
        return f'Bus editado: {bus}'