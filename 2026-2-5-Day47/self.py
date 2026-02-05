class Player:
  def __init__(self,name):
    self.name = name
    self.hp = 100

  
  def damage(self,amount):
    self.hp -= amount
    print(self.name,"took",amount,"damage")

  
  def status(self):
    print("HP",self.hp)


player = Player("hello")
player.damage(30)
player.status()

