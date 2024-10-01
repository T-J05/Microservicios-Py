from ..repositorios.bus_repo import Busclass
from ..models.buses_models import Buses

buss = Busclass #funciones directas con la base de datos
class Colectivo:
    def inicio():
        
        saludo = buss.saludar()
        return saludo
    
    def verficar_vacio(data): 
        campos_requeridos = ['linea', 'estado', 'chapa']
        for campo in campos_requeridos:
             if campo not in data or not data[campo]:
               print(f"Error: El campo '{campo}' es requerido y no puede estar vacío.")
             return False
        return True


    def crear_bus(bus):
        campos_requeridos = ['linea', 'estado','chapa']
        for campo in campos_requeridos:
             if campo not in bus or not bus[campo]:
               return f"Error: El campo '{campo}' es requerido y no puede estar vacío.",400
             
        chapa = buss.obtener_por_chapa(bus["chapa"])
        
        
        if chapa:
                return f'El bus ya existe' ,404 
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
            
        busx = buss.obtener_por_chapa(bus['chapa'])
        if not busx:
            return f'El bus no existe'

        
        busx.linea = bus.get('linea', busx.linea)  
        busx.estado = bus.get('estado', busx.estado)

           
        busx.linea = bus.get('linea', busx.linea)  
        busx.estado = bus.get('estado', busx.estado)  

        return buss.editar(busx)
    
    def delete_bus(Bus):
        bus = buss.obtener_por_chapa(Bus["chapa"])
        if bus:
            try:
                buss.eliminar_bus(bus)
                return f"bus {bus} ha muerto" 
            except Exception as e:
                return f"ndi error de {e}"
        
        
        