
while True:
    a = input("一つ目の数字を入力してください")
    try:
        a = int(a)
        if not (0 <= a <= 100):
            print("数字は０～１００の間で入力してください。")
            continue
        break
         
    except ValueError:
        print("数字は整数で、0~100の間で入力してください。")
        continue

while True:
    b = input("二つ目の数字を入力してください")
    try:
        b = int(b)
        if not (0 <= b <= 100):
            print("数字は０～１００の間で入力してください。")
            continue
        break
         
    except ValueError:
        print("数字は整数で、0~100の間で入力してください。")
        continue
print(a*b)
