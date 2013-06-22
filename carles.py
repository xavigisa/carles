from principal.principal import Principal, Principal_es, Principal_en
from drets.drets import Drets, Drets_es, Drets_en
from concepte.concepte import Concepte, Concepte_es, Concepte_en
from reserves.reserves import Reserves
from condicions.condicions import Condicions
from contacte.contacte import Contacte
from apartaments.apartaments import Apartaments
from apartaments.gestio import Gestio, Habitatges, Preus, Consulta
from foto.foto import Foto, Foto_petita

import webapp2






app = webapp2.WSGIApplication([('/', Principal),
                                     ('/es', Principal_es),
                                     ('/en', Principal_en),
                                     ('/drets',Drets),
                                     ('/es/drets',Drets_es),
                                     ('/en/drets',Drets_en),
                                     ('/concepte',Concepte),
                                     ('/es/concepte',Concepte_es),
                                     ('/en/concepte',Concepte_en),
                                     ('/condicions', Condicions),
                                     ('/contacte',Contacte),
                                     ('/tarifes',Apartaments),
                                     ('/reserves',Reserves),
                                     ('/gestio/apartament',Gestio),
                                     ('/gestio/habitatge',Habitatges),
                                     ('/gestio/preus',Preus),
                                     ('/gestio/consulta',Consulta),
                                     ('/fotos/([0-9]+)',Foto),
                                     ('/fotos_petites/([0-9]+)',Foto_petita)],
                                    debug=True)