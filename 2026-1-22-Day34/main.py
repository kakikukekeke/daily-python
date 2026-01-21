class person:
    def __init__(self,name):
        self.name = name

    def say_name(self):
        print("My name is ",self.name)

    
p1 = person("ken")
p1.say_name()
