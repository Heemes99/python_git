from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRectF
import sys

from PyQt5 import uic


class Notebook(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setGeometry(400, 400, 500, 500)

        self.pushButton.clicked.connect(self.a)

        self.b = False

    def a(self):
        self.b = True
        self.repaint()

    def paintEvent(self, event):
        if not self.b:
            return
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 153))
        d = randint(5, 50)
        qp.drawEllipse(QRectF(randint(0, 399), randint(0, 399), d, d))
        qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Notebook()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
