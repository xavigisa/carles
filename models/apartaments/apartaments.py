from google.appengine.ext import db

class Apartament(db.Model):
    nom = db.StringProperty()
    disponible = db.BooleanProperty()
    localitzacio = db.GeoPtProperty()
    descripcio = db.TextProperty()

class Fotos(db.Model):
    nom = db.ReferenceProperty(Apartament)
    foto = db.BlobProperty()
    descripcio = db.TextProperty()
    
    
########## Exemple #################
#a = Apartament(nom="Apartament 1",disponible=True,
#localitzacio= db.GeoPt(-44.22, -33.55),
#descripcio= "HOLA HOLA")
#a.put()
###################################