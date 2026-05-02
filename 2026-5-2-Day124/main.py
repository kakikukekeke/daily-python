import PySimpleGUI as sg
sg.theme("DarkBrown3")

eto = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

layout = [
    [sg.Text("あなたの誕生年"), sg.Input(key="birth_year")],
    [sg.Button("実行", key="run_button")],
    [sg.Text("あなたの干支を調べます", key="result")]
]
window = sg.Window("干支調べ",layout,font=(None,14),size=(420,170))

def execute():
    if v["birth_year"] == "" or str.isdigit(v["birth_year"]) == False :
         return
    eto_number = (int(v["birth_year"]) - 4) % 12
    your_eto = f"あなたの干支は{eto[eto_number]}です"
    window["result"].update(your_eto)

while True:
    e,v = window.read()

    if e == None:
        break

    if e == "run_button":
        execute()

window.close()
