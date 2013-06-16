from google.appengine.ext import db
from apartaments.models import Fotos
import webapp2
from google.appengine.api import images


class Foto(webapp2.RequestHandler):
    def get(self,identificador):
        if identificador:
            key = db.Key.from_path('Fotos', int(identificador))
            f = db.get(key)
            #f = Fotos.get_by_id(int(self.request.get("identificador")))
            if f:
                imatge = images.Image(f.foto)
                imatge.resize(width=400, height=300)
                imatge.im_feeling_lucky()
                thumbnail = imatge.execute_transforms(output_encoding=images.JPEG)
            
                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(thumbnail)
            else:
                self.error(404)
        else:
            self.error(404)
        