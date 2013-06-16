# -*- coding: utf-8 -*- 
import webapp2
import os
import jinja2
from google.appengine.api import users

template_dir = os.path.join(os.path.dirname(__file__),'../templates')

jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(template_dir),
                                                            autoescape = True)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
    def Configurar_idioma(self,idioma):
        self.response.set_cookie('lang',idioma) #, secure=True)
        
    def Idioma(self):
        lang = self.request.cookies.get('lang')
        if not lang:
            lang = 'ca'
        return lang
    
    def Es_administrador(self):
        user = users.get_current_user()
        if users.is_current_user_admin():
            return True
        #if user:
            #return (user.nickname() in ['javiergimenezsanchez','xavi.gisa'])
        else:
            return False