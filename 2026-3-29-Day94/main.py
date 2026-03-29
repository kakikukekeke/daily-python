import subprocess

com = [
    "ffmpeg",
    "-i","sample.HEIC",
    "sample.png"
]

res = subprocess.call(com)

print(res)
