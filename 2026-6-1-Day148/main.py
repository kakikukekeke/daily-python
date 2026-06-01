import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [
    [sg.Text("おみくじを引きましょう！")],
    [sg.Text("結果は、、、",key="result")],
    [sg.Button("おみくじを引く",key="draw_omikuzi")]
]
window = sg.Window("おみくじアプリ",layout)
omikuzi = ["大吉","中吉","小吉"]

def Drow_a_fortune_slip():
    kekka = random.choice(omikuzi)
    txt = f"結果は{kekka}でした！"
    window["result"].update(txt)

while True:
    e,v = window.read()
    if e == None:
        break
    if e == "draw_omikuzi":
        Drow_a_fortune_slip()

window.close()

    
