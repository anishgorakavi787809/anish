import speech_recognition as sr
import pyaudio
r  = sr.Recognizer()    
with sr.Microphone() as source:
    print("Say something")
    audio = r.listen(source)
    voice_data = r.recognize_google(audio)
    print(voice_data)