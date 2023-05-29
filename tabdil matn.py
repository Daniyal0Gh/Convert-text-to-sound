# install (pip install pyttsx3)
import pyttsx3

for i in range(10):
    text = input("chio bayad bgam ?")
    sound = pyttsx3.init()
    sound.setProperty('rate', 110)
    sound.say(text)
    sound.runAndWait()