import pyautogui


print(pyautogui.position())                     # Get current mouse position.
print(pyautogui.position())                     # Get current mouse position again.

p = pyautogui.position()                        # And again.
print(p)

print(p[0])                                     # The x-coordinate is at index 0.
print(p.x)                                      # The x-coordinate is also in the x attribute.
