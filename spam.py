import pyautogui, time

repeat = int(input('how many repeats?'))
time.sleep(2)
for i in range(repeat):
    print(i +1)
    time.sleep(0.05)
    pyautogui.typewrite('spam time ')
    time.sleep(0.01)
    pyautogui.press("enter")
