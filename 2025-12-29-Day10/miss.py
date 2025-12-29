def is_even(x):
  if x % 2 == 0:
    return True
  elif x % 3 == 0:
    return False
  
nums = [1,2,3,4,6,7,8,9]

for i in nums:
  is_even(i)
