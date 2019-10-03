from flask import render_template
from app import app, db
from app.forms import HTMLIngresoForm
from app.models import Guia, Criterio


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = HTMLIngresoForm()
    return render_template('index.html', title='Inicio', form=form)
