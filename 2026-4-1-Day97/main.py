import subprocess

com = ["ffmpeg",
       "-i",
       "test.jpg",
       "test.png"]

subprocess.run(com)
