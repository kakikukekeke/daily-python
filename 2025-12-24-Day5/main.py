even_count = 0
odd_count = 0
three_count = 0

for i in range(1,51):
  if i % 2 == 0:
    even_count += 1
  else:
      odd_count += 1
  if i % 3 == 0:
     three_count += 1

print("偶数",even_count)
print("奇数",odd_count)
print("３の倍数",three_count)
