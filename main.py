from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


""" 
CONFIGURATION DE L' APPLICATION 
--------------------------------------
"""

#--- app.config["SQLALCHEMY_DATABASE_URI"] =  mysql://username:password@server/db

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://odoo:odoo@localhost:5432/agregateur_rss' 
db = SQLAlchemy(app)
migrate = Migrate(app,db)


""" 
MODELS A REFACTORER
--------------------------------------
"""
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255) ,nullable=False)
    surnom = db.Column(db.String(80) )
    ville = db.Column(db.String(80) )
    pays = db.Column(db.String(80) )
    avatar = db.Column(db.String(80) )
    biographie = db.Column(db.String(80) )
    mot_de_passe = db.Column(db.String(80) )
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)



""" 
GESTION DES ERREURS 404
--------------------------------------
"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404    

""" 
ROUTAGES
--------------------------------------
"""

#---accueil du site
@app.route("/")
def index():
    return render_template("index.html")


#---redirige vers la page d'accueil si connecte
@app.route("/home")
def home():
    return render_template("home/home.html")



""" 
LANCEMENT DE L'APPLICATION
--------------------------------------
"""
app.run(port=5000,host="localhost",debug=True)