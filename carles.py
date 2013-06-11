from principal.principal import Principal, Principal_es, Principal_en
from drets.drets import Drets, Drets_es, Drets_en
from concepte.concepte import Concepte, Concepte_es, Concepte_en


import webapp2






app = app = webapp2.WSGIApplication([('/', Principal),
                                     ('/es', Principal_es),
                                     ('/en', Principal_en),
                                     ('/drets',Drets),
                                     ('/es/drets',Drets_es),
                                     ('/en/drets',Drets_en),
                                     ('/concepte',Concepte),
                                     ('/es/concepte',Concepte_es),
                                     ('/en/concepte',Concepte_en)],
                                    debug=True)