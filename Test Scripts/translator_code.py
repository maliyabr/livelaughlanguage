#importing Google Translate API
import googletrans

#create translator class
from googletrans import translator

translator = Translator()

#translator automatically translates from whatever language to english
#so for our speech recognition code this could be under the Spanish recognized audio 
result = translator.translate('whatever text to be translated here', src='the source language')

#this code translates from english to spanish
result = translator.translate('whatever text file here', src='en', dest ='es')
print(result.text)
