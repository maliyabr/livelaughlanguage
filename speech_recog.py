import speech_recognition as sr
import googletrans
from googletrans import Translator
r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()
#this code imports speech_recognition and sets up the microphone

with mic as source:
    print('One Second Please!')
    r.adjust_for_ambient_noise(source, duration=5) 
    print('Hey! We want to hear your voice! Say something :)')
    audio = r.listen(source, timeout=5)
    #this code uses the microphone as the source for audio
   
englishtext = r.recognize_google(audio, language = "en")
result = translator.translate(englishtext, src='en', dest='es')
print(englishtext)
print(result.text)
#this code will put the audio into text and then print the words
#it well then translate the english text to spanish
#then it will print both the english and spanish text


spanishtext = r.recognize_google(audio, language = "es")
result = translator.translate(spanishtext, src='es', dest='en')
print(spanishtext)
print(result.text)
#recognizes Spanish audio, specifically US Spanish
#it will then translate from spanish to english
#then it will print the spanish and english text

