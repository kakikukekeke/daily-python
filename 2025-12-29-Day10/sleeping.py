def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
nums = [1,2,3,4,6,7,8,9]
results = []
for i in nums:
  if is_even(i):
    i = i * 2
    results.append(i)
  else:
    results.append(i)

print(results)
