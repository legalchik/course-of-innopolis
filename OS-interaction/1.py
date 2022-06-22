import os
import sys
from PyQt6 import QtGui, QtCore, QtWidgets
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

basedir = os.path.dirname(__file__)
print(basedir)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Иконка')
        label = QtWidgets.QLabel('Мое приложение')
        label.setMargin(10)
        button = QtWidgets.QPushButton('Push')
        button.setIcon(QtGui.QIcon(os.path.join(basedir, '1.jpeg')))
        button.pressed.connect(self.close)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, '1.jpeg')))
    window = MyWindow()
    app.exec()
