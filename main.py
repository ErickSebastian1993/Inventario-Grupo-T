from flask import Flask,render_template,url_for,flash,redirect
from forms import FormularioLogin

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
    return render_template("home.html")

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    return render_template("recuperar.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


