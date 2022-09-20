# Proyecto-Flask
Proyecto final de Keepcoding

# Instrucciones de Instalacion
--- Abrir el Terminal
--- Abrir El entorno Virtual 
--- Executar : flask run
--- Dar clik en el viculo 



if Desde == Hacia:
        flash('Desde y Hacia deben ser distintos')
        return redirect(url_for('purchase'))

    db = DBManager(RUTA)
    cripto_cambio.moneda_origen = Desde
    cripto_cambio.moneda_destino = Hacia
    Cantidad_Desde = form.Cantidad.data
    cambio = cripto_cambio.consultar_cambio()
    Cantidad_hacia = Cantidad_Desde * cambio