class PiggyBank:
  def __init__(self):
    self.money = 0

  def add(self,amount):
    self.money += amount
  
  def show(self):
    print("Money:",self.money,"yen")


bank = PiggyBank()
bank.add(100)
bank.add(50)
bank.show()
