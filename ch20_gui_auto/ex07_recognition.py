import pyautogui


b = pyautogui.locateOnScreen('submit.png')
print(b)
print(b[0])
print(b.left)
