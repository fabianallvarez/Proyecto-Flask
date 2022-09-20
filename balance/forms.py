from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import DecimalField, HiddenField, SubmitField, SelectField
from . import MONEDAS
from wtforms.validators import DataRequired
from .models import DBManager
from . import RUTA

class ComprasForm(FlaskForm):
    Id = HiddenField()
    Desde = SelectField(
        u"Desde", choices=MONEDAS,validators=[
            DataRequired (message="Inserta Moneda")]
    )
    Cantidad = DecimalField("Cantidad", places=2)
    Hacia = SelectField(
        u"Hacia", choices=MONEDAS,validators=[
            DataRequired (message="Inserta Moneda")])

    consulta_api = SubmitField('Consulta')
    cancelar = SubmitField("Cancelar")
    guardar= SubmitField("Guardar")

def peticion_resultado(mon):
    db = DBManager(RUTA)
    consulta_Desde = 'SELECT SUM(cantidad_from) FROM movimientos WHERE moneda_from=? AND cantidad_from IS NOT NULL'
    consulta_Hacia = 'SELECT SUM(cantidad_to) FROM movimientos WHERE moneda_to=? AND cantidad_to IS NOT NULL'
    parametros = (mon,)
    gastado = db.peticionConParametros(consulta_Desde, parametros)
    comprado = db.peticionConParametros(consulta_Hacia, parametros)
    saldo = comprado - gastado
    return saldo, gastado

def formato_numero():
    pass