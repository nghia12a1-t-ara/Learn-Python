import pyautogui
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = 1)
    distance -= 25
    pyautogui.dragRel(0, distance, duration = 1)
    pyautogui.dragRel(-distance, 0, duration = 1)
    distance -= 25
    pyautogui.dragRel(0, -distance, duration = 1)
