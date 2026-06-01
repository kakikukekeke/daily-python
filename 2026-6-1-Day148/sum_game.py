import PySimpleGUI as sg
import random
sg.theme("DarkBrown3")

layout = [
    [sg.Text(key="txt1")],
    [sg.Text(key="txt2")],
    [sg.Text(key="txt3"),sg.Input(key="in1"),sg.Button("入力",key="btn",bind_return_key=True)]
]
window = sg.Window("足し算ゲーム",layout,font=(None,14),finalize=True)

def question():
    global playflag,ans
    a = random.randint(0,100)
    b = random.randint(0,100)
    ans = a + b
    window["txt1"].update("足し算ゲームです。答えを入力してね")
    window["txt2"].update("")
    window["txt3"].update(f"問題：{a} + {b} = ?")
    playflag = True

def anscheck():
    global playflag
    if v["in1"].isdecimal() == False:
        window["txt2"].update("数字を入力してね")
    else:
        myunm = int(v["in1"])
        if myunm == ans:
            window["txt2"].update("正解")
            window["txt1"].update("入力ボタンを押すと次の問題が出るよ")
            playflag = False
        else:
            window["txt2"].update(f"{myunm}じゃないよ")
        
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
                          

    
