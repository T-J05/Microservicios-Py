from ..repositorios.bus_repo import Busclass
from ..models.buses_models import Buses

buss = Busclass #funciones directas con la base de datos
class Colectivo:

    def inicio():
        
        saludo = buss.saludar()
        return saludo


    def crear_bus(bus):
        if buss.obtener_por_chapa(bus["chapa"]):
            return f'El bus ya existe'
        linea = bus.get('linea')
        estado = bus.get('estado')
        chapa = bus.get('chapa')

        # Crear una nueva instancia de Buses
        nuevo_bus = Buses()

        # Asignar valores a los atributos directamente
        nuevo_bus.linea = linea
        nuevo_bus.estado = estado
        nuevo_bus.chapa = chapa
        
        return buss.agregar_bus(nuevo_bus)
    
    
    def bus_ver(chapa):
        if not buss.obtener_por_chapa(chapa):
            return f'El bus no existe'
        bus = buss.obtener_por_chapa(chapa)
        return(f'Bus: {bus}')
        
    def editar_bus(bus):
        if not buss.obtener_por_chapa(bus['chapa']):
            return f'El bus no existe'
        busx = buss.obtener_por_chapa(bus['chapa'])
        linea = busx.get('linea')
        estado = busx.get('estado')
        

        # Crear una nueva instancia de Buses
        nuevo_bus = Buses()

        # Asignar valores a los atributos directamente
        nuevo_bus.linea = linea
        nuevo_bus.estado = estado
        return buss.editar(nuevo_bus)
        
        
        
        
        