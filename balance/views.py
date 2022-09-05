from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route('/')
def home():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/purchase')
def compra():
    return "Realiza una compra"


@app.route('/status')
def estado():
    return "Estado de movimiento"
