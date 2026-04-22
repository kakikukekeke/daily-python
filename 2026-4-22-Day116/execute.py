import PySimpleGUI as sg

sg.theme("BrightColors")

layout = [[sg.I("フタバ",k="in")],
          [sg.B("実行",k="btn")],
          [sg.T(k="txt")]]

win = sg.Window("挨拶テスト",layout,font=(None,14),size=(250,120))

def execute():
    tex = "こんにちは" +v["in"] + "さん"
    win["txt"].update(tex)

while True:
    e,v = win.read()
    if e == "btn":
        execute()

    if e == None:
        break

win.close()
