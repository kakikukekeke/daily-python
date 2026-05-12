import PySimpleGUI as sg
import datetime

layout = [
    [sg.Text("", font=("Arial", 40),
             key="tex", size=(20, 1), justification="center")],

    [sg.MLine(font=("Arial", 18),
              size=(40, 12), key="tex2")]
]

window = sg.Window(
    "時計テスト",
    layout,
    size=(500, 300),
    keep_on_top=True
)

sch = [
    ["一限", 8, 50],
    ["二限", 10, 30]
]


def execute():
    now = datetime.datetime.now()

    # 現在時刻表示
    window["tex"].update(now.strftime("%H:%M:%S"))

    tex2 = ""

    for s in sch:
        target = now.replace(
            hour=s[1],
            minute=s[2],
            second=0,
            microsecond=0
        )

        td = target - now

        if td.total_seconds() > 0:
            tex2 += f"{s[0]} ({s[1]:02d}:{s[2]:02d}) あと {td}\n"
        else:
            tex2 += f"{s[0]} ({s[1]:02d}:{s[2]:02d}) 終了\n"

    window["tex2"].update(tex2)


while True:
    e, v = window.read(timeout=500)

    if e == sg.WIN_CLOSED:
        break

    execute()

window.close()
