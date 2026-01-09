class Enemy:
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp

    def show(self):
        print(f"{self.name}HP{self.hp}")

slime = Enemy("Slime",5)
slime.show()
