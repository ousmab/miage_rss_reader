


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
    es = db.Column(db.DateTime)
    