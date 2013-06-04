from principal.principal import Principal


import webapp2






app = app = webapp2.WSGIApplication([('/', Principal)],
                                    debug=True)