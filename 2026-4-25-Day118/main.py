import PySimpleGUI as sg
sg.theme("DarkBrown3")

layout = [[sg.T("一行一列目",size=(30,1),justification="left")],
          [sg.T("二行一列目",size=(30,1),justification="center")],
          [sg.T("二行一列目",size=(30,1),justification="right")],]
win = sg.Window("要素レイアウト",layout,font=(None,14),size=(300,200))

e,v = win.read()
win.close()
