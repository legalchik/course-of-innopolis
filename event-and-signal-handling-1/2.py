from PyQt6 import QtWidgets,QtCore
import sys

class Test(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle('Блокировка и удаление обработчика')
		self.resize(300, 150)
		self.button1 = QtWidgets.QPushButton('Нажми меня')
		self.button2 = QtWidgets.QPushButton('Блокировать')
		self.button3 = QtWidgets.QPushButton('Разблокировать')
		self.button4 = QtWidgets.QPushButton('Удалить обработчик')
		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.button1)
		vbox.addWidget(self.button2)
		vbox.addWidget(self.button3)
		vbox.addWidget(self.button4)
		self.setLayout(vbox)
		self.button1.clicked.connect(self.on_clicked_button1)
		self.button2.clicked.connect(self.on_clicked_button2)
		self.button3.clicked.connect(self.on_clicked_button3)
		self.button4.clicked.connect(self.on_clicked_button4)

	@QtCore.pyqtSlot()
	def on_clicked_button1(self):
		print('apart')

	@QtCore.pyqtSlot()
	def on_clicked_button2(self):
		self.button1.blockSignals(True)
		self.button2.setEnabled(False)
		self.button3.setEnabled(True)

	@QtCore.pyqtSlot()
	def on_clicked_button3(self):
		self.button1.blockSignals(False)
		self.button2.setEnabled(True)
		self.button3.setEnabled(False)

	@QtCore.pyqtSlot()
	def on_clicked_button4(self):
		self.button1.clicked.disconnect(self.on_clicked_button1)
		self.button2.setEnabled(False)
		self.button3.setEnabled(False)
		self.button4.setEnabled(False)


app = QtWidgets.QApplication(sys.argv)
window = Test()
window.show()
sys.exit(app.exec())
