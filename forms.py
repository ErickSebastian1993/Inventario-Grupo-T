from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,validators
from wtforms.validators import DataRequired

class FormularioLogin(FlaskForm):
    user = StringField('Usuario', [validators.DataRequired(message="Por favor completa con el usuario")])
    password = PasswordField('Contraseña', [validators.DataRequired(message='Por favor completa con la contraseña')])
    enviar = SubmitField('Iniciar Sesión')