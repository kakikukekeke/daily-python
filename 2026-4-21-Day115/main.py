import PySimpleGUI as sg

layout = [[sg.T(k="txt")],[sg.B("実行",k="btn")]]
win = sg.Window("こんにちはテスト",layout,size=(200,100))

def excute():
    win["txt"].update("こんにちは")

while True:
    e,v = win.read()
    if e == "btn":
        excute()

    if e == None:
        break

win.close()
