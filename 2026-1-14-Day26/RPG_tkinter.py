import random
import tkinter as tk
def hide_label():
    nareter.place_forget()
    monster_HP.place(relx=0.5, rely=0.1, anchor="center")
    select_action_fight.place_forget()
    select_action_run.place_forget()
    attac_button_1.place(relx=0.4,rely=0.5,anchor="center")
    attac_button_2.place(relx=0.6,rely=0.5,anchor="center")
    attac_button_3.place(relx=0.4,rely=0.7,anchor="center")
    attac_button_4.place(relx=0.6,rely=0.7,anchor="center")


    
    

monster = {"slime":5,
           "goblin":4}

name,hp = random.choice(list(monster.items()))

root = tk.Tk()
root.title("RPG")
root.geometry("300x200")
nareter = tk.Label(root,text="monster spone")
nareter.place(relx=0.5, rely=0.1, anchor="center")

monster_name = tk.Label(root,text=name)
monster_name.place(relx=0.5,rely=0.3,anchor="center")

monster_HP = tk.Label(root,text=hp)
select_action_fight = tk.Button(root,text="fight",command=hide_label)
select_action_fight.place(relx=0.4,rely=0.5,anchor="center")

select_action_run = tk.Button(root,text="run away")
select_action_run.place(relx=0.6,rely=0.5,anchor="center")

#Top left →　top rihght → bottom left → bottom right
attac_button_1 = tk.Button(root,text="blade")
attac_button_2 = tk.Button(root,text="Magic")
attac_button_3 = tk.Button(root,text="jump")
attac_button_4 = tk.Button(root,text="care")

root.mainloop()
