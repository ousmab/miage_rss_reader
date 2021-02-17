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


@app.route("/register")
def register():
    return render_template("register.html")

#---redirige vers la page d'accueil si connecte
@app.route("/home")
def home():
    return render_template("home/home.html")





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
    amis = db.relationship('amitie',backref='utilisateur',lazy=True) # les amis de la personne
    souscriptions = db.relationship('souscription',backref='utilisateur',lazy=True) # les flux de la personne
    

class amitie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_demande = db.Column(db.DateTime )
    statut = db.Column(db.Boolean)
    destinataire_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id') ) #FK
    utilisateur_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id') )#FK
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)


class flux_information(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100) ,nullable=False)
    description = db.Column(db.Text )
    adresse_site_web = db.Column(db.String(255) )
    url_publications = db.Column(db.String(255) )
    langue = db.Column(db.String(8) )
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    publications = db.relationship('publication',backref='flux_information', lazy=True)

class publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(100) ,nullable=False)
    lien_publication = db.Column(db.String(255) )
    date_timestamp = db.Column(db.DateTime)
    date_publication = db.Column(db.DateTime)
    description = db.Column(db.Text )
    flux_id = db.Column(db.Integer,db.ForeignKey('flux_information.id') ) # FK
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    

class souscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_souscription = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    utilisateur_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id'))#FK utilisateur
    flux_id = db.Column(db.Integer,db.ForeignKey('flux_information.id')) # FK flux



class lecture_publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_lecture = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    utilisateur_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id'))#FK utilisateur
    publication_id = db.Column(db.Integer,db.ForeignKey('publication.id')) # FK publication
    


class partage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_partage = db.Column(db.DateTime)
    commentaire = db.Column(db.Text )
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    utilisateur_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id'))#FK utilisateur
    publication_id = db.Column(db.Integer,db.ForeignKey('publication.id')) # FK publication


class commentaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_commentaire = db.Column(db.DateTime)
    commentaire = db.Column(db.Text )
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    utilisateur_id = db.Column(db.Integer,db.ForeignKey('utilisateur.id'))#FK utilisateur
    publication_id = db.Column(db.Integer,db.ForeignKey('publication.id')) # FK publication





""" 
LANCEMENT DE L'APPLICATION
--------------------------------------
"""
app.run(port=5000,host="localhost",debug=True)