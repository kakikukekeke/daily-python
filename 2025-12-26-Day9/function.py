def judge_score(score):
  if score >= 80:
    return "Great"
  elif score >= 60:
    return "Good"
  else:
    return "Try harder"

score = [48,64,75,42,96,56,68,45,38,46]

for s in score:
  print(s,"i",judge_score(s))
