from PyQt6 import QtWidgets, QtCore
import sys


app = QtWidgets.QApplication(sys.argv)


window = QtWidgets.QWidget()
window.setWindowTitle('QTabWidget')
window.resize(400, 100)

tab = QtWidgets.QTabWidget()
tab.addTab(QtWidgets.QLabel('Текст'), 'Вкладка &1')
tab.addTab(QtWidgets.QPushButton('Кнопка'), 'Вкладка &2')
tab.setCurrentIndex(0)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(tab)

window.setLayout(vbox)
window.show()
sys.exit(app.exec())
