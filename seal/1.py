from PyQt6 import QtWidgets, QtCore, QtGui, QtPrintSupport

app = QtWidgets.QApplication([])
printer = QtPrintSupport.QPrinter()
print(printer.isValid())
painter = QtGui.QPainter()
painter.begin(printer)
pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.GlobalColor.blue), 5, style=QtCore.Qt.PenStyle.DotLine)
painter.setPen(pen)
painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
painter.drawRect(0, 0, printer.width(), printer.height())
color = QtGui.QColor(QtCore.Qt.GlobalColor.yellow)
painter.setPen(QtGui.QPen(color))
painter.setBrush(QtGui.QBrush(color))
font = QtGui.QFont("Verdana", pointSize=42)
painter.setFont(font)

for _ in range(3):
    painter.drawText(10, printer.height() // 2 - 100, printer.width() - 20, 50,
                     QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.TextFlag.TextDontClip, "QPrinter")
    printer.setPageOrientation(QtGui.QPageLayout.Orientation.Landscape)
    printer.newPage()

painter.end()
