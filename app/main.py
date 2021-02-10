from flask import Flask, render_template

app = Flask(__name__)


#retourne la page d'accueil
@app.route("/")
def index():
    return render_template("index.html")

#redirige normalement a l'acceuil si l'utilisateur est connecté
@app.route("/home")
def home():
    return render_template("home/home.html")

app.run(port=5000,host="localhost",debug=True)