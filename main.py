from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(687, 726)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(210, 630, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button.setFont(font)
        self.button.setObjectName("button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button.setText(_translate("Form", " Push to create circle"))


class CreateCircle(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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