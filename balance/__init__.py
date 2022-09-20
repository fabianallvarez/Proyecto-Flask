from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()
MONEDAS = [("EUR" , "Euro"),
           ("BTC" , "Bitcoin"),
           ("ETH" , "Ethereum"),
           ("DOGE" , "DogeCoin")
           ]
RUTA = 'balance/data/balance.db'
