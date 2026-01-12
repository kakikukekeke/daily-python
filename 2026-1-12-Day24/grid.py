import tkinter as tk

root = tk.Tk()
root.title("RPG")
root.geometry("350x300")

nareter = tk.Label(root,text="Monster spone!!!")
nareter.grid(row=0,column=0,columnspan=2,pady=10)

monster_name = tk.Label(root,text="slime")
monster_name.grid(row=1,column=0,columnspan=2,pady=10)

select_action_light = tk.Button(root,text="fight")
select_action_light.grid(row=2,column=0,padx=10,pady=30)

select_action_left = tk.Button(root,text="run away",width=12)
select_action_left.grid(row=2,column=1,padx=10,pady=30)



root.mainloop()
