import random

Attac_patern = {
  "bread":1,
  "Magic":2,
  "jump":0,
  "care":0
}
Monster_HP = 10
while Monster_HP > 0:
  print("Monster",Monster_HP)
  print("serect attac")

  for key,Value in Attac_patern.items():
    print(key)
  Player_Attac = input("Pleyer Attac")

  if Player_Attac in Attac_patern:
    damage = Attac_patern[Player_Attac]
    print("Take Damge",damage)
    Monster_HP -= damage

  if Monster_HP < 0:
    Monster_HP = 0
  print(Monster_HP)

print("Monster is deat!!!")
print("you win!!!!")
   
