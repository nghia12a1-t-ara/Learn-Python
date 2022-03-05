import sys
import time, os

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from GPIO import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.comboBox.activated[str].connect(self.getBaudrate)
        self.comboBox_2.activated[str].connect(self.getDatasize)
        self.comboBox_3.activated[str].connect(self.getParity)
        self.pushButton.clicked.connect(self.GenarateCode)
        self.toolButton.clicked.connect(self.FindFiles)

    ###############################################################
    ################ Get PARAMETERS of Configuration ###############
    ###############################################################    
    def getBaudrate(self):
        strBaud = self.comboBox.currentText()
        Baudrate = int(strBaud)
        return Baudrate

    def getDatasize(self):
        strSize = self.comboBox_2.currentText()
        Datasize = int(strSize)
        return Datasize

    def getParity(self):
        Parity = self.comboBox_3.currentText()
        return Parity

    def GenarateCode(self):
        TIME_LIMIT = 100
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.1)
            self.GenProcess.setValue(count)

    def FindFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', r'D:/', 'Source File (*.c)') 
        self.textEdit.setText(fname[0])
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
