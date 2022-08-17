from typing import ParamSpecArgs


class CriptoView:

    def __init__(self):
        pass

    def pedir_monedas(self):
        origen = input("¿Que moneda quieres cambiar?")
        destino = input("¿Que moneda deseas obtener?")
        return(origen, destino)

    def mostrar_cambios(self, origen, destino, cambio):
         print("Un {} vale como {:,.2f} {}".format(
    origen, cambio, destino,
    ))
