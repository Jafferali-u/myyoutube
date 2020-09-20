import time
import subprocess
import os

subprocess.Popen(["firefox", "https://youtu.be/tuIZok81iLk"])
time.sleep(30)
os.system('pkill firefox')
