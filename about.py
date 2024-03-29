# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(514, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ip-phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(About)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 491, 321))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.plainTextEdit.setPlainText(_translate("About", "v1.0 - MVP (Minimum Viable Product)\n"
"Author: Mark Nigh\n"
"Please direct all inquires about this application to Mark Nigh at marknigh70@gmail.com\n"
"\n"
"Source Code to be distributed upon request.\n"
"\n"
"AXL Web Service is required to be activated on CUCM publisher.\n"
"\n"
"Create a new user and assign the \"Standard AXL API Acess\" role to the user. https://developer.cisco.com/docs/axl/#!authentication/authentication\n"
"\n"
"Before executing any queries, go to CUCM administration application web interface and download the AXL WSDL and place all documents within the same folder as this application. DO NOT change the names of the files. Here is the instructions on how to download the files. https://developer.cisco.com/docs/axl/#!download-the-axl-wsdl/download-the-axl-wsdl\n"
"\n"
"For Phone Registration, additional .wsdl must be placed within same folder as application. Go to https://<server>:8443/realtimeservice2/services/RISService70?wsdl. Select the text, create a text file and paste contents. Name file RISService70.wsdl. \n"
"\n"
"**Please Note. This application performs NO configuration changes. It only queries for configuratoin data within CUCM, CUC and CER but it is recommended that a new AXL user is created and used. Do not use the Administrator credentials. \n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
