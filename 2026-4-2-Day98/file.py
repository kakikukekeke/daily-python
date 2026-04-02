import subprocess
import tkinter as tk
from tkinter import filedialog
import datetime

##ファイル選択ダイアログ png
def open_image_png():
    #ファイル名を現在時刻にする
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"output_{now}.png"


    file_path = filedialog.askopenfilename(
        filetypes=[("Image files","*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    com = ["ffmpeg",
       "-i",
       file_path,
       output_name]
    subprocess.run(com)

##ファイル選択ダイアログ jpg
def open_image_jpg():
    #ファイル名を現在時刻にする
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"output_{now}.jpg"


    file_path = filedialog.askopenfilename(
        filetypes=[("Image files","*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    com = ["ffmpeg",
       "-i",
       file_path,
       output_name]
    subprocess.run(com)
##ファイル選択ダイアログ webP
def open_image_webP():
    #ファイル名を現在時刻にする
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_name = f"output_{now}.webp"


    file_path = filedialog.askopenfilename(
        filetypes=[("Image files","*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    com = ["ffmpeg",
       "-i",
       file_path,
       output_name]
    subprocess.run(com)
#GUIの構築
root = tk.Tk()
root.title("拡張子変換")
root.geometry("400x450")


#png button
btn = tk.Button(root,text="png",command=open_image_png)
btn.pack(side="left",pady=20)

#jpg button
btn = tk.Button(root,text="jpeg",command=open_image_jpg)
btn.pack(side="left",pady=20)

#webP button
btn = tk.Button(root,text="webP",command=open_image_webP)
btn.pack(side="left",pady=20)

label_path = tk.Label(root,text="変えたい画像先を選択してください",wraplength=350)
label_path.pack()



root.mainloop()

