from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QCheckBox, QVBoxLayout, QPushButton, QMessageBox
import sys

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