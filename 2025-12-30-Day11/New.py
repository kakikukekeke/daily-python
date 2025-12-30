def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
nums = [1,2,3,4,5,6,7,8,9]

def process_numbers(nums):
  results = []

  for i in nums:
    if is_even(i):
      results.append(i*2)
    else:
      results.append(i)
  return results

result = process_numbers(nums)
print(result)
