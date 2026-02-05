class Swich:
  def __init__(self):
    self.on = False

  def press(self):
    self.on = not self.on

  def status(self):
    print("ON" if self.on else"off")


sw = Swich()
sw.status()
sw.press()
sw.status()
sw.press()
sw.status()
