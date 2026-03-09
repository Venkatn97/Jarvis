# core/voice_output.py
#This is Jarvis's mouth - converts text to speech


import pyttsx3

engine=pyttsx3.init()
voices = engine.getProperty('voices')



engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',165)
engine.setProperty('volume',1.0)

def speak(text):
    print(f"JARVIS;{text}")
    engine.say(text)
    engine.runAndWait()