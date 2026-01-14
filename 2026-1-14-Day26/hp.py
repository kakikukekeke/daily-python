import random
import tkinter as tk
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
    global hp
    hp -= attac[f"blade"]()
    monster_HP.config(text=f"HP{hp}")

    if hp <= 0:
        monster_HP.config(text="Monster defeat!")


def Player_attac_2():
    global hp
    hp -= attac[f"magic"]()
    monster_HP.config(text=f"HP{hp}")

    if hp <= 0:
        monster_HP.config(text="Monster defeat!")

def Player_attac_3():
    global hp
    hp -= attac[f"jump"]()
    monster_HP.config(text=f"HP{hp}")

    if hp <= 0:
        monster_HP.config(text="Monster defeat!")

def Player_attac_4():
    global hp
    hp -= attac[f"care"]()
    monster_HP.config(text=f"HP{hp}")

    if hp <= 0:
        monster_HP.config(text="Monster defeat!")




    
    

monster = {"slime":5,
           "goblin":4}

attac = {"blade":lambda:random.randint(1,2),
         "magic":lambda:random.randint(1,2),
         "jump":lambda:random.randint(1,2),
         "care":lambda:random.randint(1,2)}

name,hp = random.choice(list(monster.items()))

root = tk.Tk()
root.title("RPG")
root.geometry("300x200")
nareter = tk.Label(root,text="monster spone")
nareter.place(relx=0.5, rely=0.1, anchor="center")

monster_name = tk.Label(root,text=name)
monster_name.place(relx=0.5,rely=0.2,anchor="center")

monster_HP = tk.Label(root,text=f"HP{hp}")

select_action_fight = tk.Button(root,text="fight",command=fight_button)
select_action_fight.place(relx=0.4,rely=0.5,anchor="center")

select_action_run = tk.Button(root,text="run away",command=run_button)
select_action_run.place(relx=0.6,rely=0.5,anchor="center")

#Top left →　top rihght → bottom left → bottom right
attac_button_1 = tk.Button(root,text="blade",command=Player_attac_1)
attac_button_2 = tk.Button(root,text="Magic",command=Player_attac_2)
attac_button_3 = tk.Button(root,text="jump",command=Player_attac_3)
attac_button_4 = tk.Button(root,text="care",command=Player_attac_4)



finish_game = tk.Label(root,text="Thank you playing!!!!!!")

root.mainloop()
