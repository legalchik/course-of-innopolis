from PyQt6 import QtCore, QtWidgets
import time

class MyWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.setWindowTitle("Timer")
		self.resize(200, 100)
		self.timer_id =0
		self.label = QtWidgets.QLabel("")
		self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

		self.button = QtWidgets.QPushButton("тык")

		vbox = QtWidgets.QVBoxLayout()
		vbox.addWidget(self.label)
		vbox.addWidget(self.button)

		self.setLayout(vbox)
		self.button.clicked.connect(self.on_clicked_button)

		self.n = 5

	def on_clicked_button(self):
		if self.timer_id == 0:
			self.timer_id = self.startTimer(1000)

	def timerEvent(self, event):
		self.label.setText(str(self.n))
		if self.n == 0:
			self.killTimer(self.timer_id)
			self.timer_id = 0
			self.button.setEnabled(False)

		self.n -= 1


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec())