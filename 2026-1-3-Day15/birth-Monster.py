import random

Monster_HP = 10
while Monster_HP > 0:
  print("Monster",Monster_HP)
  Player_Attac = random.randint(1,5)
  print("Take Damege",Player_Attac)
  Monster_HP -= Player_Attac
  if Monster_HP < 0:
    Monster_HP = 0
  print(Monster_HP)

print("Monster is deat!!!")
   
