from manegador.manegador import Handler
from models import Apartament
from google.appengine.ext import db

class Gestio(Handler):
    def get(self):
        self.render("gestio.html")
        
    def post(self):
        nom = self.request.get('nom')
        desc = self.request.get('descripcio')
        lat =   self.request.get('lat')
        lon = self.request.get('lon')
        for file_data in self.request.POST.getall('imatges[]'):
            desc =desc + file_data.filename
            
        a = Apartament(nom=nom,disponible=True,
                       localitzacio= db.GeoPt(float(lat), float(lon)),
                       descripcio= desc)
        a.put()
        
        
