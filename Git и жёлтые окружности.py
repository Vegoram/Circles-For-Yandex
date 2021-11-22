import sys

from random import randint
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup


class DrawerCircler(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("All_circles.ui", self)
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
