from manegador.manegador import Handler


class Contacte(Handler):
    def get(self):
        self.render("contacte.html")
        
class Contacte_es(Handler):
    def get(self):
        self.render("contacte_es.html")
        
class Contacte_en(Handler):
    def get(self):
        self.render("contacte_en.html")