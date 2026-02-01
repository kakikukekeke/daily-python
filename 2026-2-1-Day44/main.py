class counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def show(self):
        print(self.count)

c = counter()

c.add()
c.add()
c.add()

c.show()
