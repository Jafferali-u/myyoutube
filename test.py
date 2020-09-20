import time
import subprocess
import os

subprocess.Popen(["firefox", "https://youtu.be/sQSbsBu2gCU"])
time.sleep(150)
os.system('pkill firefox')
