# Importing Required Libraries
import pyttsx3
import pyaudio
import speech_recognition as aa
import pywhatkit
import datetime
import wikipedia
import webbrowser
import urllib.parse

listener = aa.Recognizer()
machine = pyttsx3.init()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis',"")
                
                print(instruction)
            
    except:
        pass
    return instruction

def talk(text):
    machine.say(text)
machine.runAndWait()

def play_jarvis():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song_url = instruction.replace('play', '').strip()
        
        talk("Playing your song")
        pywhatkit.playonyt(song_url)
    
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time'+ time)  
    
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        talk("I am fine and how about you")

    elif 'what is your name' in instruction:
        talk('Jarvis, What can i do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is',"")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)

    else:
        talk('Please repeat the instruction')
        

play_jarvis()
