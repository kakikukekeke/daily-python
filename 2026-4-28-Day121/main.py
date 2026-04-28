import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("金額と人数を入力してください")],
          [sg.Text("金額"),sg.Input("1000",key="in1")],
          [sg.Text("人数"),sg.Input("4",key="in2")],
          [sg.Button("実行",key="btn"),sg.Text(key="txt")]]
win = sg.Window("割り勘アプリ",layout,font=(None,14),size=(320,150))

def execute():
    in1 = int(v["in1"])
    in2 = int(v["in2"])
    txt = f"1人、{in1 / in2 : .2f}円です"
    win["txt"].update(txt)

while True:
    e,v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()
