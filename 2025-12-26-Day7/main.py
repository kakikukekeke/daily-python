scores = [45,82,67,90,38,76]
count = 0

for s in scores:
  if s >= 60:
    print(s)
    count += 1


print("合格者",count,'人')
