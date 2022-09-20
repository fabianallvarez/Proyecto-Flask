from datetime import date, datetime, time
from flask import flash,redirect,url_for, render_template, request
from . import app
from. forms import ComprasForm, peticion_resultado
from .models import CriptoModel, DBManager
from . import RUTA

@app.route('/')
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL(" SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)

@app.route('/purchase', methods=["GET", "POST"])
def purchase():
    if request.method == "GET":
        formulario = ComprasForm()
        return render_template("form_compra.html", form=formulario)

    elif request.method == "POST":
        form = ComprasForm(data=request.form)
        Desde = form.Desde.data
        Hacia = form.Hacia.data
        cripto_cambio = CriptoModel()
    
    if not form.validate():
        return render_template("form_compra.html", form = form, id = id, error=["Validacion incorrecta"])

    if Desde == Hacia:
        flash('Desde y Hacia deben ser distintos')
        return redirect(url_for('purchase'))
    db = DBManager(RUTA)
    cripto_cambio.moneda_origen = Desde
    cripto_cambio.moneda_destino = Hacia
    cantidad_Desde = form.Cantidad.data
    cantidad_Desde = float(cantidad_Desde)
    cambio = cripto_cambio.consultar_cambio()
    print(cambio)
    print(type(cantidad_Desde))
    cantidad_Hacia = cantidad_Desde * cambio
    resto = peticion_resultado(Desde)

    if Desde == 'EUR':
        resto = float('inf')
    
    if resto < cantidad_Desde:
        flash('Saldo Insuficiente')
        return redirect(url_for('/purchase'))

    if form.consulta_api.data:
            form.Desde.render_kw = {'readonly':True}
            return render_template('form_compra.html', form = form,
                cantidad_to = round(cantidad_Desde,5),
                precio_unitario = round(cambio,5))

    elif form.cancelar.data:
            return redirect(url_for('purchase'))

    elif form.guardar.data:
            fecha = date.today().isoformat()
            hora = time(
                datetime.now().hour,
                datetime.now().minute,
                datetime.now().second)
            consulta = 'INSERT INTO movimientos(Fecha, Hora, Desde, cantidad_Desde, Hacia, cantidad_Hacia) VALUES (?, ?, ?, ?, ?, ?)'
            params = (
                fecha,
                str(hora),
                Desde,
                cantidad_Desde,
                Hacia,
                cantidad_Hacia)   
            resultado = db.consultaConParametros(consulta, params)




@app.route('/status', methods=["GET", "POST"])
def estado():
    return render_template("status.html")
