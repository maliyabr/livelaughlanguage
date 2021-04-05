import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel('Welcome to our App!'))
layout.addWidget(QPushButton('English'))
layout.addWidget(QPushButton('Spanish'))
window.setLayout(layout)
window.show()
#label.show()
app.exec()
