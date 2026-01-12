import tkinter as tk

root = tk.Tk()
root.title("RPG")
root.geometry("350x300")

nareter = tk.Label(root,text="Monster spone!!!")
nareter.grid(row=0,column=0,columnspan=2,pady=10)
monster_name = tk.Label(root,text="slime")
monster_name.grid(row=0,column=0,columnspan=2,pady=10)

select_action_light = tk.Button(root,text="fight")
select_action_left = tk.Button(root,text="run away")
select_action_left.grid(row=0,padx=50,pady=60)
select_action_light.pack(padx=20,pady=50)


root.mainloop()
