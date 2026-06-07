
while True:
    a = input("一つ目の数字を入力してください")
    if 0 >= int(a) or int(a) >= 100:
            print("数字を０～１００の間で入力してください")
            continue
    try:
        break
    except:
        print("数字は整数で、0~100の間で入力してください。")
        continue

while True:
    b = input("二つ目の数字を入力してください")
    if 0 >= int(b) or int(b) >= 100:
            print("数字は０～１００の間で入力してください")
            continue
    try:
        print(int(a) * int(b))
        break
    except:
        print("数字は整数で、0~100の間で入力してください。")
        continue
