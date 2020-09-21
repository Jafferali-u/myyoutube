import time
import subprocess
import os

subprocess.Popen(["firefox", "https://youtu.be/sQSbsBu2gCU"])
time.sleep(150)
os.system('pkill firefox')
subprocess.Popen(["firefox", "https://youtu.be/j9x8JCp2YEo"])
time.sleep(200)
os.system('pkill firefox')
