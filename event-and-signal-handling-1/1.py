from PyQt6 import QtWidgets,QtCore
import sys

class Test(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)

	@QtCore.pyqtSlot()
	def on_clicked(self):
		print('hello')


a = Test()
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Нажми меня')
button.clicked.connect(a.on_clicked)
button.show()
sys.exit(app.exec())
