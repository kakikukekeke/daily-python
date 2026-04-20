import tkinter as tk

def execute():
    tex = "こんにちは"
    lbl.configure(text=tex)
    
root = tk.Tk()
root.title("こんにちはテスト")
root.geometry("200x300")

lbl = tk.Label(root,text="")
btn = tk.Button(root,text="実行",command=execute)


lbl.pack()
btn.pack()
root.mainloop()
