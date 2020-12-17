from flask import Flask,render_template,url_for

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    #return "Hello"
    return render_template("index.html")

@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/recuperar",methods=['GET', 'POST'])
def recuperar():
    return render_template("recuperar.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)


