import speech_recognition as speech_recognition
r = sr.Recognizer()
mic = sr.Microphone()
#this code imports speech_recognition and sets up the microphone

with mic as source:
    audio = r.listen(source)
    #this code uses the microphone as the source for audio
    
text = r.recognize_google(audio)
print(text)
#this code will put the audio into text and then print the words
