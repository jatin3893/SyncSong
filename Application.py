from PyQt4 import QtGui
from MainWindow import MainWindow
import sys

App = QtGui.QApplication(sys.argv)
window = MainWindow()
window.show()
App.exec_() 