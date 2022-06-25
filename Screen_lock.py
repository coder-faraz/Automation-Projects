import pyautogui
import time

pyautogui.hotkey('win', 'r')
time.sleep(0.500)

pyautogui.typewrite('cmd\n')
time.sleep(1)

pyautogui.typewrite('rundll32.exe user32.dll, LockWorkStation\n')

