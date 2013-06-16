from google.appengine.ext import db

class Apartament(db.Model):
    nom = db.StringProperty()
    descripcio = db.TextProperty()
    nom_es = db.StringProperty()
    descripcio_es = db.TextProperty()
    nom_en = db.StringProperty()
    descripcio_en = db.TextProperty()
    disponible = db.BooleanProperty()
    
    localitzacio = db.GeoPtProperty()
    
    preu = db.FloatProperty()
    
    def fotos(self):
        f = Fotos().all().filter('apartament =',self)
        return f
    

class Fotos(db.Model):
    apartament = db.ReferenceProperty(Apartament)
    foto = db.BlobProperty()
    descripcio = db.TextProperty()
    
    
########## Exemple #################
#a = Apartament(nom="Apartament 1",disponible=True,
#localitzacio= db.GeoPt(-44.22, -33.55),
#descripcio= "HOLA HOLA")
#a.put()
###################################