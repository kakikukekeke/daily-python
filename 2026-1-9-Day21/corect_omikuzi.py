import random
omikuzi = ["daikiti","tyuukiti","syoukiti","kyou"]
result = random.choice(omikuzi)
print(f"Draw a fortune")
print(f"Yore omikuzi is {result}")

if result == "daikiti" or "tyuukiti":
    print("That's good")
else:
    print("That's bad")
