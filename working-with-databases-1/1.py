import os, zipfile
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowIcon(QIcon('icon.png'))
        vbox = QVBoxLayout()
        # Menu
        self.menu = QMenuBar()
        file_menu = self.menuBar().addMenu('&File')
        zip_file_action = QAction(QIcon('zip.png'),'Zip', self)
        zip_file_action.triggered.connect(self.zip_file)
        unzip_file_action = QAction(QIcon('unzip.png'),'Unzip', self)
        unzip_file_action.triggered.connect(self.unzip_file)
        exit_app = QAction(QIcon('exit.png'),'Exit', self)
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
        self.show()
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
    window = MainWindow()
    app.exec()
