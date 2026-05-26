import PySimpleGUI as sg
from PIL import Image
import io
sg.theme("DarkBrown3")

layout = [
    [sg.Button("ファイルを開く",k="open_file"),sg.Text(k="file_name")],
    [sg.Button("ファイル保存",key="save_file")],
    [sg.Image(key="img")]

]
window = sg.Window("モザイク画像に変換",layout,size=(320,400))

def loadimage():
    global img
    loadname = sg.popup_get_file("画像ファイルを選択してください",
                                 file_types=("画像ファイル","*.img *.jpg *.jpeg *.gif *.bmp"))
    if not loadname: return

    try:
        img = Image.open(loadname)
        w = img.width
        h = img.height
        mw = 20
        mh = int(mw * (h / w))
        img = img.resize((mw,mh)).resize((w,h),resample=0)
        img2 = img.copy()
        img2.thumbnail((300,300))
        bio = io.BytesIO()
        img2.save(bio,format="PNG")
        window["img"].update(data=bio.getvalue())
        window["file_name"].update(loadname)
    except:
        window["img"].update()
        window["file_name"].update("失敗しました")
img = None
def saveimg():
    if img == None:return
    savename = sg.popup_get_file("png画像名をつけて保存してください",save_as=True)
    if not savename:
        sg.PopupTimed("png画像名をにゅうえよくしてください")
        return
    if savename.endswith(".png") == False:
        savename = savename + ".png"
    try:
        img.save(savename)
        window["file_name"].update(savename+"を保存しました")
    except:
        window["file_name"].update("失敗しました")

while True:
    e,v = window.read()
    if e == None:break
    if e == "open_file":
        loadimage()
    if e == "save_file":
        saveimg()
window.close()
