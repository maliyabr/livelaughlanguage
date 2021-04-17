from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QVBoxLayout, QPushButton, QMessageBox
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() #oop is scary, i believe this sets up the window
        self.initUI() #this puts the ui (design of the window) into the window. drawing on the paper, paper is the window

    def initUI(self): #the ui set up of the window
        self.label = QtWidgets.QLabel(self) #sets up where the label is going to appear, in this case, win
        self.label.setText("Welcome!!") #what the label says
        self.label.move(200,10)

        self.label1 = QtWidgets.QLabel(self) #sets up where the label is going to appear, in this case, win
        self.label1.setText("Press the button to begin talking!") #what the label says
        self.label1.move(200,30)

        # add buttton options
        self.english = QtWidgets.QPushButton(win)
        self.english.setText("Start Talking")
        self.english.move(90,50)
        self.english.clicked.connect(clicked) #connect button click to the function clicked


def clicked():
    print('you clicked it!')

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    #win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(550, 200, 450, 450)
    win.setWindowTitle("The Big Brain Translator")
    
    label = QtWidgets.QLabel(win) #sets up where the label is going to appear, in this case, win
    label.setText("Welcome!!") #what the label says
    label.move(200,10)

    label1 = QtWidgets.QLabel(win) #sets up where the label is going to appear, in this case, win
    label1.setText("Press the button to begin talking!") #what the label says
    label1.move(200,30)

    # add buttton options
    english = QtWidgets.QPushButton(win)
    english.setText("Start Talking")
    english.move(90,50)
    english.clicked.connect(clicked) #connect button click to the function clicked

    win.show()
    sys.exit(app.exec_()) #exits and closes application when you x out

window()

# layout = QVBoxLayout()
# layout.addWidget(QLabel('Make the right choice:'))
# layout.addWidget(QCheckBox('Pee Pee'))
# layout.addWidget(QCheckBox('Poo Poo'))
# layout.addWidget(QPushButton('Submit'))
# window.setLayout(layout)
# window.show()
# app.exec()