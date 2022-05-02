from PyQt6 import QtWidgets, QtCore, QtGui


app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle('Работа с изображениями')
window.resize(400, 250)

vbox = QtWidgets.QVBoxLayout()
label = QtWidgets.QLabel()
image = QtGui.QPixmap('1.jpeg')

label.setPixmap(image)
vbox.addWidget(label)


window.setLayout(vbox)
window.show()
app.exec()
