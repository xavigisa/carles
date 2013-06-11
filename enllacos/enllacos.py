from manegador.manegador import Handler


class Enllacos(Handler):
    def get(self):
        self.render("enllacos.html")
        
        
        
class Enllacos_es(Handler):
    def get(self):
        self.render("enllacos_es.html")
        
class Enllacos_en(Handler):
    def get(self):
        self.render("enllacos_en.html")