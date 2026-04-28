import PySimpleGUI as sg
sg.them("DarkBrown3")

layout = [[sg.Text("身長"),sg.Input(key="height")],
          [sg.Text("体重"),sg.Input(key="body_weight")],
          [sg.Button("計算",key="calculation_button")]
          [sg.Text("あなたのBMI")]]
win = sg.Window("BMI計算機",layout,font=(None,14),size=(320,150))

if True:
