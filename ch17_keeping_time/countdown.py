#! python3
# countdown.py - A simple countdown script.

import time
import subprocess

timeLeft = 3
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# TODO: At the end of the countdown, play a sound file.
subprocess.Popen(['alarm.wav'], shell=True)
