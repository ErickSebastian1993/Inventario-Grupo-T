from flask import Flask,render_template,url_for,flash,redirect,request
from forms import FormularioLogin,FormularioRecuperar,FormularioNuevoUsuario

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
    if request.method=="POST":
        if usuario.validate():
            return redirect("/home")
        else:
            return render_template("home.html",form=usuario)
    else:
        return render_template("home.html",form=usuario)

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    form=FormularioRecuperar()
    if form.validate_on_submit():
        # Quisiera colocarle al usuario un timed pop up en la parte inferior izquierda diciendole que ya se le envio el correo
        return redirect("/")
    return render_template("recuperar.html",form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


