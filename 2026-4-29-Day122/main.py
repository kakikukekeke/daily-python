import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.Text("身長"),sg.Input(key="height")],
          [sg.Text("体重"),sg.Input(key="body_weight")],
          [sg.Button("計算",key="calculation_button")],
          [sg.Text("あなたのBMI",key="your_BMI")]]
win = sg.Window("BMI計算機",layout,font=(None,14),size=(320,150))
def execute():
    BMI = float(values["body_weight"]) / (float(values["height"]) ** 2)
    win["your_BMI"].update(BMI)


while True:
    event,values = win.read()
    if event == "calculation_button":
        execute()
    if event == None:
        break
win.close()
