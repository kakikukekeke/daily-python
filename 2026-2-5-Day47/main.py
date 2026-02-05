class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    

  def intoroduce(self):
    print("My name is ",self.name)
    print("I am ",self.age,"years old")

p1 = Person("ken",20)
p1.intoroduce()
