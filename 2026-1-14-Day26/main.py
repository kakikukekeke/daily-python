import random
import tkinter as tk
def hide_label():
    nareter.place_forget()
    monster_HP.place(relx=0.5, rely=0.1, anchor="center")

    
    

monster = ["slime","goblin"]


root = tk.Tk()
root.title("RPG")
root.geometry("300x200")
nareter = tk.Label(root,text="monster spone")
nareter.place(relx=0.5, rely=0.1, anchor="center")

monster_name = tk.Label(root,text=random.choice(monster))
monster_name.place(relx=0.5,rely=0.3,anchor="center")

monster_HP = tk.Label(root,text="HP5")
select_action_fight = tk.Button(root,text="fight",command=hide_label)
select_action_fight.place(relx=0.4,rely=0.5,anchor="center")

select_action_run = tk.Button(root,text="run away")
select_action_run.place(relx=0.6,rely=0.5,anchor="center")

root.mainloop()
