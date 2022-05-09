import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5583986079382','+5583987316537','+5583987390534','+5583994156448']


while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'Robo M1 iniciado', datetime.now().hour, datetime.now().minute +2)
    del contatos[0]
    time.sleep(30)
    keyboard.press_and_release('ctrl + w')