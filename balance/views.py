from flask import render_template, request
from . import app
from. forms import ComprasForm
from .models import DBManager

RUTA = 'balance/data/balance.db'

@app.route('/')
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL(" SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)

@app.route('/purchase', methods=["GET", "POST"])
def compra():
    if request.method == "GET":
        formulario = ComprasForm()
        return render_template("form_compra.html", form=formulario)

@app.route('/status', methods=["GET", "POST"])
def estado():
    return render_template("status.html")
