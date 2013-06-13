from manegador.manegador import Handler
from models import Apartament


class Apartaments(Handler):
    def get(self):
        a = Apartament.all()
        parametres = {}
        parametres['apartaments'] = a
        self.render("apartaments.html", **parametres)
        
        
class Apartaments_es(Handler):
    def get(self):
        self.render("apartaments_es.html")
        
class Apartaments_en(Handler):
    def get(self):
        self.render("apartaments_en.html")