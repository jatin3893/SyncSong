from PyQt4.uic import loadUi
from PyQt4.QtGui import QWidget, QFileDialog
from PyQt4.QtCore import pyqtSlot
from sys import exit
from shutil import copy

class SyncSongWidget(QWidget):
    
    def __init__(self, parent = None):
        super(SyncSongWidget, self).__init__(parent)
        self.Ui = loadUi('SyncSong.ui', self)
        
        self.Ui.SourceFileButton.clicked.connect(self.SourceFileButtonClicked)
        
        self.Ui.DestinationDirectoryButton.clicked.connect(self.DestinationDirectoryButtonClicked)

        self.Ui.ButtonBox.accepted.connect(self.Accepted)
        self.Ui.ButtonBox.rejected.connect(self.Rejected)

        self.Ui.SyncLimitAll.stateChanged.connect(self.SyncLimitAllStateChanged)

    @pyqtSlot()
    def SourceFileButtonClicked(self):
        print "Source File Button Clicked"
        _filename = QFileDialog().getOpenFileName()
        self.Ui.SourceFileLineEdit.setText(_filename)

    @pyqtSlot()
    def DestinationDirectoryButtonClicked(self):
        print "DestinationDirectoryButtonClicked"
        _directory = QFileDialog().getExistingDirectory()
        self.Ui.DestinationDirectoryLineEdit.setText(_directory)

    @pyqtSlot()
    def Accepted(self):
        print "Accepted"
        self.Ui.ButtonBox.setDisabled(True)
        from xml.dom.minidom import parse
        dom1 = parse(str(self.Ui.SourceFileLineEdit.text()))
        ChildList = dom1.childNodes[0].childNodes[0].childNodes

        copyCount = 0
        for node in ChildList:
            filename = node.childNodes[0].childNodes[0].toxml()
            filename = filename.replace("&amp;", "&")
            print "Copying: " + filename[7:]
            copy(filename[7:], str(self.Ui.DestinationDirectoryLineEdit.text()))
            copyCount = copyCount + 1
        print "Copying Complete!"
        self.Ui.ButtonBox.setEnabled(True)

    @pyqtSlot()
    def Rejected(self):
        print "Rejected"
        exit()

    @pyqtSlot(int)
    def SyncLimitAllStateChanged(self, state):
        print "Sync Limit All State Changed"
        if state == 2:
            self.Ui.SyncLimitCountSpinBox.setDisabled(True)
        elif state == 0:
            self.Ui.SyncLimitCountSpinBox.setEnabled(True)
