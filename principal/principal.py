#from manegador.manegador import Handler
from manegador.manegador import Handler
<<<<<<< HEAD:pagines/pagines.py


=======
>>>>>>> 813c830cf2f9db04c34f75abe80bdda73691a548:principal/principal.py


class Principal(Handler):
    def get(self):
        self.Configurar_idioma('en')
        self.render("index.html")
