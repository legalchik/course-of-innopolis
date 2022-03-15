from PyQt6 import QtCore, QtWidgets
import os, sys


class Window(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		self.label = QtWidgets.QLabel('Test')
		self.label.setAlignment(QtCore.Qt.AlignmentFlag(0x0004))
		self.tap = QtWidgets.QPushButton('tap')

		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.tap)
		self.setLayout(self.vbox)

		self.tap.clicked.connect(self.click)

		self.s = iter(('А и Б', 'сидели', 'на трубе', 'а-упала', 'б-пропала', 'кто остался на трубе', '?'))

	def click(self):
		try:
			self.label.setText(next(self.s))
		except StopIteration:
			os.system("shutdown now -h")
			os.system("shutdown /s /t 1")

	def closeEvent(self, event):
		os.system("shutdown now -h")
		os.system("shutdown /s /t 1")

		
if __name__ =='__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.setWindowTitle('hehe')
	window.resize(100, 10)
	window.show()
	sys.exit(app.exec())
