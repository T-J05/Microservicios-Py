from ..repositorios.bus_repo import Busclass
bus = Busclass
class Colectivo:
    def inicio():
        saludo = bus.saludar()

        return saludo


# def crear_bus(linea,estado,chapa):
#     agregar()