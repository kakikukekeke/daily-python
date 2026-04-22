import PySimpleGUI as sg

layout = [[sg.Input("ふたば",key="in")],
          [sg.Button("実行",key="btn")],
          [sg.Text(key="tex")]]

window = sg.Window("挨拶テスト",layout)

def execute():
    tex = "こんにちは," + values["in"] + "さん"
    window["tex"].update(tex)

while True:
    event, values = window.read()

    if event == "btn":
        execute()

    if event == None:
        break

window.close()
