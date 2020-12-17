from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,validators
from wtforms.fields.html5 import EmailField

class FormularioLogin(FlaskForm):
    user = StringField('Usuario', [validators.DataRequired(message="Por favor completa con el usuario")])
    password = PasswordField('Contraseña', [validators.DataRequired(message='Por favor completa con la contraseña')])
    enviar = SubmitField('Iniciar Sesión')

class FormularioRecuperar(FlaskForm):
    correo=EmailField('Correo',[validators.DataRequired(message="Por favor completa con el correo"),validators.Email(message="Correo no valido")])
    enviar=SubmitField('Recuperar contraseña')

class FormularioNuevoUsuario(FlaskForm):
    user = StringField('Usuario', [validators.DataRequired(message="Por favor completa con un usuario")])
    email= EmailField('Correo Electrónico',[validators.DataRequired(message="Por favor completa con un correo"),validators.Email(message="Correo no valido")])
    name= StringField('Nombre')
    password=PasswordField('Contraseña',[
        validators.DataRequired(message="Por favor completa con una contraseña"),
        validators.EqualTo('confirm',message="Contraseñas deben ser iguales"),
        validators.length(min=6,message="Longitud minima de 6 caracteres"),
        validators.regexp(regex=".*[A-Z]",message="Debe tener minimo una mayuscula"),
        validators.regexp(regex=".*[0-9]",message="Debe tener minimo un numero") 
    ])
    confirm=PasswordField('Confirmar contraseña')
    rol=SelectField('Rol',choices=[('Administrador','Administrador'),('Vendedor','Vendedor')])
    enviar=SubmitField('Registrar')
