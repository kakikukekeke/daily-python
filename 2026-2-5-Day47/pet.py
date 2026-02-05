class Pet:
  def __init__(self,name,kind):
    self.name = name
    self.kind = kind

  def speak(self):
    print(self.name,"is a",self.kind)

pet1 = Pet("Pochi","dog")
pet2 = Pet("Toma","cat")

pet1.speak()
pet2.speak()

