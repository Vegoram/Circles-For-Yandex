import sys

from random import randint
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 949)
        MainWindow.setStyleSheet("background-color: rgb(216, 255, 241);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 830, 371, 31))
        self.radioButton.setStyleSheet("font: 14pt \"Uroob\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 880, 371, 31))
        self.radioButton_2.setStyleSheet("font: 14pt \"Uroob\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 880, 371, 41))
        self.pushButton.setStyleSheet("background-color: rgb(60, 121, 89);")
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 810, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 800, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 830, 371, 31))
        self.label.setStyleSheet("font: 14pt \"Uroob\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 781, 781))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Только жёлтые окружности"))
        self.radioButton_2.setText(_translate("MainWindow", "Окружности рандомного цвета"))
        self.pushButton.setText(_translate("MainWindow", " "))
        lbl = "<html><head/><body><p align=\"center\">Сгенерировать окружность</p></body></html>"
        self.label.setText(_translate("MainWindow", lbl))


class DrawerCircler(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons = QButtonGroup()
        self.buttons.addButton(self.radioButton)
        self.buttons.addButton(self.radioButton_2)
        self.circle_type = True
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton.clicked.connect(self.change_circles_type)
        self.radioButton_2.clicked.connect(self.change_circles_type)
        self.pushButton.clicked.connect(self.draw_circle)
        self.setWindowTitle('Две задачи в одной!')

    def change_circles_type(self):
        if self.sender().text() == 'Только жёлтые окружности':
            self.circle_type = True
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
        else:
            self.circle_type = False
            self.radioButton_2.setChecked(True)
            self.radioButton.setChecked(False)

    def draw_circle(self):
        circle = Image.new('RGB', (781, 781), (216, 255, 241))
        draw = ImageDraw.Draw(circle)
        diameter = randint(20, 780)
        gap = (780 - diameter) // 2
        if self.circle_type:
            draw.ellipse((gap, gap, gap + diameter, gap + diameter), fill=(253, 233, 16), outline=(0, 0, 0))
        else:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            draw.ellipse((gap, gap, gap + diameter, gap + diameter), fill=(r, g, b), outline=(0, 0, 0))
        self.a = ImageQt(circle)
        self.pixmap = QPixmap.fromImage(self.a)
        self.label_2.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawerCircler()
    ex.show()
    sys.exit(app.exec())
