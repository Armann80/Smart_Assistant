import wikipedia
import pyttsx3
import tkinter
import requests
from bs4 import BeautifulSoup

# windows = tkinter.Tk()

# windows.size()
# windows.mainloop()

import os
os.system('cls')

Data = open('Data.txt',mode='r+',encoding = 'utf-8')
Data1 = open('Data1.txt',mode='r+',encoding = 'utf-8')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()




def WikiPedia_Search(lang='en',links='',):
	try:
		# Get Url
		links = links.replace(' ','_')
		links = requests.get(f'https://{lang}.wikipedia.org/wiki/{links}')
		

		soup = BeautifulSoup(links.content,'html.parser')

		# Extract Data
		content_info = soup.findAll('div',{'class':'mw-parser-output'})
		table_info = soup.find('table',{'class':'infobox biography vcard'})
		content_heads = soup.findAll('h2')
		

		# Convert to Text
		content_info_txt = BeautifulSoup(str(content_info),'html.parser').get_text()
		table_info_txt = BeautifulSoup(str(table_info),'html.parser').get_text()
		content_heads_txt = BeautifulSoup(str(content_heads),'html.parser').get_text()
		


		content_info_txt = content_info_txt.replace(table_info_txt,'')
		content_heads_txt_list = content_heads_txt.split(',')
	 

		# Delete Space for content_heads_txt_list
		for i in range(len(content_heads_txt_list)):
			content_heads_txt_list[i] = content_heads_txt_list[i][1:]

		# Split the Content by Heads
		master_dic = {}
		for i in range(len(content_heads_txt_list)):
			if content_heads_txt_list[i] + '\n' in content_info_txt:
				x = content_info_txt.find(content_heads_txt_list[i])
				if content_heads_txt_list[i+1] + '\n' in content_info_txt:
					y = content_info_txt.find(content_heads_txt_list[i+1])
				else:
					y = content_info_txt[x:].find('\n')

				master_dic[content_heads_txt_list[i]] = content_info_txt[x+len(content_heads_txt_list[i]):y-1]

		master_dic['summery'] = content_info_txt[0:content_info_txt.find(content_heads_txt_list[1])-1]

		return master_dic['summery']
	except Exception as e:
		print(f'Error {e} has accured')
