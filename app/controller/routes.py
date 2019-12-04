from flask import render_template, redirect, url_for
from app import app, db
from app.forms import HTMLIngresoForm
from app.models import Guia, Criterio
import requests
from bs4 import BeautifulSoup
from app.controller.parsers.ParseoHelper import ParseoHelper
from app.controller.verificacion.validacionTextoAlternativo import validacionTextoAlternativo
from app.controller.verificacion.validacionInputName import validacionInputName
from app.controller.verificacion.validacionAlternativasMultimedia import validacionAlternativasMultimedia
from app.controller.reglas import WCAGReglas


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    resultados = list()
    form = HTMLIngresoForm()

    if form.validate_on_submit():
        respuesta = requests.get(form.contenidoHTML.data)
        form.contenidoHTML.data=''
        # Parsear HTML y guardar como Objeto BeautifulSoup
        contenidoHTML = BeautifulSoup(respuesta.text, "html.parser")

        # Criterio 1.1- Falta texto alternativo
            #Parsea elementos
        elementos = ParseoHelper.ObtenerElementos(contenidoHTML, WCAGReglas.dictWCAG2A_1_ReglasChecks["1.1.1"][2])
            #Verifico regla y guardo el resultado
        resultado_parcial = validacionTextoAlternativo.Verificar(elementos, "1.1.1", WCAGReglas.dictWCAG2A_1_ReglasChecks)
            #Agrego resultado a la lista de fallas
        resultados.append(resultado_parcial)

        # Criterio 1.1- Los inputs deben tener un nombre que describa su propósito
            #Parsea elementos
        elementos = ParseoHelper.ObtenerElementos(contenidoHTML, WCAGReglas.dictWCAG2A_1_ReglasChecks["1.1.2"][2])
            #Verifico regla y guardo el resultado
        resultado_parcial = validacionInputName.Verificar(elementos, "1.1.2", WCAGReglas.dictWCAG2A_1_ReglasChecks)
            #Agrego resultado a la lista de fallas
        resultados.append(resultado_parcial)

        # Criterio 1.2- Identificar elementos multimedia para validacion manual
            #Parsea elementos
        elementos = ParseoHelper.ObtenerElementos(contenidoHTML, WCAGReglas.dictWCAG2A_1_ReglasChecks["1.2"][2])
            #Verifico regla y guardo el resultado
        resultado_parcial = validacionAlternativasMultimedia.Verificar(elementos, "1.2", WCAGReglas.dictWCAG2A_1_ReglasChecks)
            #Agrego resultado a la lista de fallas
        resultados.append(resultado_parcial)



    return render_template('index.html', title='Inicio', form=form,resultados=resultados)
