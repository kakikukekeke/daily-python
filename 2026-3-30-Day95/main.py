import subprocess
import tkinter as tk

root = tk.Tk()
root.title("画像変換アプリ")
root.geometry("400x300")


com = [
    "ffmpeg",
    "-i","sample.HEIC",
    "sample.png"
]

#res = subprocess.call(com)

#print(res)

root.mainloop()
