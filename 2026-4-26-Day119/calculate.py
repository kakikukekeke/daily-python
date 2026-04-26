import PySimpleGUI as sg

sg.theme("green")

layout = [[sg.Input("金額",k="fee")],
          [sg.Input("人数",k="num")],
          [sg.Button("計算",key="calculation")],
          [sg.Text("ひとりあたり",key="per")]]

win = sg.Window("割り勘アプリ",layout)

def execute():
    per_person = int(v["fee"]) / int(v["num"])
    win["per"].update(per_person)


while True:
    e,v = win.read()
    if e == None:
        break
    if v["fee"] != "金額":
        win["fee"].update()
    if v["num"] != "人数":
        win["num"].update()

    if e == "calculation":
        execute()


win.close()

    
