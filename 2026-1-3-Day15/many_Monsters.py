import random

Attac_patern = {
  "bread":1,
  "Magic":2,
  "jump":0,
  "handshake":0
}
Monster_List = {
  "slime":5,
  "Gobrin":6,
  "nite":8,
  "Darek_enper":10
}

Monster_name = random.choice(list(Monster_List.keys()))
Monster_HP = Monster_List[Monster_name]
print(Monster_name,"HP",Monster_HP)
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
  else:
    print("no choices")
    continue

  if Monster_HP < 0:
    Monster_HP = 0
  print(Monster_HP)

print("Monster is deat!!!")
print("you win!!!!")
   
