# this project uses OCR from pytesseract, so will not run properly unless you have
# installed pytesseract and put the file location of the tesseract.exe in the first variable

# this project was mainly me trying to use OCR for practical purposes

# this program hasn't been trained, so can only recognise certain texts (like pycharm's segoe UI)


print('please wait')
from gtts import gTTS
import os
import pyautogui
import pytesseract
import mouse
import time
import keyboard
import translators as ts
from colorama import Fore
pytesseract.pytesseract.tesseract_cmd = 'C:/program files/Tesseract-OCR/tesseract.exe'
time.sleep(0.3)
try:
    from PIL import Image
except ImportError:
    import Image


mylist = []
click_list = []
j = 0


# shift to mark
def mark():
    while True:
        if keyboard.is_pressed("shift"):
            x, y = mouse.get_position()
            click_list.append(x)
            click_list.append(y)
            break


from_lang = input('what language are you translating from?: ')
to_lang = input('what language are you translating into?: ')

print('mark ready')
for i in range(2):
    mark()
    time.sleep(0.3)

im = pyautogui.screenshot(region=(click_list[0], click_list[1], click_list[2] - click_list[0], click_list[3] - click_list[1]))
print('converting to string')
text = pytesseract.image_to_string(im)
for letter in text:
    if letter.isalnum():
        mylist.append(str(letter))


#print(mylist)
#print(text)

translated = []
mess = text

translator = ts.google(mess, from_language=from_lang, to_language=to_lang)

a = translator.split()
print('\n', Fore.GREEN + mess)

x = 0
y = 30

while True:
    group = a[x:y]

    for i in range(30):

        b = group[i]
        print(Fore.LIGHTBLUE_EX + group[i], end=' ')
    print('\n')
    x += 30
    y += 30
