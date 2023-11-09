import pyautogui, webbrowser
from time import sleep
webbrowser.open('https://web.whatsapp.com/send?phone=+573185832727')

sleep(65)
with open ('mensaje.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
