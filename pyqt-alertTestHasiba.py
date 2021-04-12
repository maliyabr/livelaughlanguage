from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QCheckBox, QVBoxLayout, QPushButton, QMessageBox
app = QApplication([])
window = QWidget
button = QPushButton('Answer 1')
alsoButton = QPushButton('Answer 2')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText("You're right!")
    alert.exec()
def on_button_clicked_also():
    alert = QMessageBox()
    alert.setText("You're wrong!")
    alert.exec()
button.clicked.connect(on_button_clicked)
alsoButton.clicked.connect(on_button_clicked_also)
button.show()
alsoButton.show()
app.exec()