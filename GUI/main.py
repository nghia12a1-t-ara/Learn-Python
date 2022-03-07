import sys
import time, os

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from GPIO import Ui_MainWindow
from AddConfig import Ui_AddConfig
sys.path.insert(0, 'D:/Python/Python_Repo/Learn-Python/GUI/Backend')
from DataHandler import ReplaceCfg, GenerateFile

ConfigList = []     ## List to save all Configuration
tempConfig = {
        "Peripheral_Name" : "",
        "Peripheral" : "",
        "Pin_Number" : "",
        "GPIO_Mode" : "",
        "GPIO_Speed" : "",
        "GPIO_PuPd" : "",
        "GPIO_OType" : ""
    }
ConfigListName = list(tempConfig.keys())
tempList = []

#################################################################
################ Get PARAMETERS of Configuration ################
#################################################################
class ConfigWindow(QMainWindow, Ui_AddConfig):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.Combo_GPIOPort.activated[str].connect(self.SetupPort)
        self.Combo_GPIOPin.activated[str].connect(self.SetupPin)
        self.Combo_GPIOMode.activated[str].connect(self.SetupMode)
        self.Combo_GPIOSpeed.activated[str].connect(self.SetupSpeed)
        self.Combo_GPIOPuPd.activated[str].connect(self.SetupPuPd)
        self.Combo_GPIOOType.activated[str].connect(self.SetupOType)
        self.Accept.clicked.connect(self.ConfigAccept)
        self.Cancel.clicked.connect(self.ConfigReject)

    def ConfigAccept(self):
        GPIONameText = self.GPIOName.toPlainText()
        
        tempConfig["Peripheral_Name"] = GPIONameText
        tempConfig["Peripheral"] = ConfigWindow.SetupPort(self)
        tempConfig["Pin_Number"] = ConfigWindow.SetupPin(self)
        tempConfig["GPIO_Mode"] = ConfigWindow.SetupMode(self)
        tempConfig["GPIO_Speed"] = ConfigWindow.SetupSpeed(self)
        tempConfig["GPIO_PuPd"] = ConfigWindow.SetupPuPd(self)
        tempConfig["GPIO_OType"] = ConfigWindow.SetupOType(self)
        
        ListTemp = list(tempConfig.values())
        
        ConfigList.append(ListTemp)

        ### Show Configuration to Main Window ###
        win.ConfigView.addItem(ListTemp[0])

        ### Show List GPIO Name to ListWidgets ###
        print(len(ConfigList))
        win.ConfigView.show()
        
        ConfigWin.close()
        

    def ConfigReject(self):
        ConfigWin.close()
    
    def SetupPort(self):
        Port = self.Combo_GPIOPort.currentText()
        return Port
        
    def SetupPin(self):
        PinText = self.Combo_GPIOPin.currentText()
        return PinText

    def SetupMode(self):
        ModeText = self.Combo_GPIOMode.currentText()
        if ModeText == "Input Mode":
            Mode = "IN"
        elif ModeText == "Output Mode":
            Mode = "OUT"
        elif ModeText == "Alternate Function":
            Mode = "AF"
        elif ModeText == "Analog Mode":
            Mode = "AN"
        return Mode

    def SetupSpeed(self):
        SpeedText = self.Combo_GPIOSpeed.currentText()
        if SpeedText == 'Low Speed':
            Speed = 25
        elif SpeedText == 'Medium Speed':
            Speed = 50
        elif SpeedText == 'High Speed':
            Speed = 100
        elif SpeedText == 'Very High Speed':
            Speed = 150     
        return str(Speed)

    def SetupPuPd(self):
        PuPdText = self.Combo_GPIOPuPd.currentText()
        if PuPdText == "NO Pull":
            PuPd = "NOPULL"
        elif PuPdText == "Pull Up":
            PuPd = "UP"
        elif PuPdText == "Pull Down":
            PuPd = "DOWN"    
        return PuPd

    def SetupOType(self):
        OTypeText = self.Combo_GPIOOType.currentText()
        if OTypeText == "Push-Pull":
            OType = "PP"
        elif OTypeText == "Open-Drain":
            OType = "OD"    
        return OType

#################################################################
################## Main WINDOW for Show Config ##################
#################################################################
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        #self.addConfig.activated[str].connect(self.AddConfig)
        self.addConfig.clicked.connect(self.AddConfig)
        self.pushButton.clicked.connect(self.GenarateCode)
        self.toolButton.clicked.connect(self.FindFiles)
  
    def AddConfig(self):
        # Open Configuration Window
        ConfigWin.show()

    def FindFiles(self):
        ConfigPath = QFileDialog.getExistingDirectory()
        self.textEdit.setText(ConfigPath)
        tempList.append(ConfigPath)

    def GenarateCode(self):
        GenerateFile(tempList[0], ConfigList, ConfigListName)
        TIME_LIMIT = 100
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.001)
            self.GenProcess.setValue(count)

#################################################################
########################## MAIN FUNCTION ########################
#################################################################                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    ConfigWin = ConfigWindow()
    win.show()
    sys.exit(app.exec())
#################################################################
################################################################# 
