import os
import subprocess

input_file = "input.MOV"
output_dir = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/video_cuts")

# フォルダ作成
os.makedirs(output_dir, exist_ok=True)

# ffmpegで30秒ごとに分割
command = [
    "ffmpeg",
    "-i", "input.MOV",
    "-c:v", "libx264",
    "-c:a", "aac",
    "-f", "segment",
    "-segment_time", "30",
    "-reset_timestamps", "1",
    os.path.join(output_dir, "output_%03d.mp4")
]

subprocess.run(command)
