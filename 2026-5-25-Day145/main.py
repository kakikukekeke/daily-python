import PySimpleGUI as sg
import ffmpeg
import os
import math

sg.theme("DarkBrown3")

layout = [
    [sg.Button("動画ファイルを開く", key="btn1"), sg.Text(key="txt")],
    [sg.Text("ここに処理結果が表示されます", size=(40, 2), key="result")]
]

window = sg.Window("ショート動画カットツール",layout,size=(400,150))

def edit_video():
    loadname = sg.popup_get_file("動画ファイルを選択してください",file_types=(("動画ファイル","*.mp4 *.avi *.mkv"),))
    if not loadname:return
    window["txt"].update(os.path.basename(loadname))
    window["result"].update("画像処理中...お待ちください")
    window.refresh()
    probe = ffmpeg.probe(loadname)
    duration = float(probe["format"]["duration"])
    loop_count = math.ceil(duration / 30)

    try:
        for i in range(loop_count):
            cut_time = i * 30
            base,ext = os.path.splitext(loadname) 
            output_name = f"{base}_part{i + 1}.mp4"
            (
                ffmpeg
                .input(loadname)
                .output(output_name,ss=cut_time,t=30,c="copy")
                .run(overwrite_output=True)
            )  
            window["result"].update(f"成功しました")
    except Exception as e:
        window["result"].update("失敗しました")

while True:
    e,v = window.read()
    if e is None:
        break
    if e == "btn1":
        edit_video()
window.close()
