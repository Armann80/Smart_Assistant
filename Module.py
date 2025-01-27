import os
import json
import urllib.request
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pypdf
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
# music_dir = "E:\MUSIC"
# songs = os.listdir(music_dir)
# print(songs)
# random = os.startfile(os.path.join(music_dir, songs[1]))

clear = lambda: os.system('cls')

def Clear_Space(string_A):
    new_str = ''
    for i in range(len(string_A)):
        if string_A[i] != ' ' or ',':
            new_str+=string_A[i]
    return new_str

def Similarity_percentage(string_A,string_B):
    string_A = string_A.lower()
    string_B = string_B.lower()
    len_A = len(string_A)
    len_B = len(string_B)
    string_A = Clear_Space(string_A)
    string_B = Clear_Space(string_B)

    def smaller():
        if len_A >= len_B:
            return string_B
        else:
            return string_A

    def greater():
        if len_A >= len_B:
            return string_A
        else:
            return string_B

    small_str = smaller()
    greater_str = greater()
    pe = 0
    
   
    for i in small_str:
        if i in greater_str:
            pe+=1

    res = (pe / ((len_A+len_B)/2)) * 100

    return res


import datetime

strTime = datetime.datetime.now().strftime("%H:%M:%S")
print(strTime)
