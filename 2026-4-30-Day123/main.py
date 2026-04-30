import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("身長と体重を入力してください。")],
          [sg.Text("身長cm"),sg.Input("160",key="height")],
          [sg.Text("体重"),sg.Input("60",key="weight")],
          [sg.Button("実行",key="btn"),sg.Text(key="result")]]

window = sg.Window("BMI計算アプリ",layout,font=(None,14),size=(320,150))

def execute():
    height = float(v["height"]) / 100.0
    weight = float(v["weight"])
    bmi = weight / (height ** 2)
    txt = f"BMI値は、{bmi:.2f}です"
    window["result"].update(txt)




while True:
    e,v = window.read()
    if e == "btn":
        execute()
    if e == None:
        break
window.close()
