from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,validators
from wtforms.fields.html5 import EmailField

class FormularioLogin(FlaskForm):
    user = StringField('Usuario', [validators.DataRequired(message="Por favor completa con el usuario")])
    password = PasswordField('Contraseña', [validators.DataRequired(message='Por favor completa con la contraseña')])
    enviar = SubmitField('Iniciar Sesión')

class FormularioRecuperar(FlaskForm):
    correo=EmailField('Correo',[validators.DataRequired(message="Por favor completa con el correo"),validators.Email(message="Direccion de correo no valida")])
    enviar=SubmitField('Recuperar contraseña')