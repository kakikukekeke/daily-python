import os
import subprocess

input_file = "input.mp4"
output_dir = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/video_cuts")

# フォルダ作成
os.makedirs(output_dir, exist_ok=True)

# ffmpegで30秒ごとに分割
command = [
    "ffmpeg",
    "-i", input_file,
    "-c", "copy",
    "-map", "0",
    "-segment_time", "30",
    "-f", "segment",
    os.path.join(output_dir, "output_%03d.mp4")
]

subprocess.run(command)
