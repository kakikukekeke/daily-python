import PySimpleGUI as sg
import random

layout = [
    [sg.Text(key="hint")],
    [sg.Text("試行回数",key="attempt")],
    [sg.Input(key="answer"),sg.Button("実行",bind_return_key="run")]
]
sg.theme("DarkBrown3")

window = sg.Window("数字あてゲーム",layout,font=(None,14),finalize=True)

def question():
    global playflag,ans,count
    ans = random.randint(1,100)
    count = 0
    playflag = True

def anscheck():
    global playflag,countif ,count
    if v["answer"].isdecimal() == False:
        window["hint"].update("数字を入力してね")
    else:
        count += 1
        mynum = int(v["answer"])
        if mynum == ans:
            window["hint"].update(f"あたり！答えは{ans}です！")
            window["attempt"].update(f"試行回数{count}")
            playflag = False
        elif mynum < ans:
            window["hint"].update("もっと大きいよ")
            window["attempt"].update(f"試行回数{count}")
        else:
            window["hint"].update("もっと小さいよ")
            window["attempt"].update(f"試行回数{count}")
question()
while True:
    e,v = window.read()
    if e == None:
        break
    if playflag == False:
        question()
    else:
        anscheck()
window.close()


