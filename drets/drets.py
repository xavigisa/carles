from manegador.manegador import Handler


class Drets(Handler):
    def get(self):
        self.render("drets.html")
        
class Drets_es(Handler):
    def get(self):
        self.render("drets_es.html")
        
class Drets_en(Handler):
    def get(self):
        self.render("drets_en.html")