from flask import Flask,render_template,url_for,flash,redirect,request
from forms import FormularioLogin,FormularioRecuperar,FormularioNuevoUsuario,FormularioNuevoProducto,FormularioActualizarAdmin
from db import *

app = Flask(__name__)
app.config.update(SECRET_KEY="la_llave")

@app.route("/",methods=['GET', 'POST'])
@app.route("/index",methods=['GET', 'POST'])
def index():
    form = FormularioLogin()
    if form.validate_on_submit():
        return redirect("/home")
    return render_template("index.html",form=form)

@app.route("/home",methods=['GET', 'POST'])
def home():
    usuario=FormularioNuevoUsuario()
    producto=FormularioNuevoProducto()
    actualizar=FormularioActualizarAdmin()
    productos = get_productos()
    if request.method=="POST":
        if usuario.enviar.data and usuario.validate():
            return redirect("/home")
        if producto.enviar2.data and producto.validate():
<<<<<<< HEAD
            insertar_producto(producto.referencia.data,producto.producto.data,producto.precio.data,producto.cantidad.data,'Activo',producto.imagen.data)
=======
            #insertar_producto(producto.referencia,producto.producto,producto.precio,producto.cantidad,'ACTIVO',producto.imagen)
            #flash("producto creado")
>>>>>>> 70d5fb34cf9a1e8d1e636c51ee4e7cd6cec07aec
            return redirect('/home')
        if actualizar.enviar3.data and actualizar.validate():
            return redirect('/home')
    return render_template("home.html",form=usuario,form2=producto,form3=actualizar,productos = productos)

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    form=FormularioRecuperar()
    if form.validate_on_submit():
        # Quisiera colocarle al usuario un timed pop up en la parte inferior izquierda diciendole que ya se le envio el correo
        return redirect("/")
    return render_template("recuperar.html",form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


