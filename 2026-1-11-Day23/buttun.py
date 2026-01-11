import tkinter as tk

def change_text():
    label.config(text="changed!")
root = tk.Tk()
root.title("The First Tkinter")
root.geometry("300x150")

label = tk.Label(root,text="Hello tkinter!")
label.pack()

button = tk.Button(root,text="change",command=change_text)
button.pack()
root.mainloop()
