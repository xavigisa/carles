# -*- coding: utf-8 -*-
from manegador.manegador import Handler
from google.appengine.api import mail
from recaptcha.recaptcha import RecaptchaClient


class Reserves(Handler):
    def get(self):
        self.render("reserves.html")
        
    def post(self):
        recaptcha_client = RecaptchaClient('6LdYHuMSAAAAAIfXRdLxjKMSEvPnkeeZtPDRQmUa', '6LdYHuMSAAAAAHVyyt9JLh5sxGOyTLCAh8NGn7WN')

        prova = self.request.get('prova')
        recaptcha_challenge_field = self.request.get('recaptcha_challenge_field')
        recaptcha_response_field = self.request.get('recaptcha_response_field')
        is_solution_correct = recaptcha_client.is_solution_correct(
                recaptcha_response_field,
                recaptcha_challenge_field,
                self.request.remote_addr,
                )
        fitxers = {}
        
        if is_solution_correct:
            #fitxers['attachments'] =['nom',fitxer]
            aux =[]
            for file_data in self.request.POST.getall('imatges[]'):
                aux.append([file_data.filename,file_data.value])
                
            fitxers['attachments'] = aux    
                    
    
            mail.send_mail("webstudents.home@gmail.com", 'xavi.gisa@gmail.com', "prova de reserves", """la hhola hola
            
            
            hoñadf ñañdls""", **fitxers)
            # xavi.gisa és el correu al que se le envia
        else:
            self.redirect('/')
        
        
        
