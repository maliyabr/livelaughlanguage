#import all necessary packages and libraries into the code before anything
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
import pyaudio
import speech_recognition as sr
import googletrans
from googletrans import Translator

r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()
pyqtRemoveInputHook() #supresses error message during countclick 

#Main Window Class
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 663)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_Translate = QPushButton(self.centralwidget)
        self.pushButton_Translate.setObjectName(u"pushButton_Translate")
        self.pushButton_Translate.setGeometry(QRect(340, 440, 85, 32))
        self.pushButton_Translate.setAutoDefault(True)
        self.pushButton_Translate.clicked.connect(self.clicked)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 150, 681, 261))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_1 = QTextEdit(self.widget)
        self.textEdit_1.setObjectName(u"textEdit_1")
        self.horizontalLayout.addWidget(self.textEdit_1)
        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.horizontalLayout.addWidget(self.textEdit_2)
        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 100, 681, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        self.horizontalLayout_2.addWidget(self.label)
        #Dropdown Original Language
        self.Drop_Language1 = QComboBox(self.widget1)
        self.Drop_Language1.setObjectName(u"Drop_Language1")
        self.horizontalLayout_2.addWidget(self.Drop_Language1)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        #Dropdown Translated Language
        self.Drop_Language2 = QComboBox(self.widget1)
        self.Drop_Language2.setObjectName(u"Drop_Language2")
        self.horizontalLayout_2.addWidget(self.Drop_Language2)
        #Count Keyword Button
        self.countButton = QPushButton(self.centralwidget)
        self.countButton.setObjectName(u"countButton")
        self.countButton.setGeometry(QRect(330, 470, 108, 32))
        self.countButton.setAutoDefault(True)
        self.countButton.clicked.connect(self.countclick)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        self.add_languages()

       #CSS Classes 
        self.centralwidget.setStyleSheet("""


        QComboBox {
            background-color: rgb(204, 230, 255);
        }

        QLabel {
            font-weight: bold;
            color: rgb(0, 51, 51);

        }

        QPushButton {
            font: bold;
            border: 2px solid black;
            border-radius: 4px;
            background-color: rgb(204, 230, 255);
            }
        """)
   
   
    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"The Big Brain Translator", None))
        self.pushButton_Translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
        self.countButton.setText(QCoreApplication.translate("MainWindow", u"Count Words", None))
    # retranslateUi
  
    
    #Languages using Google Translate
    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.Drop_Language1.addItem(x.capitalize())
            self.Drop_Language2.addItem(x.capitalize())
    
    #This is what occurs when the translate button is pushed
    def clicked(self):
        try:
            #this code uses the microphone as the source for audio
            with mic as source:
                msg = QMessageBox()
                msg.setText("Welcome to Our Translator!")
                x = msg.exec()
                #print("Welcome to Our Translator!")
                r.adjust_for_ambient_noise(source, duration=1)
                msg = QMessageBox()
                msg.setText("Press OK and speak now!")
                x = msg.exec()
                #print("Press OK and speak now!")
                audio = r.listen(source, timeout=10)
            lang_1 = self.Drop_Language1.currentText()
            lang_2 = self.Drop_Language2.currentText()
            self.lang_text_1 = r.recognize_google(audio)#, language = "en")
            self.lang_text_2 = translator.translate(self.lang_text_1, src=lang_1, dest=lang_2)
            self.textEdit_1.setPlainText(str(self.lang_text_1))
            self.textEdit_2.setPlainText(str(self.lang_text_2.text))
            print(self.lang_text_2.text)
        #Exception Handling
        except AttributeError: 
            msg = QMessageBox()
            msg.setText("Attribute Error!")
            x = msg.exec()
            #print("Attribute Error!")
        #other errors go here
        except Exception as e: 
            msg = QMessageBox()
            msg.setText("Unknown Error, try again!")
            x = msg.exec()
            #print("Unknown Error, try again!")
    
    #function for autograder
    def countclick(self):
        #Define microphone output as string (count for original language)
        string = str(self.lang_text_1)
        substring = input("Please enter a keyword in the original language\n")
        count = string.count(substring)
        #Print count for keyword
        c = QMessageBox()
        message = "The count for " + substring + " is:", count
        c.setText(str(message))
        x = c.exec()
        #print("The count for " + substring + " is:", count)


if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    UI_Window = Ui_MainWindow()
    UI_Window.setupUi(MainWindow)
    MainWindow.show()
    app.exec()

