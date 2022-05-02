# import os.path

# from PyQt6.QtGui import *
# from PyQt6.QtWidgets import *
# from PyQt6.QtCore import *
# from PyQt6.QtPrintSupport import *


# class MainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setGeometry(100, 100, 600, 400)
#         layout = QVBoxLayout()
#         self.editor = QPlainTextEdit()
#         fixedfont = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
#         fixedfont.setPointSize(12)
#         self.editor.setFont(fixedfont)

#         self.path = None



#         layout.addWidget(self.editor)
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)
#         self.status = QStatusBar()
#         self.setStatusBar(self.status)
#         file_toolbar = QToolBar("File")
#         self.addToolBar(file_toolbar)
#         file_menu = self.menuBar().addMenu("&File")

#         open_file_action = QAction("Open file", self)
#         open_file_action.triggered.connect(self.file_open)
#         file_menu.addAction(open_file_action)
#         file_toolbar.addAction(open_file_action)

#         save_file_action = QAction("Save", self)
#         save_file_action.setStatusTip("Save current page")
#         save_file_action.triggered.connect(self.file_save)
#         file_menu.addAction(save_file_action)
#         file_toolbar.addAction(save_file_action)

#         saveas_file_action = QAction("Save As", self)
#         saveas_file_action.setStatusTip("Save current page to specified file")
#         saveas_file_action.triggered.connect(self.file_saveas)
#         file_menu.addAction(saveas_file_action)
#         file_toolbar.addAction(saveas_file_action)

#         print_action = QAction("Print", self)
#         print_action.setStatusTip("Print current page")
#         print_action.triggered.connect(self.file_print)
#         file_menu.addAction(print_action)
#         file_toolbar.addAction(print_action)

#         edit_toolbar = QToolBar("Edit")
#         self.addToolBar(edit_toolbar)
#         edit_menu = self.menuBar().addMenu("&Edit")

#         undo_action = QAction("Undo", self)
#         undo_action.setStatusTip("Undo last change")
#         undo_action.triggered.connect(self.editor.undo)
#         edit_menu.addAction(undo_action)
#         edit_toolbar.addAction(undo_action)

#         redo_action = QAction("Redo", self)
#         redo_action.setStatusTip("Redo last change")
#         redo_action.triggered.connect(self.editor.redo)
#         edit_menu.addAction(redo_action)
#         edit_toolbar.addAction(redo_action)

#         cut_action = QAction("Cut", self)
#         cut_action.setStatusTip("Cut selected text")
#         cut_action.triggered.connect(self.editor.cut)
#         edit_menu.addAction(cut_action)
#         edit_toolbar.addAction(cut_action)

#         copy_action = QAction("Copy", self)
#         copy_action.setStatusTip("Copy selected text")
#         copy_action.triggered.connect(self.editor.copy)
#         edit_menu.addAction(copy_action)
#         edit_toolbar.addAction(copy_action)

#         paste_action = QAction("Paste", self)
#         paste_action.setStatusTip("Paste from clipboard")
#         paste_action.triggered.connect(self.editor.paste)
#         edit_menu.addAction(paste_action)
#         edit_toolbar.addAction(paste_action)

#         select_action = QAction("Select all", self)
#         select_action.setStatusTip("Select all text")
#         select_action.triggered.connect(self.editor.selectAll)
#         edit_menu.addAction(select_action)
#         edit_toolbar.addAction(select_action)

#         wrap_action = QAction("Wrap text to window", self)
#         wrap_action.setStatusTip("Check to wrap text to window")
#         wrap_action.setCheckable(True)
#         wrap_action.setChecked(True)
#         wrap_action.triggered.connect(self.edit_toggle_wrap)
#         edit_menu.addAction(wrap_action)
#         edit_toolbar.addAction(wrap_action)

#         self.update_title()
#         self.show()

#     def dialog_critical(self, s):
#         dlg = QMessageBox(self)
#         dlg.setText(s)
#         dlg.setIcon(QMessageBox.Icon.Critical)
#         dlg.show()


#     def file_open(self):
#         path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
#         if path:
#             try:
#                 with open(path, 'r') as f:
#                     text = f.read()
#             except Exception as e:
#                 self.dialog_critical(str(e))
#             else:
#                 self.path = path
#                 self.editor.setPlainText(text)
#                 self.update_title()
#     def file_save(self):
#         if self.path is None:
#             return self.file_saveas()
#         self._save_to_path(self.path)

#     def file_saveas(self):
#         path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")
#         if not path:
#             return
#         self._save_to_path(path)

#     def _save_to_path(self, path):
#         text = self.editor.toPlainText()
#         try:
#             with open(path, 'w') as f:
#                 f.write(text)
#         except Exception as e:
#             self.dialog_critical(str(e))
#         else:
#             self.path = path
#             self.update_title()

#     def file_print(self):
#         dlg = QPrintDialog()
#         if dlg.exec():
#             self.editor.print(dlg.printer())
#     def update_title(self):
#         self.setWindowTitle('%s - PyQt6 Notepad' % (os.path.basename(self.path) if self.path else "Untitled"))

#     def edit_toggle_wrap(self):
#         if str(self.editor.lineWrapMode()) == 'LineWrapMode.WidgetWidth':
#             self.editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
#         else:
#             self.editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)



# if __name__ == '__main__':
#     app = QApplication([])
#     app.setApplicationName("PyQT6-Note")
#     window = MainWindow()
#     app.exec()


import os
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowOpacity(0.88)
        vbox = QVBoxLayout()
        
        # Menu
        self.menu = QMenuBar()
        file_menu = self.menuBar().addMenu('&File')
        zip_file_action = QAction('Zip', self)
        unzip_file_action = QAction('Unzip', self)
        exit_app = QAction('Exit', self)
        exit_app.triggered.connect(self.close)

        file_menu.addActions([zip_file_action, unzip_file_action, exit_app])

        selection_menu = self.menuBar().addMenu('&Selection')
        help_menu = self.menuBar().addMenu('&Help')
        about = QAction('About', self)
        help = QAction('Help', self)
        help_menu.addActions([about, help])

        self.list_widget = QListWidget(self)
        self.list_widget.move(0, 20)
        self.list_widget.resize(600, 380)

        vbox.addWidget(self.menu)
        vbox.addWidget(self.list_widget)
        self.setLayout(vbox)

        self.setStyleSheet('background-color: #323232; color:white')

        self.list_widget.clicked.connect(self.item_clicked)
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


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("Explorer")
    window = MainWindow()
    app.exec()
    