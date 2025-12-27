def judge_grade(average):
  if average >= 80:
    return 'Great'
  elif average >= 60:
    return "Good"
  else:
    return "Try harder"

scores = [50,38,54,75,53,86,53,31,64,64,35,57,35,78]

def calc_average(scores):
  total = 0
  for s in scores:
    total += s
    return total / len(scores)
  
  average = calc_average(scores)
  result = judge_grade(average)

  print("average:",average)
  print("result:",result)
  

