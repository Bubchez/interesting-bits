# this project uses OCR from pytesseract, so will not run properly unless you have
# installed pytesseract and put the file location of the tesseract.exe in the first variable

# this project was mainly me trying to use OCR for practical purposes, instead of trying to find the most
# efficient way of typing what's on the screen

# this program hasn't been trained, so can only recognise certain texts (like pycharm's segoe UI)

print('please wait')

import pyautogui
import pytesseract
import mouse
import time
import keyboard
pytesseract.pytesseract.tesseract_cmd = 'C:/program files/Tesseract-OCR/tesseract.exe'

try:
    from PIL import Image
except ImportError:
    import Image


mylist = []
click_list = []
j = 0
empty = 0
spaceCount = 0


# shift to mark each corner of the text location
def mark():
    while True:
        if keyboard.is_pressed("shift"):
            x, y = mouse.get_position()
            click_list.append(x)
            click_list.append(y)
            break


# converts the image to a string
def im_to_string(mylist):
    im = pyautogui.screenshot(
        region=(click_list[0], click_list[1], click_list[2] - click_list[0], click_list[3] - click_list[1]))
    text = pytesseract.image_to_string(im)
    for letter in text:
        if letter.isalnum() or letter == ' ' or letter == '\'' or letter == '.' or letter == '?' or letter == '!':

            mylist.append(str(letter))

    return mylist


# main script
def main(mylist, empty):

    print('mark ready')
    for i in range(2):
        mark()
        time.sleep(0.3)

    time.sleep(1)

    while True:
        if not mylist:
            empty += 1
            if empty == 3:
                break
        else:
            empty = 0
        mylist = []
        im_to_string(mylist)
        print(mylist)
        for ii in mylist:
            pyautogui.typewrite(ii)
        pyautogui.typewrite(' ')

        time.sleep(0.01)


main(mylist, empty)
