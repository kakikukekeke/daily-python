nums = [1,2,3,4,5,6,7,8,9]

def zero_three(nums):
  result = []

  for i in nums:
    if i % 3 == 0:
      result.append(0)
    else:
      result.append(i)

  return result

result = zero_three(nums)
print(result)
