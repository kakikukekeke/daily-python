def judge_score(score):
  for s in score:
    if scores >= 80:
      return "Great"
    elif scores >= 60:
      return "Good"
    else:
      return "Try harder"

scores = [48,64,75,42,96,56,68,45,38,46]

judge_score(score)
