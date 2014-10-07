from PyQt4 import QtGui
from SyncSongWidget import SyncSongWidget

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        _widget = SyncSongWidget()
        self.setCentralWidget(_widget)