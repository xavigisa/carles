from manegador import Handler


class Principal(Handler):
    def get(self):
        self.Configurar_idioma('en')
        self.render("index.html")
