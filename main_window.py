# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(640, 480)
        self.btnCheckout = QtGui.QPushButton(main_window)
        self.btnCheckout.setGeometry(QtCore.QRect(50, 160, 251, 131))
        self.btnCheckout.setObjectName(_fromUtf8("btnCheckout"))
        self.btnCheckin = QtGui.QPushButton(main_window)
        self.btnCheckin.setGeometry(QtCore.QRect(320, 160, 251, 131))
        self.btnCheckin.setObjectName(_fromUtf8("btnCheckin"))

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Form", None))
        self.btnCheckout.setText(_translate("main_window", "貸出", None))
        self.btnCheckin.setText(_translate("main_window", "返却", None))

