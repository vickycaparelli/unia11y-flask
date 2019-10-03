from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired


class HTMLIngresoForm(FlaskForm):
    contenidoHTML = StringField('Contenido Html a Verificar', validators=[DataRequired()])
    boton_submit = SubmitField('Analizar')
