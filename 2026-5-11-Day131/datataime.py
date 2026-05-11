import PySimpleGUI as sg
import datetime

layout = [[sg.Text(font=("Arial",40),key="tex",
                   size=(20,1),justification="center")]]

window = sg.Window("時計テスト",layout,size=(400,80),keep_on_top=True)
def execute():
    now = datetime.datetime.now()
    window["tex"].update(f"{now:%H:%M:%S}")

while True:
    e,v = window.read(timeout=500)
    if e == None:
        break
    execute()
window.close()
