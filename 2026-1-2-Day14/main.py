def provess_numbers(x):
  return x % 3 == 0

nums = [1,2,3,4,5,6,7,8,9]
result = []
for s in nums:
  if provess_numbers(s):
    s = s * 3
    result.append(s)
  else:
    result.append(s)
print(result)
