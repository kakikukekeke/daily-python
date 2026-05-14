import PySimpleGUI as sg
from pathlib import Path
import chardet

sg.theme("DarkBrown3")

layout = [
    [sg.Text("テキストファイルを選択してください")],

    [
        sg.Input(key="file_path", size=(40, 1), readonly=True),
        sg.FileBrowse(
            "ファイル選択",
            file_types=(("テキストファイル", "*.txt"),),
            key="browse"
        )
    ],

    [
        sg.Push(),
        sg.Button("OK", key="ok"),
        sg.Button("キャンセル", key="cancel"),
        sg.Push()
    ]
]

window = sg.Window(
    "テキストファイルの読み込み",
    layout,
    font=(None, 14)
)

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "cancel"):
        break

    if event == "ok":
        file_path = values["file_path"]

        if file_path == "":
            sg.popup("ファイルを選択してください")
            continue

        path = Path(file_path)

        try:
            # バイナリで読み込む
            binary_data = path.read_bytes()

            # 文字コード判定
            result = chardet.detect(binary_data)
            encoding = result["encoding"]

            # テキストとして読み込み
            text = binary_data.decode(encoding)

            sg.popup_scrolled(
                text,
                title="ファイル内容",
                size=(80, 20)
            )

        except Exception as e:
            sg.popup_error("エラーが発生しました", e)

window.close()
