from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import io
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>687</width>
    <height>726</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="button">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>630</y>
     <width>261</width>
     <height>51</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>11</pointsize>
    </font>
   </property>
   <property name="text">
    <string> Push to create circle</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class CreateCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
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