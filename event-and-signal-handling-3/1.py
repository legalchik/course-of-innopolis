from PyQt6 import QtWidgets, QtCore


class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, id, parent=None):
        QtWidgets.QLineEdit.__init__(self, parent)
        self.id = id


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.resize(300, 100)

        self.button = QtWidgets.QPushButton('print')
        self.line = MyLineEdit(1)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.line)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

        self.button.clicked.connect(self.on_clicked)
        QtWidgets.QWidget.setTabOrder(self.line,  self.button)
        QtWidgets.QWidget.setTabOrder(self.button, self.line)


    def on_clicked(self):
        print(self.line.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
