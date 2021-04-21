# livelaughlanguage

This project was designed to implement speech recognition code and use it transcribe and then translate that transcitption from any language you want into any other language. This project also uses PyQt5 to create a GUI where we make the implementation user friendly. There is also an autograder-type option where you can designate a word to seach search for in the transcribed text and count how many times that word was listed. 

Necessary Packages:
1. pyaudio
2. speech_recognition
3. sys
4. PyQt5 
    - PyQt5.QtCore import *
    - PyQt5.QtGui import *
    - PyQt5.QtWidgets import *
5. googletrans alpha release
    - specfically need: pip install googletrans==3.1.0a0

Instructions:
1. Run file from terminal main_translator.py
2. Once window pops up, select desired langauges from drop down menus
3. Click translate. Follow pop up windows instructions.
4. After you click count, input prompt for count is located in the terminal. Type in desired word to be counted.
5. Exit out of window when done
