import os
import webbrowser

# Drive_names = ['C','R','D','E','T']
# # music_dir = "G:\\Song"
# music_dir = "E:\MUSIC\русский"
# songs = os.listdir(f'{Drive_names[0]}:')
# os.startfile(f'{Drive_names[0]}:')
# # random = os.startfile(os.path.join(music_dir, songs[1]))
# print(songs)

# temp = webbrowser.open('C:')
# webbrowser.open('R:')

import psutil
from subprocess import PIPE

#How to open a process
# psutil.Popen(['R:'],stdout=PIPE)

#How to kill a process
TARGET = "telegram.exe"
# [process.kill() for process in psutil.process_iter() if process.name() == TARGET]

print(x for x in psutil.process_iter())