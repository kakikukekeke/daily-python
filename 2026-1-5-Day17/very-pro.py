def game():
  import random
###　Player attac patern

  Attac_patern = {
    "Blade":lambda:random.randint(2,4),
    "Magic":lambda:random.randint(3,4),
    "Jump":lambda:random.randint(1,5)
  }

### Kind of Monster
  Monster_List = {
    "slime":lambda:random.randint(5,6),
    "Gobrin":lambda:random.randint(8,10),
    "nite":lambda:random.randint(10,15),
    "Darek_emper":lambda:random.randint(17,25),
    "Fish_man":lambda:random.randint(12,16)
  }
  preview = {}
  Player_HP = 50
  Magic_point = 4
  ##Appearance monster
  Monster_name = random.choice(list(Monster_List.keys()))
  Monster_HP = Monster_List[Monster_name]()
  print("A monster appeared!!!!!!")

  #repeat for END
  while Monster_HP > 0 and Player_HP > 0:
    print(Monster_name,"HP",Monster_HP)
    print("---serect the attac---")
  #get the dictionaly
    for key,Value in Attac_patern.items():
      result = Value()
      preview[key] = result
      if key == "Magic":
        print(key,result,"MP -3")
      else:
        print(key,result)
    print("care 3 MP -5")
    print("----------------------")
    Player_Attac = input("Pleyer Attac  ")


    if Player_Attac in Attac_patern:
      damage = preview[Player_Attac]
      if Player_Attac == "Magic":
        if Magic_point < 3:
          print("You have no MP")
          continue
        Magic_point -= 3
        print("MP ",Magic_point)

      print("Take Damge",damage)
      Monster_HP -= damage
      if Monster_HP <= 0:
        Monster_HP = 0
        print("Monster is deat!!!")
        print("you win!!!!")
        print("--select next acction--")
        print("walk / run away")
        break
    elif Player_Attac == "care":
      if Magic_point < 5 :
        print("You dont have MP")
        continue
      Magic_point -= 5
      Player_HP += 3
      print("Care Player HP + 3")
      print("Player_HP",Player_HP)
      print("MP ",Magic_point)
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
    pass
while True:
  game()
  next_aciton = input()
  if next_aciton != "walk":
    print("Thank you playing!!!")
    break
