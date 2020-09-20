import time
import subprocess
import os

subprocess.Popen(["firefox", "https://youtu.be/sQSbsBu2gCU"])
time.sleep(100)
subprocess.Popen(["firefox", "https://youtu.be/IkjteJNcKqs"])
time.sleep(400)
os.system('pkill firefox')
