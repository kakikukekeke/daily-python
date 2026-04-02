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
# --- GUIの構築 ---
root = tk.Tk()
root.title("拡張子変換")
root.geometry("400x200") # 縦が長すぎたので少し調整

# 1. ボタンたちをまとめる「透明な箱」を作る
button_frame = tk.Frame(root)
button_frame.pack(pady=20) # この箱自体は上から順に配置（縦並び）

# 2. ボタンはその「箱の中」に左から詰めていく
btn_png = tk.Button(button_frame, text="png", command=open_image_png, width=10)
btn_png.pack(side="left", padx=5)

btn_jpg = tk.Button(button_frame, text="jpeg", command=open_image_jpg, width=10)
btn_jpg.pack(side="left", padx=5)

btn_webp = tk.Button(button_frame, text="webP", command=open_image_webP, width=10)
btn_webp.pack(side="left", padx=5)

# 3. ラベルは「箱の外」に置くので、ボタンの下に配置される
label_path = tk.Label(root, text="変換したいファイル形式のボタンを押してください", wraplength=350)
label_path.pack(pady=10)

root.mainloop()


