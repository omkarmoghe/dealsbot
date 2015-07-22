import os
import subprocess

filepath =  os.getcwd() + "\Scripts\\activate.bat"
print filepath
print "staring dealsbot..."
subprocess.call(filepath, shell=True)
print("activated!")
subprocess.call("python dealbot.py", shell=True)
print("dealsbot is running...")
