import PySimpleGUI as sg

sg.theme("DarkBrown3")

layout = [
    
    [sg.Input("あなたの得点",key="My_Score"),
     sg.Input("平均点",key="average_score"),
     sg.Input("標準偏差",key="standard_deviation")],
    [sg.Push(),sg.Button("実行",key="run"),sg.Push()],
    [sg.Push(),sg.Text("あなたの偏差値は",key="deviation_value"),sg.Push()]
]
window = sg.Window("偏差値",layout)

def calculation():
    your_devitation = 50 + 10 * (float(values["My_Score"]) - float(values["average_score"])) / float(values["standard_deviation"])
    window["decitation_value"].update("yore_devitation")

while True:
    event,values = window.read()
    if event == None:
        break
    if event == "run":
        calculation()

window.close()

