from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


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

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Translate.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select Language:", None))
    # retranslateUi

    #def init_button(self):
        #self.pushButton_Translate.clicked.connect(self.clicked)

    def clicked(self):
        self.label_3.setText("Start Speaking")
        self.update()

    def update(self):
        self.label_3.adjustSize()

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    UI_Window = Ui_MainWindow()
    UI_Window.setupUi(MainWindow)
    MainWindow.show()

    app.exec()

