from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys
import os

os.system('cls')

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate',150)

speaker.say('Run the AI')
speaker.runAndWait()


def interduce():
    
    speaker.say('my name is Gideon')
    speaker.runAndWait()


def create_note():
    global recognizer

    speaker.say('What do you wish to write onto your note sir?')
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with sr.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say('choose a filename!')
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename,'w') as f:
                f.write(note)
                done = True
                speaker.say(f'Adding Note {filename} Has been done !')
                speaker.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I can't get what are you talking about , can you say it again sir?")
            speaker.runAndWait()

def hello():
    speaker.say('Hello my dear friend')
    speaker.runAndWait()

def bye():
    speaker.say('Good bye my dear friend')
    speaker.runAndWait()

def quit():
    speaker.say('See you soon sir')
    speaker.runAndWait()
    sys.exit(0)


mapping  = {
    "interducing": interduce,
    "greeting": hello,
    "bye": bye
}

assistant = GenericAssistant('mapping.json',intent_methods=mapping)
assistant.train_model()


while True:

    try:
        with sr.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()
            print(str(message))
            speaker.say('Copy That')
            speaker.runAndWait()

        assistant.request(message)
        
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()

