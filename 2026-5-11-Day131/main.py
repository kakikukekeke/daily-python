import PySimpleGUI as sg
import datetime

layout = [[sg.Text(font=("Arial",40),key="tex",
                   size=(20,1),justification="center")]]

window = sg.Window("時計テスト",layout,size=(320,80),keep_on_top=True)
count = 0
while True:
    e,v = window.read(timeout=500)
    if e == None:
        break
    count += 1
    window["tex"].update(f"{count}")
window.close()
