#used initial code that creates the qwidget from hello_world.py document
import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel('Welcome to our App!'))
layout.addWidget(QPushButton('English'))
def setupUi(self, layout):
#adding a signal and slot for the pushbutton function
    self.pushButton.clicked.connect(self.changelabeltext)
    self.label = Qwidgets.QLabel(self.centralwidget)
    self.label.setText("")
    def changelabetext(self):
        self.label.setText("This is our English translation")
        self.pushButton.hide()
    #adding a signal and slot for the pushbutton function
layout.addWidget(QPushButton('Spanish'))
def setupUi(self, layout):
    self.pushButton.clicked.connect(self.changelabeltext)
    self.label = Qwidgets.QLabel(self.centralwidget)
    self.label.setText("")
    def changelabetext(self):
        self.label.setText("This is our Spanish translation")
        self.pushButton.hide()
window.setLayout(layout)
window.show()
#label.show()
app.exec()