from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, HiddenField, RadioField, StringField, SubmitField


class ComprasForm(FlaskForm):
    Fecha = DateField("Fecha")
    Hora = DateField("Hora")
    Desde = StringField("Desde")
    Cantidad = DecimalField("Cantidad", places=2)
    Hacia = StringField("Hacia")
    C = DecimalField("C", places=2)
    PU = DecimalField("PU", places=2)

    cancelar = SubmitField("Cancelar")
    guardar= SubmitField("Guardar")