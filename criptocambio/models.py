import requests
from . import APIKEY

class APIError(Exception):
    pass

class CriptoModel:

    def __init__(self):
        self.moneda_origen = ""
        self.moneda_destino = ""
        self.cambio = 0.0

    def consultar_cambio(self):
        cabeceras = {
            "X-CoinAPI-Key": APIKEY
        }
        url =f"https://rest-sandbox.coinapi.io/v1/exchangerate/{self.moneda_origen}/{self.moneda_destino}"
        respuesta = requests.get(url, headers=cabeceras)

        if respuesta.status_code == 200:
            self.cambio = respuesta.json()["rate"]
        else:
            raise APIError(
                "Ha ocurrido un error {} {} al consultar la API".format(
                    respuesta.status_code, respuesta.reason
                    )
                )
    pass