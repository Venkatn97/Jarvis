import speech_recognition as sr
recognizer = sr.Recognizer()

def listen():
    """ Listen to microphone and return text"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source,timeout=10, phrase_time_limit=15)

    try:
        text = recognizer.recognize_google(audio)
        print(f"YOU:{text}")
        return text.lower()
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
    except sr.WaitTimeoutEror:
        return None
    