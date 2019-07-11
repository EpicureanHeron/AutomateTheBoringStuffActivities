import time, subprocess

timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen('C:/Program Files (x86)/Notepad++/notepad++.exe', 'getToWork.txt')