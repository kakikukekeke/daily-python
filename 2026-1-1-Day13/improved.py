def calc_average(nums):
  if nums == []:
    return 0
  else:
    number = 0
    for s in nums:
      number += s
    average = number / len(nums)
    return average
nums = [1,2,3,4,5,6,7,8,9]
result = calc_average(nums)
print(result)

