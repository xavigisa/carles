# -*- coding: utf-8 -*-
from manegador.manegador import Handler
from google.appengine.api import mail
from recaptcha.recaptcha import RecaptchaClient


class Suggerencies(Handler):
    def get(self):
        self.render("suggerencies.html")
        
    def post(self):
        recaptcha_client = RecaptchaClient('6LdYHuMSAAAAAIfXRdLxjKMSEvPnkeeZtPDRQmUa', '6LdYHuMSAAAAAHVyyt9JLh5sxGOyTLCAh8NGn7WN')

        suggerencia = self.request.get('suggerencia')
        correu = self.request.get('correu')
        nom = self.request.get('nom')
        
        
        recaptcha_challenge_field = self.request.get('recaptcha_challenge_field')
        recaptcha_response_field = self.request.get('recaptcha_response_field')
        is_solution_correct = recaptcha_client.is_solution_correct(
                recaptcha_response_field,
                recaptcha_challenge_field,
                self.request.remote_addr,
                )
        fitxers = {}
        
        if is_solution_correct:
            mail.send_mail("webstudents.home@gmail.com", correu, "prova de reserves", correu + "Nom:" + nom)
            # xavi.gisa és el correu al que se le envia
        else:
            self.redirect('/')
        
        
        
