import PySimpleGUI as sg
import datetime

layout = [[sg.Text(1111,font=("Arial",40),key="tex",
                   size=(20,1),justification="center")],
                   [sg.Push(),sg.Button("START/STOP",key='btn'),sg.Push()]]

window = sg.Window("時計テスト",layout,size=(400,120),keep_on_top=True)
def execute():
    if startflag == True:
        now = datetime.datetime.now()
        td = now - start
        window["tex"].update(str(td))

def startstop():
    global start,startflag
    if startflag == True:
        startflag = False
    else:
        start = datetime.datetime.now()
        startflag = True


startflag = False

while True:
    e,v = window.read(timeout=500)
    if e == None:
        break
    if e == "btn":
        startstop()
    execute()
window.close()
