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
pytesseract.pytesseract.tesseract_cmd = 'C:/program files/Tesseract-OCR/tesseract.exe'

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
    else:
        mylist.append(str(letter))


print(mylist)
print(text)

speak = ''
speak += text
language = 'en'
print('preparing audio')
myobj = gTTS(text=speak, lang=language, slow=False)
myobj.save("TTS_MP3_FILE.mp3")
os.system("TTS_MP3_FILE.mp3")
