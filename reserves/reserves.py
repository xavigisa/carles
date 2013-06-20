# -*- coding: utf-8 -*-
from manegador.manegador import Handler
from google.appengine.api import mail

class Reserves(Handler):
    def get(self):
        self.render("reserves.html")
        
    def post(self):
        prova = self.request.get('prova')
        fitxers = {}
        
        #fitxers['attachments'] =['nom',fitxer]
        aux =[]
        for file_data in self.request.POST.getall('imatges[]'):
            aux.append([file_data.filename,file_data.value])
            
        fitxers['attachments'] = aux    
                

        mail.send_mail("webstudents.home@gmail.com", 'xavi.gisa@gmail.com', "prova de reserves", """la hhola hola
        
        
        hoñadf ñañdls""", **fitxers)
        # xavi.gisa és el correu al que se le envia
        
        