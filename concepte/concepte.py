from manegador.manegador import Handler


class Concepte(Handler):
    def get(self):
        self.render("concepte.html")
        
        
class Concepte_es(Handler):
    def get(self):
        self.render("concepte_es.html")
        
class Concepte_en(Handler):
    def get(self):
        self.render("concepte_en.html")