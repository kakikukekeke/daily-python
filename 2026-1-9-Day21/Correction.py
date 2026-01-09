import random
CRITICAL_RATE = 0.2
MAGIC_COST = 3
CARE_COST = 5
CARE_HEAL = 3
LEVEL_UP_EX = 3
ATTAC_PATTERN = {
    "blade":lambda:random.randint(2,4),
    "magic":lambda:random.randint(3,4),
    "jump":lambda:random.randint(1,5)
}

MONSTER_LIST = {
    "silime":lambda:random.randint(5,6),
    "Goblin":lambda:random.randint(8,10),
    "Knight":lambda:random.randint(10,15),
    "Dark Emperor":lambda:random.randint(17,25),
    "Fish Man":lambda:random.randint(12,16)
}

player = {
    "level":1,
    "hp":20,
    "mp":15,
    "exp":0,
}

def spawn_monster():
    name = random.choice(list(MONSTER_LIST.keys()))
    hp = MONSTER_LIST[name]()
    return {"name":name,"hp":hp}

def show_status(monster):
    print("\n--------------------")
    print(f"player HP:{player["hp"]} MP:{player["mp"]}")
    print(f"{monster["name"]}HP:{monster["hp"]}")
    print("---Select Action ---")

    preview = {}
    for key , func in ATTAC_PATTERN.items():
        damage = func()
        preview[key] = damage
        if key == "magic":
            print(f"{key}{damage}(MP -{MAGIC_COST})")
        else:
            print(f"{key}{damage}")
    print(f"care{CARE_HEAL}(HP -{CARE_COST})")
    return preview

def level_up():
    if player["exp"] >= LEVEL_UP_EX:
        player["level"] += 1
        player["hp"] += 5
        player["exp"] = 0
        print("Level UP!")

def player_turn(monster,preview):
    action = input("Plyer Action:").lower()
    if action in ATTAC_PATTERN:
        if action == "magic"and player["mp"] < MAGIC_COST:
            print("NOt enough MP !")
            return False
        
        damge = preview[action]

        if random.random() < CRITICAL_RATE:
            damge *= 2
            print("Critical Damge!")
        
        if action == "magic":
            player["mp"] -= MAGIC_COST

        monster["hp"] -= damge
        print(f"You dealt {damge}damage!")

    elif action == "care":
        if player["mp"] < CARE_COST:
            print("Not enough MP!")
            return False
        player["mp"] -= CARE_COST
        player["hp"] += CARE_HEAL
        print(f"Recovered{CARE_HEAL}HP!")

    else:
        print("Incalid action")
        return False
    
    return True
def monster_turn(monster):
    damage = random.randint(1,5)
    player["hp"] -= damage
    print(f"{monster["name"]}attacks! You take {damage}damage")

def game():
    monster = spawn_monster()
    print(f"\n A wild{monster["name"]}appeared!")

    while monster["hp"] > 0 and player["hp"] > 0:
        preview = show_status(monster)

        if not player_turn(monster,preview):
            continue

        if monster["hp"] <= 0:
            print("MOnster defeated")
            player["exp"] += random.randint(1,4)
            level_up()
            return
        
        monster_turn(monster)

    
    print("game over")


while True:
    game()
    next_action = input("\nwalk / run away:").lower()
    if next_action != "walk":
        print("Thank you for planning!")
        break




