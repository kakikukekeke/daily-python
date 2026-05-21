import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [
    [sg.Button("ファイルを開く",key="btn1"),sg.Text(key="txt")],
    [sg.Image(key="img")]
]
window = sg.Window("画像ファイル表示",layout,size=(320,380))

def loadimage():
    loadname = sg.popup_get_file("画像ファイルを選択してください")
    if not loadname:
        return
    try:
        img = Image.open(loadname)
        img.thumbnail((300,300))
        bio = io.BytesIO()
        img.save(bio,format="PNG")
        window["img"].update(data=bio.getvalue())
        window["txt"].update(loadname)

    except:
        window["img"].update()
        window["txt"].update("失敗しました")

while True:
    e,v=window.read()
    if e == None:
        break
    if e == "btn1":
        loadimage()
window.close()
