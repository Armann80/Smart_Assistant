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
from Module_Search import WikiPedia_Search
from tkinter import *
import urllib.request
from gtts import gTTS
import os
import playsound

###
#set property
   
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
###

###################################
# functions
clear = lambda: os.system('cls')

def store_file(method='zip',obj=[],file_name = 'test'):
    if method.lower() == 'zip':
        try:
            fp = open(file_name,'r+')
            json.dump(obj,fp,)
            
        except:
            with open(file_name,'w') as fp:
                json.dump(obj,fp)
    if method.lower() == 'extract':
        try:
            fp = open(file_name,'r')
            str_obj = json.load(fp)
            return str_obj
        except:
            pass      

def check_internet():
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except:
        return False
    
def play_music(query = ''):
    speak("copy that")
    # music_dir = "G:\\Song"
    music_dir = "E:\MUSIC\русский"
    songs = os.listdir(music_dir)
    random = os.startfile(os.path.join(music_dir, songs[1]))

def calculate(query = ''):
    app_id = "Wolframalpha api id"
    client = wolframalpha.Client(app_id)
    indx = query.lower().split().index('calculate')
    query = query.split()[indx + 1:]
    res = client.query(' '.join(query))
    answer = next(res.results).text
    print("The answer is " + answer)
    speak("The answer is " + answer)

def GUI_bot(text):
	gui = Tk()
	gui.title('Gidien')
	text_box = Entry(master=gui,font=('arial',20,'bold'),textvariable=text, bd= 30,insertwidth=4,bg='powder blue',justify='right').grid(columnspan=4)
	gui.mainloop()

def speak(audio,lang = 'en'):
	# if check_internet:
	# 	myobj = gTTS(text=audio, lang=lang, slow=False)
	# 	myobj.save("temp.mp3")
	# 	playsound.playsound('temp.mp3', True)
	# 	os.remove('temp.mp3')
	# else:
		engine.say(audio)
		engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Captain !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Captain !")

	else:
		speak("Good Evening Captain !")

	assname = "Gidien"
	
def username():
	# speak("What should i call you sir")
	# uname = takeCommand()
	# speak(f"Welcome {uname}")
	# speak(uname)
	# columns = shutil.get_terminal_size().columns
	
	# print("#####################".center(columns))
	# print("Welcome Mr.", uname.center(columns))
	# print("#####################".center(columns))
	
	speak("How can I Help you Captain?")

def listening():
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		while True:
			try:
				print("Listening...")
				r.pause_threshold = 1
				audio = r.listen(source)
				query = r.recognize_google(audio, language ='en-in')
				if len(query)>0:
					print(query)
					break
			except:
				pass

	
	return query

def sendEmail(to, content,query):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()

def wikipedia_engine(query = ''):
	speak('what do you want to know captain ?')
	Key_word = takeCommand()
	list_search = wikipedia.search(Key_word)
	print(list_search)
	speak(f'Here is the related result about {Key_word} , tell me which one?')
	choosen = takeCommand()
	if choosen or choosen.lower() or choosen.capitalize() in list_search:
		index = list_search.index(choosen or choosen.lower() or choosen.capitalize())
		result = WikiPedia_Search(lang='en',links = list_search[index])
		speak('According to the wikipedia')
		clear()
		print(result)
		speak(result)

def Time(query = ''):
	strTime = datetime.datetime.now().strftime("%H:%M:%S")
	speak(f"Sir, the time is {strTime}")

def search(query = ''):
	query = query.replace("search", "")
	query = query.replace("play", "")		
	webbrowser.open(query)

def news(query = ''):
	try:
		jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
		data = json.load(jsonObj)
		i = 1
		
		speak('here are some top news from the times of india')
		print('''=============== TIMES OF INDIA ============'''+ '\n')
		
		for item in data['articles']:
			
			print(str(i) + '. ' + item['title'] + '\n')
			print(item['description'] + '\n')
			speak(str(i) + '. ' + item['title'] + '\n')
			i += 1
	except Exception as e:
		
		print(str(e))

def shutdown():
	speak("Hold On a Sec ! Your system is on its way to shut down")
	subprocess.call('shutdown / p /f')

def where_is(query = ''):
	query = query.replace("where is", "")
	location = query
	speak("User asked to Locate")
	speak(location)
	webbrowser.open("https://www.google.nl/maps/place/" + location + "")

def takeCommand():
	done = True
	r = sr.Recognizer()
	while done:
		
		try:
			query = listening()
			print(f"you said : {query}\n")
			return str(query)
		except :
			pass
		
###################################

commands = {
    "play music": play_music,
    'open youtube' and 'youtube': lambda : webbrowser.open("youtube.com"),
    'open google': webbrowser.open("google.com"),
    'time' : Time,
    'news' : news,
    'lock': lambda : ctypes.windll.user32.LockWorkStation,
	'restart' : lambda : subprocess.call(["shutdown", "/r"]),
	'hibernate' : lambda : subprocess.call("shutdown / h")

}


 







def Gidien():

	# L1
	clear()
	wishMe()
	username()
	
	
	#L2
	
	while True:
		try:
			query = takeCommand().lower()
			print(query)
			if query in commands:
				commands[query]()
		except Exception as e:
			speak("something Wrong!,let's start again")
			print(e)	
	

Gidien()