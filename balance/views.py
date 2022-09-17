from flask import render_template, request
from . import app
from .models import DBManager

RUTA = 'balance/data/balance.db'

@app.route('/')
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL(" SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)

@app.route('/purchase/<int:id>', methods=["GET", "POST"])
def compra(id):
    if request.method == "GET":
        render_template("form_movimiento.html")
    return render_template("purchase.html")

@app.route('/status', methods=["GET", "POST"])
def estado(id):
    return render_template("status.html")
