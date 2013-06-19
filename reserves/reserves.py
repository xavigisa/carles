from manegador.manegador import Handler

class Reserves(Handler):
    def get(self):
        self.render("reserves.html")
        