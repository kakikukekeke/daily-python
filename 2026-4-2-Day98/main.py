import subprocess
import tkinter as tk
from tkinter import filedialog
import datetime

##ファイル選択ダイアログ
def open_image():
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



#GUIの構築
root = tk.Tk()
root.title("拡張子変換")
root.geometry("400x450")

btn = tk.Button(root,text="画像ファイルを選択",command=open_image)
btn.pack(pady=20)

label_path = tk.Label(root,text="ファイルが選択されていません",wraplength=350)
label_path.pack()



root.mainloop()

