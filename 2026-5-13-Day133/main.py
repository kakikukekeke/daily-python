import PySimpleGUI as sg

svename = sg.popup_get_file("名前をつけて保存してください",default_path="text.txt",save_as=True)
print(svename)
