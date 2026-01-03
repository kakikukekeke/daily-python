nums = [1,2,3,4,5,6,7,8]
def chek_number(x):
  if x % 2 == 0 and x % 3 == 0:
    return "FizzBuzz"
  elif x % 2 == 0:
    return "Fizz"
  elif x % 3 == 0:
    return "Buzz"
  else:
    return x
  
result = []
for s in nums:
  result.append(chek_number(s))

print(result)
