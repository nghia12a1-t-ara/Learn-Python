# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddRegion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddConfig(object):
    def setupUi(self, AddConfig):
        AddConfig.setObjectName("AddConfig")
        AddConfig.resize(691, 397)
        self.textBrowser_8 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_8.setGeometry(QtCore.QRect(10, 270, 294, 41))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_2.setGeometry(QtCore.QRect(9, 76, 294, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 120, 294, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_6 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_6.setGeometry(QtCore.QRect(10, 170, 294, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.Combo_AccessRight = QtWidgets.QComboBox(AddConfig)
        self.Combo_AccessRight.setGeometry(QtCore.QRect(310, 270, 371, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Combo_AccessRight.setFont(font)
        self.Combo_AccessRight.setEditable(True)
        self.Combo_AccessRight.setIconSize(QtCore.QSize(40, 40))
        self.Combo_AccessRight.setObjectName("Combo_AccessRight")
        self.Combo_AccessRight.addItem("")
        self.Combo_AccessRight.addItem("")
        self.Combo_AccessRight.addItem("")
        self.RegionNumber = QtWidgets.QTextEdit(AddConfig)
        self.RegionNumber.setGeometry(QtCore.QRect(309, 76, 373, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.RegionNumber.setFont(font)
        self.RegionNumber.setObjectName("RegionNumber")
        self.textBrowser_5 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_5.setGeometry(QtCore.QRect(9, 9, 673, 61))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.Combo_MemTypes = QtWidgets.QComboBox(AddConfig)
        self.Combo_MemTypes.setGeometry(QtCore.QRect(310, 220, 373, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Combo_MemTypes.setFont(font)
        self.Combo_MemTypes.setEditable(True)
        self.Combo_MemTypes.setIconSize(QtCore.QSize(40, 40))
        self.Combo_MemTypes.setObjectName("Combo_MemTypes")
        self.Combo_MemTypes.addItem("")
        self.Combo_MemTypes.addItem("")
        self.Combo_MemTypes.addItem("")
        self.Combo_MemTypes.addItem("")
        self.textBrowser_10 = QtWidgets.QTextBrowser(AddConfig)
        self.textBrowser_10.setGeometry(QtCore.QRect(10, 220, 294, 41))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.Cancel = QtWidgets.QPushButton(AddConfig)
        self.Cancel.setGeometry(QtCore.QRect(310, 320, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setObjectName("Cancel")
        self.StartAddr = QtWidgets.QTextEdit(AddConfig)
        self.StartAddr.setGeometry(QtCore.QRect(310, 120, 373, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.StartAddr.setFont(font)
        self.StartAddr.setObjectName("StartAddr")
        self.EndAddr = QtWidgets.QTextEdit(AddConfig)
        self.EndAddr.setGeometry(QtCore.QRect(310, 170, 373, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.EndAddr.setFont(font)
        self.EndAddr.setObjectName("EndAddr")
        self.Accept = QtWidgets.QPushButton(AddConfig)
        self.Accept.setGeometry(QtCore.QRect(10, 320, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Accept.setFont(font)
        self.Accept.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Accept.setAutoFillBackground(False)
        self.Accept.setObjectName("Accept")

        self.retranslateUi(AddConfig)
        QtCore.QMetaObject.connectSlotsByName(AddConfig)

    def retranslateUi(self, AddConfig):
        _translate = QtCore.QCoreApplication.translate
        AddConfig.setWindowTitle(_translate("AddConfig", "Form"))
        self.textBrowser_8.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Access Rights</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Region Number</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Start Address</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">End Address</span></p></body></html>"))
        self.Combo_AccessRight.setItemText(0, _translate("AddConfig", "MPU_PRIV_UNPRIV_NONE"))
        self.Combo_AccessRight.setItemText(1, _translate("AddConfig", "MPU_PRIV_RWX_UNPRIV_RWX"))
        self.Combo_AccessRight.setItemText(2, _translate("AddConfig", "MPU_PRIV_R_UNPRIV_R"))
        self.RegionNumber.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#00aa00;\">Adding MPU Region</span></p></body></html>"))
        self.Combo_MemTypes.setItemText(0, _translate("AddConfig", "MPU_MEM_STRONG_ORDER"))
        self.Combo_MemTypes.setItemText(1, _translate("AddConfig", "MPU_MEM_DEVICE_SHARED"))
        self.Combo_MemTypes.setItemText(2, _translate("AddConfig", "MPU_MEM_NORMAL_IO_NO_CACHE"))
        self.Combo_MemTypes.setItemText(3, _translate("AddConfig", "MPU_MEM_NORMAL_CACHEABLE"))
        self.textBrowser_10.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Memory Types</span></p></body></html>"))
        self.Cancel.setText(_translate("AddConfig", "Cancel"))
        self.StartAddr.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.EndAddr.setHtml(_translate("AddConfig", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.Accept.setText(_translate("AddConfig", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddConfig = QtWidgets.QWidget()
    ui = Ui_AddConfig()
    ui.setupUi(AddConfig)
    AddConfig.show()
    sys.exit(app.exec_())
