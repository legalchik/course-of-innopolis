from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hehe")

        self.s = "5+5"
        self.button = QPushButton(self.s+'=')
        self.button.clicked.connect(self.clicked)
        self.setCentralWidget(self.button)

    def clicked(self):
        self.button.setText(self.s+'='+str(eval(self.s)))
        self.button.setEnabled(False)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec()
    