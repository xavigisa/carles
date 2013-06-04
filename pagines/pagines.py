#from manegador.manegador import Handler
from manegador.manegador import Handler




class Principal(Handler):
    def get(self):
        self.Configurar_idioma('en')
        self.render("index.html")