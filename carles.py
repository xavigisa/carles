from pagines.pagines import Principal

import webapp2






app = app = webapp2.WSGIApplication([('/', Principal)],
                                    debug=True)