from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pyaudio
import speech_recognition as sr
import googletrans
from googletrans import Translator
r = sr.Recognizer()
mic = sr.Microphone()
translator = Translator()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(772, 643)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_Translate = QPushButton(self.centralwidget)
        self.pushButton_Translate.setObjectName(u"pushButton_Translate")
        self.pushButton_Translate.setGeometry(QRect(340, 460, 85, 32))
        self.pushButton_Translate.setAutoDefault(True)
        self.pushButton_Translate.clicked.connect(self.clicked)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(340, 430, 85, 16))
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

        self.Drop_Language1 = QComboBox(self.widget1)
        self.Drop_Language1.setObjectName(u"Drop_Language1")

        self.horizontalLayout_2.addWidget(self.Drop_Language1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Drop_Language2 = QComboBox(self.widget1)
        self.Drop_Language2.setObjectName(u"Drop_Language2")

        self.horizontalLayout_2.addWidget(self.Drop_Language2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.label_3.setText("")

        self.add_languages()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
    # retranslateUi

    #def init_button(self):
        #self.pushButton_Translate.clicked.connect(self.clicked)

    
    def add_languages(self):
        for x in googletrans.LANGUAGES.values():
            self.Drop_Language1.addItem(x.capitalize())
            self.Drop_Language2.addItem(x.capitalize())
    
    def clicked(self):
        with mic as source:
            self.label_3.setText("One Second Please!")
            r.adjust_for_ambient_noise(source, duration=1)
            self.label_3.setText("Start Speaking!")
            audio = r.listen(source, timeout=10)
        #this code uses the microphone as the source for audio
        #write a debug for no audio heard (try & except)
        self.update()

        lang_text_1 = r.recognize_google(audio, language = "en")
        lang_text_2 = translator.translate(lang_text_1, src='en', dest='es')

        self.textEdit_1.setPlainText(lang_text_1)
        self.textEdit_2.setPlainText(lang_text_2)
        
    def update(self):
        self.label_3.adjustSize()

    #def translate(self):
        #text_1 = r.recognize_google(audio, language = "en")
        #text_2 = r.recognize_google(text_1, src='en', dest='es')
        #box 1
        #box 2

#englishtext = r.recognize_google(audio, language = "en")
#result = translator.translate(englishtext, src='en', dest='es')

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    UI_Window = Ui_MainWindow()
    UI_Window.setupUi(MainWindow)
    MainWindow.show()

    app.exec()

