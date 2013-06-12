#from manegador.manegador import Handler
from manegador.manegador import Handler


class Condicions(Handler):
    def get(self):    
        self.render("condicions.html")