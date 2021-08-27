import pyautogui


wh = pyautogui.size() # Obtain the screen resolution.
print(wh)                                                       # Size(width=1920, height=1080)
print(wh[0])                                                    # 1920
print(wh.width)                                                 # 1920
