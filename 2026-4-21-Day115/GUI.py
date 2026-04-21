import PySimpleGUI as sg

layout = [[sg.T(k="txt")],[sg.B("実行",k="btn")]]
win = sg.Window("こんにちはテスト",layout,size=(200,100))

def execute():
    win["txt"].update("こんにちは")

while True:
    e,v = win.read()
    if e == "btn":
        execute()

    if e == sg.WIN_CLOSED:
        break

win.close()
