from PyQt6 import QtCore, QtWidgets
import time

class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.resize(300, 100)

	def resizeEvent(self, e):
		size = {"x": e.size().width(), "y": e.size().height()}
		print(size)
		QtWidgets.QWidget.resizeEvent(self, e)


if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MyWindow()
	window.show()
	app.exec()
