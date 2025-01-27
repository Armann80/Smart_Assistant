
from gtts import gTTS
import os
import playsound

# The text that you want to convert to audio
#mytext = 'наша мечта - сделать счастливыми всех людей во всем мире'

mytext = 'Hallo'
mytext1 = 'wie geht es ihnen meine lieber,achsooooo'


a = 'Arman'

t = f'glad to see you captain {a}'

# Language in which you want to convert
language = 'de'


myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("1.mp3")
myobj = gTTS(text=mytext1, lang=language, slow=False)
myobj.save("2.mp3")
# playsound.playsound('welcome.mp3', True)
