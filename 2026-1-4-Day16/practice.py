grades = {
  "A":80,
  "B":60,
  "C":0
}
def judge(score):
  for grade,border in grades.items():
    if score >= border:
      return grade
print(judge(85))
print(judge(65))
print(judge(40))
