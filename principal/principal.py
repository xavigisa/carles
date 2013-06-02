from manegador import Handler



class Principal(Handler):
  def get(self):
    self.render("index.html")