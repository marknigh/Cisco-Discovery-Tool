# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phone_registration_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PhoneRegistration(object):
    def setupUi(self, PhoneRegistration):
        PhoneRegistration.setObjectName("PhoneRegistration")
        PhoneRegistration.resize(561, 408)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/ip-phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PhoneRegistration.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(PhoneRegistration)
        self.centralwidget.setObjectName("centralwidget")
        self.Phone_Reg_View = QtWidgets.QTableView(self.centralwidget)
        self.Phone_Reg_View.setGeometry(QtCore.QRect(10, 10, 521, 341))
        self.Phone_Reg_View.setObjectName("Phone_Reg_View")
        PhoneRegistration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PhoneRegistration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.menubar.setObjectName("menubar")
        PhoneRegistration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PhoneRegistration)
        self.statusbar.setEnabled(False)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        PhoneRegistration.setStatusBar(self.statusbar)

        self.retranslateUi(PhoneRegistration)
        QtCore.QMetaObject.connectSlotsByName(PhoneRegistration)

    def retranslateUi(self, PhoneRegistration):
        _translate = QtCore.QCoreApplication.translate
        PhoneRegistration.setWindowTitle(_translate("PhoneRegistration", "Phone Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PhoneRegistration = QtWidgets.QMainWindow()
    ui = Ui_PhoneRegistration()
    ui.setupUi(PhoneRegistration)
    PhoneRegistration.show()
    sys.exit(app.exec_())