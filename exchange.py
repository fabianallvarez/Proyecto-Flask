import locale
import requests

loc = locale.getlocale()
print

apikey = "10352093-DC90-44AE-A3C8-C01441A3AD7B"
cabeceras = {
    "X-CoinAPI-Key": apikey
    }

moneda_origen = input("¿Que moneda quieres cambiar?")
moneda_destino = input("¿Que moneda deseas obtener?")
url =f"https://rest-sandbox.coinapi.io/v1/exchangerate/{moneda_origen}/{moneda_destino}"
respuesta = requests.get(url, headers=cabeceras)
tipo_cambio = respuesta.json()

cambio = tipo_cambio["rate"]

print("Un {} vale como {:,.2f} {}".format(
    moneda_origen, cambio, moneda_destino,
))
 