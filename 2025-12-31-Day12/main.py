def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count

nums = [1,2,3,4,5,6,7,8,9]
result = count_evens(nums)
print(result)
