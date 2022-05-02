import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from math import sqrt
from random import randrange, choice

class Example(QMainWindow):
    send = pyqtSignal(tuple)
    def __init__(self):
        super().__init__()
        self.initUI()
        
    @pyqtSlot()
    def initUI(self):
        self.setWindowTitle("Пример")
        self.setGeometry(888, 222, 152, 120)

        self.line_edit = QLineEdit(self)
        self.line_text = QTextBrowser(self)

        self.line_edit.setGeometry(0, 0, 150, 33)
        self.line_text.setGeometry(0, 66, 150, 33)

        self.button = QPushButton('Угадать', self)
        self.button.clicked.connect(self.btn)
        self.button.setGeometry(0, 33, 150, 33)

        self.line_edit.setText(str(randrange(10)))
        self.num = str(randrange(11))
        self.line_text.setText("Угадайте число 0-10")

    def btn(self):
        if self.line_edit.text() in self.num:
            self.line_text.setText("shutdown haha, угадали")
        else:
            self.line_text.setText(choice(["неверно", " не угадали", "пробуйте еще", "не попадаешь"]))
            self.line_edit.setText('')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(application.exec_())
