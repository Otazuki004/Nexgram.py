class BadRequest(Exception):
  def __init__(self, err):
    super().__init__(err)
    self.err = err