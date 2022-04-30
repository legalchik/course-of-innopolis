import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QGridLayout, QWidget


app = QApplication(sys.argv)


window = QWidget()

btn1, btn2, btn3 = QPushButton('x'), QPushButton('0'), QPushButton('0')

btn4, btn5, btn6 = QPushButton(' '), QPushButton('x'), QPushButton('0')

btn7, btn8, btn9 = QPushButton('x'), QPushButton('x'), QPushButton(' ')


layout = QGridLayout(window)

layout.addWidget(btn1,0,0)
layout.addWidget(btn2,0,1)
layout.addWidget(btn3,0,2)

layout.addWidget(btn4,1,0)
layout.addWidget(btn5,1,1)
layout.addWidget(btn6,1,2)

layout.addWidget(btn7,2,0)
layout.addWidget(btn8,2,1)
layout.addWidget(btn9,2,2)


def click():
	import os, time
	os.system("shutdown /s /t 10")
	time.sleep(2)
	os.system("shutdown -a")


btn1.clicked.connect(click)
btn2.clicked.connect(click)
btn3.clicked.connect(click)
btn4.clicked.connect(click)
btn5.clicked.connect(click)
btn6.clicked.connect(click)
btn7.clicked.connect(click)
btn8.clicked.connect(click)
btn9.clicked.connect(click)


window.show()
sys.exit(app.exec())
