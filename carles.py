<<<<<<< HEAD
from pagines.pagines import Principal
=======
import manegador

from principal.principal import Principal
>>>>>>> 813c830cf2f9db04c34f75abe80bdda73691a548

import webapp2






app = app = webapp2.WSGIApplication([('/', Principal)],
                                    debug=True)