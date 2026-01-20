import tkinter as tk

root = tk.Tk()
root.title("aaa")
root.geometry("300x300")
count = 0
def count_buttn():
    global count
    count += 1
    count_up_label.config(text=count)


count_up_label = tk.Label(root,text=count)
count_up_label.place(relx=0.4,rely=0.4,anchor="center")
nmber_count_button = tk.Button(root,text="count UP",command=count_buttn)
nmber_count_button.place(relx=0.3,rely=0.3,anchor="center")
root.mainloop()
