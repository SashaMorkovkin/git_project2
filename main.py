from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic


class CreateCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def run(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x = random.randint(1, 350)
        qp.drawEllipse(200, 200, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flag_maker = CreateCircle()

    flag_maker.show()
    sys.exit(app.exec())