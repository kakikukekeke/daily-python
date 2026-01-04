import random
###　Player attac patern
Attac_patern = {
  "bread":lambda:random.randint(2,4),
  "Magic":lambda:1.5,
  "jump":lambda:random.randint(1,5)
}
### Kind of Monster
Monster_List = {
  "slime":5,
  "Gobrin":6,
  "nite":8,
  "Darek_enper":10
}
Player_HP = 50
##Appearance monster
Monster_name = random.choice(list(Monster_List.keys()))
Monster_HP = Monster_List[Monster_name]
print("A monster appeared!!!!!!")


while Monster_HP > 0:
  print(Monster_name,"HP",Monster_HP)
  print("---serect the attac---")

  for key,Value in Attac_patern.items():
    print(key,Value())
  print("care 3")
  print("----------------------")
  Player_Attac = input("Pleyer Attac  ")


  if Player_Attac in Attac_patern:
    damage = Attac_patern[Player_Attac]()
    print("Take Damge",damage)
    Monster_HP -= damage
    if Monster_HP < 0:
      Monster_HP = 0
      print("Monster is deat!!!")
      print("you win!!!!")
      break
  elif Player_Attac == "care":
    Player_HP += 3
    print("Care Player HP + 3")
    print("Player_HP",Player_HP)
  else:
    print("no choices")
    continue

  if Player_HP <= 0:
    print("Gameover")
    break

  Monster_attac = random.randint(1,5)
  print("Monster Attac",Monster_attac,"Damage")
  print("Damage was taken!")
  Player_HP -= Monster_attac
  print("Player_HP",Player_HP)

  

  
