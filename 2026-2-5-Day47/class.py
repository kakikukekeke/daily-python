class Counter:
  def __init__(self):
    self.count = 0

  def add(self):
    self.count += 1

  def show(self):
    print("count ",self.count)


c = Counter()
c.add()
c.add()
c.show()
