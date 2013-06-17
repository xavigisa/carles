from manegador.manegador import Handler
from models import Apartament, Fotos
from google.appengine.ext import db

class Gestio(Handler):
    def get(self):
        if self.Es_administrador():
            self.render("gestio.html")
        
    def post(self):
        if self.Es_administrador():
            nom = self.request.get('nom')
            desc = self.request.get('descripcio')
            equip = self.request.get('equipament')
            serv = self.request.get('serveis')
            lat =   self.request.get('lat')
            lon = self.request.get('lon')
            preu = self.request.get('preu')
            
            
            
                
            a = Apartament(nom=nom,disponible=True,
                           localitzacio= db.GeoPt(float(lat), float(lon)),
                           descripcio= desc,
                           preu = float(preu),
                           equipament = equip,
                           serveis = serv)
            a.put()
            for file_data in self.request.POST.getall('imatges[]'):
                f = Fotos(descripcio=file_data.filename, foto= file_data.value, apartament = a)
                f.put()
        
        
