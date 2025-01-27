import pyaudio

# import LiveSpeech
from pocketsphinx import LiveSpeech



for phrase in LiveSpeech():
	print('Start to listen!')
	print(phrase)
else:
	print("Sorry! could not recognize what you said")


