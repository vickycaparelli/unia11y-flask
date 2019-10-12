from flask import render_template, redirect, url_for
from app import app, db
from app.forms import HTMLIngresoForm
from app.models import Guia, Criterio
import requests
from bs4 import BeautifulSoup
from app.controller.parsers.ParseoHelper import ParseoHelper
from app.controller.verificacion.VerificacionCriterio01 import VerificacionCriterio01
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

        # Criterio 1- Controlo textos alternativos para elementos que no sean de tipo texto

        for regla in WCAGReglas.dictWCAG2A_1:
            #Parsea elementos
            elementos = ParseoHelper.ObtenerElementos(contenidoHTML, WCAGReglas.dictWCAG2A_1[regla][1])

            #Verifico regla y guardo el resultado
            resultado_parcial = VerificacionCriterio01.Verificar(elementos, regla, WCAGReglas.dictWCAG2A_1)

            #Agrego resultado a la lista de fallas
            resultados.append(resultado_parcial)
    return render_template('index.html', title='Inicio', form=form,resultados=resultados)
