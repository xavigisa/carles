from manegador.manegador import Handler
from models import Apartament, Fotos, Habitatge, Preu
from google.appengine.ext import db
from google.appengine.api import users
import json

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
            referencia = self.request.get('referencia')
            apartament_id = self.request.get('apartament')
            
            llista_fotos =[]
            for file_data in self.request.POST.getall('imatges[]'):
                f = Fotos(descripcio=file_data.filename, foto= file_data.value)
                f.put()
                llista_fotos.append(f.key())
            
            h = Habitatge(nom=nom,
                          descripcio = desc,
                         referencia = referencia,
                         apartament = db.Key.from_path('Apartament',int(apartament_id)),
                          fotos = llista_fotos)
            
            h.put()
        else:
            self.redirect(users.create_login_url('/gestio/habitatge'))
            
class Preus(Handler):
    def get(self):
        if self.Es_administrador():
            self.render("preus.html")
        else:
            self.redirect(users.create_login_url('/gestio/preus'))
        
    def post(self):
        if self.Es_administrador():
            habitatge = self.request.get('habitatge')
            desc = self.request.get('descripcio')
            preu =   self.request.get('preu')
            ordre = self.request.get('ordre')
            
            
                   
            p = Preu(     descripcio= desc,
                           preu = float(preu),
                           ordre = int(ordre),
                           habitatge = db.Key.from_path("Habitatge", int(habitatge)))
            p.put()
        
        
        
        
        
        
                        
                        
class Consulta(Handler):
    def get(self):
        if self.Es_administrador():
            taula= self.request.get('taula')
            aux = {} 
            if taula== 'apartament':
                a = Apartament().all()
                
                for x in a:
                    aux[x.nom] = x.key().id()
            elif taula == 'habitatge':
                a_id = self.request.get('apartament_id')
                h = Habitatge().all().filter('apartament =',db.Key.from_path('Apartament', int(a_id)))
                for x in h:
                    aux[x.nom] = x.key().id()
                    
                
                
                
            if aux:    
                self.response.headers['Content-Type'] = 'application/json'
                self.response.out.write(json.dumps(aux))
        else:
            self.redirect(users.create_login_url('/'))
                                       