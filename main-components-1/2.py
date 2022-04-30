# from PyQt5 import Qt
 

# class W(Qt.QMainWindow):
#     def __init__(self):
#         Qt.QMainWindow.__init__(self)
#         self.tab = Qt.QTabWidget()
#         self.setCentralWidget(self.tab)
 
#         self.btnOpen = Qt.QPushButton('Open')
#         self.btnOpen.clicked.connect(self.open)
#         self.statusBar().addWidget(self.btnOpen)
        
#         self.btnSave = Qt.QPushButton('Save')
#         self.btnSave.clicked.connect(self.save)
#         self.statusBar().addWidget(self.btnSave)
        
#         self.btnClose = Qt.QPushButton('Close')
#         self.btnClose.clicked.connect(self.close)
#         self.statusBar().addWidget(self.btnClose)

#     def open(self):
#         fname = Qt.QFileDialog.getOpenFileName()[0]
#         if not fname: return
#         with open(fname) as f:
#             txt = f.read()
#         idx = self.tab.addTab(Qt.QTextEdit(),fname)
#         self.tab.widget(idx).setPlainText(txt)
#         self.tab.setCurrentIndex(idx)

#     def save(self):
#         fname = Qt.QFileDialog.getSaveFileName()[0]
#         if not fname: return
#         txt = self.tab.currentWidget().toPlainText()
#         with open(fname,'w') as f:
#             f.write(txt)

#     def close(self):
#         idx = self.tab.currentIndex()
#         wgt = self.tab.widget(idx)
#         self.tab.removeTab(idx)
#         del wgt


# if __name__=="__main__":
#     app = Qt.QApplication([])
#     t = W()
#     t.resize(640,480)
#     t.show()
#     app.exec_()
