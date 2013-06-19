from manegador.manegador import Handler
from models import Apartament, Fotos, Habitatge
from google.appengine.ext import db
from google.appengine.api import users

class Gestio(Handler):
    def get(self):
        if self.Es_administrador():
            self.render("gestio.html")
        else:
            self.redirect(users.create_login_url('/gestio/apartament'))
        
    def post(self):
        if self.Es_administrador():
            nom = self.request.get('nom')
            desc = self.request.get('descripcio')
            lat =   self.request.get('lat')
            lon = self.request.get('lon')
            adreca = self.request.get('adreca')
            
            
            llista_fotos =[]
            for file_data in self.request.POST.getall('imatges[]'):
                f = Fotos(descripcio=file_data.filename, foto= file_data.value)
                f.put()
                llista_fotos.append(f.key())
                   
            a = Apartament(nom=nom,
                           localitzacio= db.GeoPt(float(lat), float(lon)),
                           descripcio= desc,
                           adreca = adreca,
                           fotos = llista_fotos)
            a.put()
            
        
        
class Habitatges(Handler):
    def get(self):
        if self.Es_administrador():
            a = Apartament.all()
            parametres = {}
            parametres['apartaments']=a
            self.render("habitatge.html",**parametres)
            
    def post(self):
        if self.Es_administrador():
            nom = self.request.get('nom')
            desc = self.request.get('descripcio')
            preu = self.request.get('preu')
            apartament_id = self.request.get('apartament')
            
            llista_fotos =[]
            for file_data in self.request.POST.getall('imatges[]'):
                f = Fotos(descripcio=file_data.filename, foto= file_data.value)
                f.put()
                llista_fotos.append(f.key())
            
            h = Habitatge(nom=nom,
                          descripcio = desc,
                         preu = (float(preu)),
                         apartament = db.Key.from_path('Apartament',int(apartament_id)),
                          fotos = llista_fotos)
            
            h.put()
        else:
            self.redirect(users.create_login_url('/gestio/habitatge'))
            
            