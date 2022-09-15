from flask import render_template
from . import app
from .models import DBManager

RUTA = 'balance/data/balance.db'

@app.route('/')
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL(" SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route('/purchase', methods=["GET", "POST"])
def compra():
    return render_template("purchase.html")


@app.route('/status', methods=["GET", "POST"])
def estado():
    return render_template("status.html")

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db = DBManager(RUTA)
    esta_borrado: db.borrar(id)
    return render_template("borrar.html", resultado=esta_borrado)