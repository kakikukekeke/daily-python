class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introdce(self):
        print(f"hello I'm{self.name},and {self.age}years old")

    def birthday(self):
        self.age += 1
        print(f"{self.name} be {self.age} years old.")

Dog1 = Dog("ken",3)
Dog2 = Dog("sasuke",5)
Dog3 = Dog("maichel",5)
Dog3.introdce()
Dog1.introdce()
Dog2.introdce()

Dog1.birthday()
Dog2.birthday()
