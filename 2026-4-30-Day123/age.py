import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("身長と体重を入力してください。")],
          [sg.Text("お母さんの年齢"),sg.Input("45",key="height")],
          [sg.Text("子供の年齢"),sg.Input("10",key="weight")],
          [sg.Button("実行",key="btn"),sg.Text(key="result")]]

window = sg.Window("出生の秘密アプリ",layout,font=(None,14),size=(320,150))

def execute():
    bmi = int(v["height"]) - int(v["weight"])
    txt = f"お母さんは子供を{bmi}歳の時に生みました"
    window["result"].update(txt)




while True:
    e,v = window.read()
    if e == "btn":
        execute()
    if e == None:
        break
window.close()
