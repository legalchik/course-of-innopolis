import os, zipfile, sqlite3, random
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('res/icon.png'))
        vbox = QVBoxLayout()
        self.list_widget = QListWidget(self)
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)
        
        vbox.addWidget(self.list_widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.list_widget.clicked.connect(self.item_clicked)
        self.update_list()

    def update_list(self):
        cursor.execute("SELECT * FROM boo")
        data = cursor.fetchall()
        # print(data)
        for i, item in enumerate(data):
            print(item)
            self.list_widget.insertItem(i + 1, f"login: {item[0]}  password: {item[1]}")

    def item_clicked(self):
        self.list_widget.clear()
        self.update_list()


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS boo(login, password)")
cursor.execute("INSERT INTO boo VALUES(?, ?)", (f"LG{random.randrange(100)}", str(random.randrange(100000))))
cursor.execute("INSERT INTO boo VALUES(?, ?)", (f"LOGG{random.randrange(10)}", str(random.randrange(10000))))
conn.commit()


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Explorer")
    apply_stylesheet(app, theme='dark_blue.xml')
    window = MainWindow()
    window.show()
    app.exec()
