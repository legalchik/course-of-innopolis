from PyQt6 import QtWidgets, QtCore
import sys


app = QtWidgets.QApplication(sys.argv)


window = QtWidgets.QWidget()
window.setWindowTitle('QSplitter')
window.resize(200, 200)

main = QtWidgets.QVBoxLayout()

button1 = QtWidgets.QPushButton('кнопка')
button2 = QtWidgets.QPushButton('кнопка')

main.addWidget(button1)
main.addWidget(button2)

splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Vertical)
label1 = QtWidgets.QLabel('Содержимое 1')
label2 = QtWidgets.QLabel('Содержимое 2')

label1.setFrameStyle(QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Shape.Box | QtWidgets.QFrame.Shadow.Plain)

splitter.addWidget(label1)
splitter.addWidget(label2)

main.addWidget(splitter)

window.setLayout(main)
window.show()
sys.exit(app.exec())
