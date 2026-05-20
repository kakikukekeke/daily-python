import PySimpleGUI as sg

sg.theme("DarkBrown3")

layout = [
    
    [sg.Input("あなたの得点",key="My_Score"),
     sg.Input("平均点",key="average_score"),
     sg.Input("標準偏差",key="standard_deviation")]
    [sg.Push(),sg.Button("実行",key="run"),sg.Push()]
]
window = sg.Window("偏差値",layout)

def 
