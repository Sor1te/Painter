import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPolygonF, QPolygon
from PyQt6.QtCore import QPointF, QRectF, Qt
from random import randint

from UI import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.drawer(qp)
        # Завершаем рисование
        qp.end()

    def drawer(self, qp):
        try:
            size = randint(20, 100)
            qp.setBrush(QColor(255, 255, 0))
            qp.setPen(QColor(255, 255, 0))
            self.coor_mouse = [randint(1, 400), randint(1, 400)]
            qp.drawEllipse(QPointF(self.coor_mouse[0], self.coor_mouse[1]), size / 2, size / 2)

        except Exception:
            print('sdfjo')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
