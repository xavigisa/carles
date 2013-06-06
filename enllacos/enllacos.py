from manegador.manegador import Handler


class Enllacos(Handler):
    def get(self):
        self.render("enllacos.html")