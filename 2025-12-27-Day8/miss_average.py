scores = [32,60,70,53,69,58,39]
def calc_average(scores):
  total = 0
  for s in scores:
    total += 1
    return total / len(scores)

average = calc_average(scores)
print("average:",average)

