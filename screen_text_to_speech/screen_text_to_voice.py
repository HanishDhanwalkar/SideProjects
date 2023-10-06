import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
import pyautogui
from pynput import mouse
import pyttsx3
import time

time.sleep(0.5)
print("start now")

counter =0
lis= []

def on_click(x, y, button, pressed):
    global counter,lis
    if pressed:
        counter += 1
        lis.append((x,y))
        if counter >= 2:
            return False
    
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
listener=mouse.Listener(on_click=on_click)
listener.start()

# print(lis)

screenshot = pyautogui.screenshot(region=(lis[0][0],lis[0][1],abs(lis[1][0] - lis[0][0]) ,abs(lis[1][1]-lis[0][1])))
text = pytesseract.image_to_string(screenshot)

print(text)

engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(text)
