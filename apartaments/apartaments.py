from manegador.manegador import Handler
from models import Apartament, Fotos


class Apartaments(Handler):
    def get(self):
        a = Apartament.all()
        parametres = {}
        parametres['apartaments'] = a
        #fotos = Fotos.all().filter('apartament =',a)
        #parametres['fotos'] = fotos
        self.render("apartaments.html", **parametres)
        
        
class Apartaments_es(Handler):
    def get(self):
        self.render("apartaments_es.html")
        
class Apartaments_en(Handler):
    def get(self):
        self.render("apartaments_en.html")