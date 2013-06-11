#from manegador.manegador import Handler
from manegador.manegador import Handler


class Principal(Handler):
    def get(self):
        self.Configurar_idioma('en')
        self.render("inici.html")


class Principal_es(Handler):
    def get(self):
        self.render("inici_es.html")
        
class Principal_en(Handler):
    def get(self):
        self.render("inici_en.html")