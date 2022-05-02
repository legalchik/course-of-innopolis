import os
import zipfile
import sqlite3

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from qt_material import apply_stylesheet

class AuthWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Войти в систему')
        self.setWindowIcon(QIcon('res/icon.png'))
        vbox = QVBoxLayout()
        self.label = QLabel('Войти')
        self.hint = QLabel('Введите свои данные')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.button = QPushButton('Войти')
        self.button.clicked.connect(self.auth)
        vbox.addWidget(self.label)
        vbox.addWidget(self.hint)
        vbox.addWidget(self.username)
        vbox.addWidget(self.password)
        vbox.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
        self.show()

    def auth(self):
        try:
            login = self.username.text()
            password = self.password.text()
            print(login, password, sep=':')
            if login != '' and password != '':
                conn = sqlite3.connect('test.db')
                cur = conn.cursor()
                cur.execute(f'SELECT * FROM users WHERE username="{login}"')
                value = cur.fetchone()
                if value is None:
                    self.hint.setText('Данного пользователя  не существует')
                else:
                    # print(value[1])
                    if value[1] == password:
                        self.hide()
                        window.show()
                        # MainWindow.show(window)
                    else:
                        self.username.clear()
                        self.password.clear()
                        self.hint.setText('Не верно')
            else:
                print('Поля не могут быть пустыми')
        except Exception as err:
            print(err)




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('res/icon.png'))
        vbox = QVBoxLayout()
        # Menu
        self.menu = QMenuBar()
        file_menu = self.menuBar().addMenu('&File')
        zip_file_action = QAction(QIcon('res/zip.png'),'Zip', self)
        zip_file_action.triggered.connect(self.zip_file)
        unzip_file_action = QAction(QIcon('res/unzip.png'),'Unzip', self)
        unzip_file_action.triggered.connect(self.unzip_file)
        exit_app = QAction(QIcon('res/exit.png'),'Exit', self)
        exit_app.triggered.connect(self.close)

        file_menu.addActions([zip_file_action, unzip_file_action, exit_app])


        selection_menu = self.menuBar().addMenu('&Selection')

        help_menu = self.menuBar().addMenu('&Help')
        about = QAction('About', self)
        help = QAction('Help', self)
        help_menu.addActions([about, help])
        #ListWidget
        self.list_widget = QListWidget(self)
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)

        vbox.addWidget(self.menu)
        vbox.addWidget(self.list_widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.list_widget.doubleClicked.connect(self.item_clicked)
        self.update_list()

    def update_list(self):
        cur_dir = os.listdir()
        last_dir = '..'
        self.list_widget.insertItem(0,last_dir)
        for i, item in enumerate(cur_dir):
            self.list_widget.insertItem(i + 1, item)

    def item_clicked(self):
        path = os.path.abspath(os.getcwd())
        # print(path)
        item = self.list_widget.currentItem()
        # print(item.text())
        if item.text() == '..':
            os.chdir('..')
        elif os.path.isdir(item.text()):
            os.chdir(f'{path}\\{item.text()}')
        else:
            os.system(item.text())
        self.list_widget.clear()
        self.update_list()

    def zip_file(self):
        file = self.list_widget.currentItem().text()
        file_name = file.split('.')
        with zipfile.ZipFile(f'{file_name[0]}.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.write(file)
        self.list_widget.clear()
        self.update_list()

    def unzip_file(self):
        file = self.list_widget.currentItem().text()
        try:
            archive = zipfile.ZipFile(file, 'r')
            archive.extractall('.')
            archive.close()
            print('Готово')
        except:
            print('Error')
        self.list_widget.clear()
        self.update_list()

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Explorer")
    apply_stylesheet(app, theme='dark_blue.xml')
    auth = AuthWindow()
    window = MainWindow()
    app.exec()
