import random
import tkinter as tk
def monster_attac_random():
    damage = random.randint(1,2)
    return damage

def fight_button():
    nareter.place_forget()
    monster_HP.place(relx=0.5, rely=0.1, anchor="center")
    select_action_fight.place_forget()
    select_action_run.place_forget()
    attac_button_1.place(relx=0.4,rely=0.5,anchor="center")
    attac_button_2.place(relx=0.6,rely=0.5,anchor="center")
    attac_button_3.place(relx=0.4,rely=0.7,anchor="center")
    attac_button_4.place(relx=0.6,rely=0.7,anchor="center")

def run_button():
    nareter.place_forget()
    monster_name.place_forget()
    select_action_fight.place_forget()
    select_action_run.place_forget()
    finish_game.place(relx=0.5,rely=0.3,anchor="center")

def Player_attac_1():
    global hp,Player_HP
    hp -= attac[f"blade"]()
    monster_HP.config(text=f"HP{hp}")
    Monster_attack = random.randint(1,2)
    Player_HP -= Monster_attack
    monster_action = tk.Label(root,text=f"Monster Attack HP-{Monster_attack}")
    monster_action.place(relx=0.5,rely=0.27,anchor="center")
    if Player_HP <= 0:
        monster_name.place_forget()
        monster_HP.place_forget()
        Player_HP_label.place_forget()
        monster_action.place_forget()
        Dead_Player.place(relx=0.5,rely=0.27,anchor="center")
    Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")

    if hp <= 0:
        for wiget in root.winfo_children():
            wiget.destroy()
            continue
        monster_dead = tk.Label(root,text="Monster defeat!!!\nYou win !!!")
        monster_dead.place(relx=0.5, rely=0.08, anchor="center")
        finish_game = tk.Label(root,text="Thank you playing!!!!!!")
        finish_game.place(relx=0.5,rely=0.3,anchor="center")


def Player_attac_2():
    global hp,Player_HP,Player_MP
    if Player_MP <= 0:
        monster_action.place_forget()
        Player_no_MP.place(relx=0.5,rely=0.27,anchor="center")
        return
    else:
        Player_MP -= 2
        Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")
        hp -= attac[f"magic"]()
        monster_HP.config(text=f"HP{hp}")
        Monster_attack = random.randint(1,2)
        monster_action = tk.Label(root,text=f"Monster Attack HP-{Monster_attack}")
        Player_HP -= Monster_attack
        monster_action.place(relx=0.5,rely=0.27,anchor="center")
    if Player_HP <= 0:
        monster_name.place_forget()
        monster_HP.place_forget()
        Player_HP_label.place_forget()
        monster_action.place_forget()
        Dead_Player.place(relx=0.5,rely=0.27,anchor="center")
    Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")

    if hp <= 0:
        for wiget in root.winfo_children():
            wiget.destroy()
            continue
        monster_dead = tk.Label(root,text="Monster defeat!!!\nYou win !!!")
        monster_dead.place(relx=0.5, rely=0.08, anchor="center")
        finish_game = tk.Label(root,text="Thank you playing!!!!!!")
        finish_game.place(relx=0.5,rely=0.3,anchor="center")

def Player_attac_3():
    global hp,Player_HP
    hp -= attac[f"jump"]()
    monster_HP.config(text=f"HP{hp}")
    Monster_attack = random.randint(1,2)
    Player_HP -= Monster_attack
    monster_action = tk.Label(root,text=f"Monster Attack HP-{Monster_attack}")
    monster_action.place(relx=0.5,rely=0.27,anchor="center")
    if Player_HP <= 0:
        monster_name.place_forget()
        monster_HP.place_forget()
        Player_HP_label.place_forget()
        monster_action.place_forget()
        Dead_Player.place(relx=0.5,rely=0.27,anchor="center")
    Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")

    if hp <= 0:
        for wiget in root.winfo_children():
            wiget.destroy()
            continue
        monster_dead = tk.Label(root,text="Monster defeat!!!\nYou win !!!")
        monster_dead.place(relx=0.5, rely=0.08, anchor="center")
        finish_game = tk.Label(root,text="Thank you playing!!!!!!")
        finish_game.place(relx=0.5,rely=0.3,anchor="center")

def Player_attac_4():
    global hp,Player_HP,monster_HP,Player_MP
    Monster_attack = monster_attac_random()
    if Player_MP <= 0:
        buttle_message.config(text="Not enough MP")
        return
    Player_MP -= 2
    Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")
    Player_HP += attac[f"care"]()
    monster_HP.config(text=f"HP{hp}")
    Player_HP -= Monster_attack
    buttle_message.config(text=f"Monster Attack HP-{Monster_attack}")
    
    
    if Player_HP <= 0:
        monster_name.place_forget()
        monster_HP.place_forget()
        Player_HP_label.place_forget()
        monster_action.place_forget()
        Dead_Player.place(relx=0.5,rely=0.27,anchor="center")
    Player_HP_label.config(text=f"HP {Player_HP} MP {Player_MP}")

    if hp <= 0:
        for wiget in root.winfo_children():
            wiget.destroy()
            continue
        monster_dead = tk.Label(root,text="Monster defeat!!!\nYou win !!!")
        monster_dead.place(relx=0.5, rely=0.08, anchor="center")
        finish_game = tk.Label(root,text="Thank you playing!!!!!!")
        finish_game.place(relx=0.5,rely=0.3,anchor="center")

monster = {"slime":5,
           "goblin":4}

attac = {"blade":lambda:random.randint(1,2),
         "magic":lambda:random.randint(0,0),
         "jump":lambda:random.randint(1,2),
         "care":lambda:random.randint(5,7)}

name,hp = random.choice(list(monster.items()))
Player_HP = 10
Player_MP = 10



root = tk.Tk()
root.title("RPG")
root.geometry("300x200")
nareter = tk.Label(root,text="monster spone")
nareter.place(relx=0.5, rely=0.08, anchor="center")

Monster_attack = random.randint(1,2)
monster_action = tk.Label(root,text=f"Monster Attack HP-{Monster_attack}")
monster_action.place(relx=0.5,rely=0.27,anchor="center")
monster_action.place_forget()

buttle_message = tk.Label(root,text="")
buttle_message.place(relx=0.5, rely=0.27, anchor="center")

monster_name = tk.Label(root,text=name)
monster_name.place(relx=0.5,rely=0.18,anchor="center")

monster_HP = tk.Label(root,text=f"HP{hp}")

Player_HP_label = tk.Label(root,text=f"HP {Player_HP} MP {Player_MP}")
Player_HP_label.place(relx=0.5,rely=0.37,anchor="center")

Player_no_MP = tk.Label(root,text="Not enough MP ")


select_action_fight = tk.Button(root,text="fight",command=fight_button)
select_action_fight.place(relx=0.4,rely=0.5,anchor="center")

select_action_run = tk.Button(root,text="run away",command=run_button)
select_action_run.place(relx=0.6,rely=0.5,anchor="center")

#Top left →　top rihght → bottom left → bottom right
attac_button_1 = tk.Button(root,text="blade",command=Player_attac_1)
attac_button_2 = tk.Button(root,text="Magic",command=Player_attac_2)
attac_button_3 = tk.Button(root,text="jump",command=Player_attac_3)
attac_button_4 = tk.Button(root,text="care",command=Player_attac_4)

monster_dead = tk.Label(root,text="Monster defeat!!!\nYou win !!!")


finish_game = tk.Label(root,text="Thank you playing!!!!!!")

Dead_Player = tk.Label(root,text="You are Dead!!!")
root.mainloop()
