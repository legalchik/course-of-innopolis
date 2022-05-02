import os, zipfile, sqlite3
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from qt_material import apply_stylesheet


conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)")
conn.close()


class AuthWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Регистрация')
        self.setWindowIcon(QIcon('res/icon.png'))
        vbox = QVBoxLayout()
        self.label = QLabel('Регистрация')
        self.hint = QLabel('Введите свои данные')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.button = QPushButton('Регистрация')
        self.button.clicked.connect(self.reg)
        vbox.addWidget(self.label)
        vbox.addWidget(self.hint)
        vbox.addWidget(self.username)
        vbox.addWidget(self.password)
        vbox.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.show()

    def reg(self):
        try:
            login = self.username.text()
            password = self.password.text()
            print(login, password, sep=':')
            if login != '' and password != '':
                conn = sqlite3.connect('test.db')
                cur = conn.cursor()
                cur.execute('INSERT INTO users VALUES(?, ?)', (login, password))
                conn.commit()
                self.hint.setText('succes')
            else:
                print('Поля не могут быть пустыми')
        except Exception as err:
            print(err)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Explorer")
    apply_stylesheet(app, theme='dark_blue.xml')
    auth = AuthWindow()
    app.exec()
