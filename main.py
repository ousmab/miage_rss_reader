from flask import Flask, render_template, request,flash,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


""" 
CONFIGURATION DE L' APPLICATION 
--------------------------------------
"""

app.config["SECRET_KEY"]= "_5#sdem45@y2L"
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
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email'].strip()
        passw = request.form['password'].strip()

        if email and passw:
            user = Utilisateur.query.filter_by(email=email,mot_de_passe=passw).first()
            session['logged'] = True
            
            session['user_logged'] = user.id
            session['user_logged_name'] = user.surnom
            
            if user:
                return redirect(url_for('home') )
                
            else:
                flash(u'Vos identifiants sont incorrects !','error')
        else:
            flash(u'Vous devez saisir tous les champs !','error')

    return render_template("index.html")


@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if ( request.form['email'].strip() ) and ( request.form['username'].strip()) and ( request.form['password'].strip()) :
            print(session['user_logged'] )
            user = Utilisateur(user_id= int(session['user_logged']),email=request.form['email'].strip(),surnom=request.form['username'].strip(),mot_de_passe=request.form['password'].strip())
            db.session.add(user)
            db.session.commit()
            flash(u'Nous sommes heureux de vous compter parmis nous connectez-vous dès maintenant !','success')
            return redirect(url_for('index'))
        else:
            flash(u'Vous devez saisir tous les champs !','error')
    return render_template("register.html")

#---redirige vers la page d'accueil si connecte

@app.route("/home")
def home():

    if session['logged'] == True:

        flux_list = flux_information.query.all()     
        flux_list = flux_information.query.all()    
    
        url_publication = flux_information.query.get(5).url_publications

        url = requests.get(url_publication).text
        soup = BeautifulSoup(url,"lxml")

        publications = {}
        xml_pub = soup.find('channel').find_all('item',limit=3)
        list_publication = []
        for pub in xml_pub:
            pub_format = BeautifulSoup(str(pub),'lxml' )
            publication = {}
            publication["titre"] = checkValue(pub_format.find('title').text)
            publication["lien_publication"] = checkValue(str(pub_format.find('link').text) )
            publication["date_publication"] = checkValue(pub_format.find('pubDate'))
            publication["description"] = checkValue(pub_format.find('description').text)
            list_publication.append(publication)

    
        return render_template('home/home.html',flux_list=flux_list,list_publication=list_publication)

    else:
        return render_template("index.html")


def checkValue(str):
    if str:
        return str
    else:
        return ""


@app.route("/publication/<flux_id>")
def publication(flux_id):
    flux_list = flux_information.query.all()    
    
    url_publication = flux_information.query.get(flux_id).url_publications

    url = requests.get(url_publication).text
    soup = BeautifulSoup(url,"lxml")

    publications = {}
    xml_pub = soup.find('channel').find_all('item',limit=10)
    list_publication = []
    for pub in xml_pub:
        pub_format = BeautifulSoup(str(pub),'lxml' )
        publication = {}
        publication["titre"] = checkValue(pub_format.find('title').text)
        publication["lien_publication"] = checkValue(str(pub_format.find('link').text) )
        publication["date_publication"] = checkValue(pub_format.find('pubDate'))
        publication["description"] = checkValue(pub_format.find('description').text)
        list_publication.append(publication)

    
    return render_template('home/publication.html',flux_list=flux_list,list_publication=list_publication)

@app.route("/logout")
def logout():
    session['logged'] = False
    session['user_logged'] = None
    session['user_logged_name'] = None
    return redirect(url_for('index') )     


@app.route("/new",methods=['GET','POST'])
def add_flux():
    flux_list = flux_information.query.all()  
    
    if request.method == 'POST':
        if ( request.form['url'].strip() ) and ( request.form['adresse_site'].strip()):
            flux = flux_information(adresse_site_web= request.form['adresse_site'].strip(),url_publications=request.form['url'].strip() )
            created = db.session.add(flux)
            
            db.session.commit()
            flash(u'Votre flux a été ajouté !','success')
        else:
            flash(u'Vous devez saisir tous les champs !','error')
    return render_template('home/add_flux.html',flux_list=flux_list)

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
    #amis = db.relationship('amitie',backref='utilisateur_id',lazy=True) # les amis de la personne
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
    titre = db.Column(db.String(100) )
    description = db.Column(db.Text )
    adresse_site_web = db.Column(db.String(255) )
    url_publications = db.Column(db.String(255) )
    langue = db.Column(db.String(8) )
    created_at = db.Column(db.DateTime )
    updated_at = db.Column(db.DateTime)
    publications = db.relationship('publication',backref='flux_information', lazy=True)
    user_id=db.Column(db.Integer) #pour des besoins de presentation juste
    
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