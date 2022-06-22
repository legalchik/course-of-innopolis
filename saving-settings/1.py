from PyQt6 import QtCore, QtWidgets
import sys


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.WindowType.Window)
        self.setWindowTitle('Использование ключей')
        self.settings = QtCore.QSettings('Python', 'Использование ключей')
        vbox = QtWidgets.QVBoxLayout()
        self.textLine = QtWidgets.QLineEdit(parent=self)
        vbox.addWidget(self.textLine)
        btnSave = QtWidgets.QPushButton('&Сохранить')
        vbox.addWidget(btnSave)
        self.setLayout(vbox)
        btnSave.clicked.connect(self.saveText)
        if self.settings.contains('Окно/Местоположение'):
            self.setGeometry(self.settings.value('Окно/Местоположение'))
        else:
            self.resize(200, 50)
        if self.settings.contains('Данные/Текст'):
            self.textLine.setText(self.settings.value('Данные/Текст'))

    def closeEvent(self, event):
        self.settings.beginGroup('Окно')
        self.settings.setValue('Местоположение', self.geometry())
        self.settings.endGroup()

    def saveText(self):
        self.settings.beginGroup('Данные')
        self.settings.setValue('Текст', self.textLine.text())
        self.settings.endGroup()


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
