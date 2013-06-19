from google.appengine.ext import db

class Apartament(db.Model):
    nom = db.StringProperty()
    descripcio = db.TextProperty()
    nom_es = db.StringProperty()
    descripcio_es = db.TextProperty()
    nom_en = db.StringProperty()
    descripcio_en = db.TextProperty()
    localitzacio = db.GeoPtProperty()
    adreca = db.StringProperty()
    fotos = db.ListProperty(db.Key)
 
    def llistat_fotos(self):
        f = Fotos().all().filter('__key__ in',self.fotos)
        return f
    

class Fotos(db.Model):
    foto = db.BlobProperty()
    descripcio = db.TextProperty()

class Habitatge(db.Model):
    nom = db.StringProperty()
    nom_es = db.StringProperty()
    nom_en = db.StringProperty()
    descripcio = db.TextProperty()
    descripcio_es = db.TextProperty()
    descripcio_en = db.TextProperty()
    preu = db.FloatProperty()
    apartament = db.ReferenceProperty(Apartament)
    fotos = db.ListProperty(db.Key)
    
    def llistat_fotos(self):
        f = Fotos().all().filter('__key__ in',self.fotos)
        return f   
    
    
########## Exemple #################
#a = Apartament(nom="Apartament 1",disponible=True,
#localitzacio= db.GeoPt(-44.22, -33.55),
#descripcio= "HOLA HOLA")
#a.put()
###################################