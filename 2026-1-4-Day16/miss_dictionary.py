scores = {
  "Alice":78,
  "Bob":92,
  "Charlie":65,
  "Dave":50
}
def judge(score):
  for key,value in scores.items():
    if value >= 80:
      return "A"
    elif value >= 60:
      return "B"
    else:
      return "C"
result = judge(scores)
print(result)
