score = [72,80,71,52,84]
total = 0 
for s in score:
  total += s

average = total / len(score)

print('averege:',average)

if average >= 80:
  print("Greate")
elif average >= 60:
  print("Good")
else:
  print("Try harder")
