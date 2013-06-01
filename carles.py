import manegador
import pagines

import webapp2






app = app = webapp2.WSGIApplication([('/', pagines.Principal)],
                                    debug=True)