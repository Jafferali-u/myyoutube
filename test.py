import time
import subprocess
import os

for i in range(5):
  subprocess.Popen(["firefox", "https://youtu.be/sQSbsBu2gCU"])
  time.sleep(150)
  os.system('pkill firefox')
  subprocess.Popen(["firefox", "https://youtu.be/j9x8JCp2YEo"])
  time.sleep(450)
  os.system('pkill firefox')
  subprocess.Popen(["firefox", "https://youtu.be/vg795v1N2nw"])
  time.sleep(200)
  time.sleep(30)

