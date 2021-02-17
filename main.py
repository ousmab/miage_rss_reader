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



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404    

app.run(port=5000,host="localhost",debug=True)