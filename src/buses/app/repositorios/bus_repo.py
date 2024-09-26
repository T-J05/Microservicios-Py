# Importar la clase Bus y la base de datos
from ..models.buses_models import Buses
from app import db

class Busclass:
    def saludar ():
        
        return "hola"

    def verificar_existe(self,chapa):
        bus_existe = Buses.query.filter_by(chapa=chapa).first()
        if bus_existe:
                return bus_existe


    def obtener_por_chapa(self,chapa):
        bus = self.verificar_existe(chapa)
        if bus:
            return bus
        else:
            return("Bus no encontrado")
        
        
    def agregar_bus(self,linea,estado,chapa):
        existe = self.verificar_existe(chapa)
        if existe:
            return f"El bus con chapa ya {existe} ya existe"
        else: 
            bus = Buses(linea=linea,estado=estado,chapa=chapa)
            db.session.add(bus)
            db.session.commit()
            return f"{bus} creado con exito"
        
        
    def editar_por_chapa(self,nueva_linea,estado_nuevo,chapa):
        bus = self.verificar_existe(chapa)
        if bus:
            if nueva_linea is not None:
                bus.linea = nueva_linea
            if estado_nuevo is not None:
                bus.estado = estado_nuevo

            db.session.commit()
            return bus
