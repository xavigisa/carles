from manegador import Handler
import jinja2


class Principal(Handler):
  def get(self):
    self.render("index.html")