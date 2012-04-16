# Create a process that won't end on its own
import subprocess
process = subprocess.Popen(['python.exe', '-c', 'while 1: pass'])

# Kill the process using pywin32
import win32api
win32api.TerminateProcess(int(process._handle), -1)

process = subprocess.Popen(['python.exe', '-c', 'while 1: pass'])

# Kill the process using ctypes
import ctypes
ctypes.windll.kernel32.TerminateProcess(int(process._handle), -1)

process = subprocess.Popen(['python.exe', '-c', 'while 1: pass'])

# Kill the proces using pywin32 and pid
import win32api
PROCESS_TERMINATE = 1
handle = win32api.OpenProcess(PROCESS_TERMINATE, False, process.pid)
win32api.TerminateProcess(handle, -1)
win32api.CloseHandle(handle)

process = subprocess.Popen(['python.exe', '-c', 'while 1: pass'])

# Kill the proces using ctypes and pid
import ctypes
PROCESS_TERMINATE = 1
handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, process.pid)
ctypes.windll.kernel32.TerminateProcess(handle, -1)
ctypes.windll.kernel32.CloseHandle(handle)

# Kill the proces using TaskKill and pid
from locale import str
import os

#process = subprocess.Popen(['python.exe', '-c', 'while 1: pass'])
#os.popen('TASKKILL /PID ' + str(process.pid) + ' /F' + ' /T')

os.popen('TASKKILL /PID ' + str(1408) + ' /F' + ' /T')
os.popen('TASKKILL /PID ' + str(3324) + ' /F' + ' /T')