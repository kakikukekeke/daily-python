import PySimpleGUI as sg
import io
import qrcode
sg.theme("DarkBrown3")

layout = [
    [sg.Text("URL:"),sg.Input(key="in_URL")],
    [sg.Button("QRコード作成",k="make_QR")],
    [sg.Button("ファイルを保存",key="save_file"),sg.Text(key="txt")],
    [sg.Image(key="image")]
]
window = sg.Window("QRコードメーカー",layout,size=(320,420))

img = None
def execute():
    global img
    if not v["in_URL"]:
        sg.PopupTimed("URLを入力してください")
        return
    img = qrcode.make(v["in_URL"])
    img.thumbnail((300,300))
    bio = io.BytesIO()
    img.save(bio,format="PNG")
    window["image"].update(data=bio.getvalue())

def saveimage():
    if img == None:
        return
    savename = sg.popup_get_file("png画像名をつけて保存してください",save_as=True)
    if not savename:
        sg.PopupTimed("png画像名を入力してください")
        return
    if savename.endswith(".png") == False:
        savename = savename + ".png"

    try:
        img.save(savename)
        window["txt"].update(savename+"画像を保存しました")
    except:
        window["txt"].update("失敗しました")

while True:
    e,v = window.read()
    if e == None:
        break
    if e == "make_QR":
        execute()
    if e == "save_file":
        saveimage()
window.close()
