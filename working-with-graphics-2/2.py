from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


def img():
	a, b, c, d = text1.text(), text2.text(), text3.text(), text4.text()
	image1 = image.copy(rect=QtCore.QRect(int(a), int(b), int(c), int(d)))
	image1.save('test.jpeg')


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle('Работа с изображениями')
window.resize(400, 250)

vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
image = QtGui.QPixmap('1.jpeg')
label.setPixmap(image)
vbox.addWidget(label)


text1 = QLineEdit()
text2 = QLineEdit()
text3 = QLineEdit()
text4 = QLineEdit()
button = QPushButton('save')

vbox.addWidget(text1)
vbox.addWidget(text2)
vbox.addWidget(text3)
vbox.addWidget(text4)
vbox.addWidget(button)

button.clicked.connect(img)


for el in (text1, text2, text3, text4):
	el.setText("50")

window.setLayout(vbox)
window.show()
app.exec()
