import pyautogui


pyautogui.click(100, 200)
pyautogui.write('Hello, world!')

pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

pyautogui.hotkey('ctrl', 'c')
