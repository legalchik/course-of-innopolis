import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from math import sqrt


class Example(QMainWindow):
    send = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.initUI()
        
    @pyqtSlot()
    def initUI(self):
        self.setWindowTitle("Пример")
        self.setGeometry(888, 222, 475, 190)

        self.line_edit11 = QLineEdit(self)
        self.line_edit12 = QLineEdit(self)
        self.line_edit13 = QLineEdit(self)
        self.line_text1 = QTextBrowser(self)

        self.line_edit11.setGeometry(0, 0, 150, 33)
        self.line_edit12.setGeometry(0, 33, 150, 33)
        self.line_edit13.setGeometry(0, 66, 150, 33)
        self.line_text1.setGeometry(0, 132, 150, 55)

        self.button1 = QPushButton('Треугольник', self)


        self.line_edit21 = QLineEdit(self)
        self.line_edit22 = QLineEdit(self)
        self.line_text2 = QTextBrowser(self)

        self.line_edit21.setGeometry(160, 33, 150, 33)
        self.line_edit22.setGeometry(160, 66, 150, 33)
        self.line_text2.setGeometry(160, 132, 150, 55)

        self.button2 = QPushButton('Прямоугольник', self)

        
        self.line_edit31 = QLineEdit(self)
        self.line_text3 = QTextBrowser(self)

        self.line_edit31.setGeometry(320, 66, 150, 33)
        self.line_text3.setGeometry(320, 132, 150, 55)

        self.button3 = QPushButton('Квадрат', self)


        self.button1.clicked.connect(self.btn1)
        self.button1.setGeometry(0, 99, 150, 34)
        
        self.button2.clicked.connect(self.btn2)
        self.button2.setGeometry(160, 99, 150, 34)

        self.button3.clicked.connect(self.btn3)
        self.button3.setGeometry(320, 99, 150, 34)

        for el in (self.line_edit11, self.line_edit12, self.line_edit13, self.line_edit21, self.line_edit22, self.line_edit31):
        	el.setText("2")


    def btn1(self):
        a, b, c = int(self.line_edit11.text()), int(self.line_edit12.text()), int(self.line_edit13.text())
        p = a + b + c
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        self.line_text1.setText(f"площадь: {s} периметр: {p}")

    def btn2(self):
        a, b = int(self.line_edit21.text()), int(self.line_edit22.text())
        p = 2 * (a + b)
        s = a * b
        self.line_text2.setText(f"площадь: {s} периметр: {p}")

    def btn3(self):
        a = int(self.line_edit31.text())
        p = 4 * a
        s = a ** 2
        self.line_text3.setText(f"площадь: {s} периметр: {p}")

        
if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(application.exec_())
