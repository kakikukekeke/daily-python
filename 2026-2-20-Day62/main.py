class Dog:
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(self.name,"がワンと鳴いた")


dog1 = Dog("daniel")
dog2 = Dog("mcichel")

dog1.bark()
dog2.bark()
