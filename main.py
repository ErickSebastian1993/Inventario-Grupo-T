from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    return render_template("recuperar.html")