from flask import Flask,render_template,url_for,flash,redirect,request,session
from forms import FormularioLogin,FormularioRecuperar,FormularioNuevoUsuario,FormularioNuevoProducto,FormularioActualizarAdmin
from db import *
from flask_uploads import configure_uploads,IMAGES,UploadSet


app = Flask(__name__)
app.config.update(SECRET_KEY="la_llave")
app.config['UPLOADED_IMAGES_DEST']='static/img'

images=UploadSet('images',extensions=('jpg', 'jpe', 'jpeg', 'png'))
configure_uploads(app,images)

def esAdmin():
    return session.get("usuario").get("rol") == "Administrador"

def esVendor():
    return session.get("usuario").get("rol") == "Vendedor"

def usuarioLogeado():
    return session.get("usuario")

@app.route("/",methods=['GET', 'POST'])
@app.route("/index",methods=['GET', 'POST'])
def index():
    form = FormularioLogin()
        
    if form.validate_on_submit():
        user = validar_usuario(form.user.data)
        if user:
            validarContra = validar_password(user[0][2],user[0][3])
            if validarContra:
                session["usuario"] = {"nom_usuario":user[0][2],"rol":user[0][4]}
                return redirect(url_for("home"))
        else:
            flash("Usuario o Contraseña incorrectos.")
    return render_template("index.html",form=form)

@app.route("/home",methods=['GET', 'POST'])
def home():
    if not usuarioLogeado():
        return redirect("/index")

    usuario=FormularioNuevoUsuario()
    producto=FormularioNuevoProducto()
    actualizar=FormularioActualizarAdmin()
    productos = get_productos()

    if request.method=="POST":
        if usuario.enviar.data and usuario.validate():
            insertar_usuario(usuario.name.data,usuario.email.data,usuario.user.data,usuario.password.data,usuario.rol.data)
            return redirect("/home")
        if producto.enviar2.data and producto.validate():
            try:
                if producto.imagen.data.filename!='':
                    insertar_producto(producto.referencia.data,producto.producto.data,producto.precio.data,producto.cantidad.data,producto.estado.data,producto.imagen.data)
                    filename=images.save(producto.imagen.data)
            except:
                insertar_producto(producto.referencia.data,producto.producto.data,producto.precio.data,producto.cantidad.data,producto.estado.data,'noimage.jpg')

            return redirect('/home')
        if actualizar.enviar3.data and actualizar.validate():
            actualizar_producto(actualizar.referencia.data,actualizar.producto.data,actualizar.precio.data,actualizar.cantidad.data,actualizar.estado.data,actualizar.imagen.data)
            try:
                if actualizar.imagen.data == "":
                    filename=images.save(actualizar.imagen.data)
            except:
                pass
            return redirect('/home')
    return render_template("home.html",form=usuario,form2=producto,form3=actualizar,productos = productos)

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    form=FormularioRecuperar()
    if form.validate_on_submit():
        # Quisiera colocarle al usuario un timed pop up en la parte inferior izquierda diciendole que ya se le envio el correo
        return redirect("/")
    return render_template("recuperar.html",form=form)

@app.route("/cerrar",methods=['GET','POST'])
def cerrarSesion():
    session.pop("usuario")
    flash("Sesión Cerrada.")
    return redirect("/index")



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


