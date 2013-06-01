from manegador.manegador import Handler
import jinja2


class Principal(Handler):
    def get(self):
        self.Configurar_idioma('en')
        self.render("index.html")