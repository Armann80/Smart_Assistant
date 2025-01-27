from cgitb import text
from distutils.command.config import LANG_EXT
from tkinter.tix import Tk
from turtle import title
from typing import Counter
import googletrans
from tkinter import *
import speech_recognition as sr
import translate as tr
from playsound import playsound
A = sr.Recognizer()
import pyttsx3
import os
engine = pyttsx3.init()

Memory = open('memory.txt','r+',encoding='utf-8')
m_r = Memory.readlines()

print(m_r,type(m_r))

def get_speech():
    try:
        with sr.Microphone(device_index=0) as sourcr:
            reslut = A.listen(sourcr)
            mytext = A.recognize_google(reslut)
            print(mytext)
            return mytext
            
           

    except:
        print("Device could'n recognize your voice or we have internet problem")
        





def Robot():
    while True:
        engine.say('Im liston to you sir')
        engine.runAndWait()
        mytext=get_speech()
        
        if 'stop' in str(mytext):
            break
        if 'shutdown' or 'shut down' in str(mytext):
            engine.say('Are you sure?')
            engine.runAndWait()
            mytext=get_speech()
            if 'yes' or 'Yes' or 'do it' in str(mytext):
                os.system('Shutdown /r /t 2')
                engine.say('Good by sir')
                engine.runAndWait()


