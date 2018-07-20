# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form/main_window.ui'
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
        self.btnCheckout.setGeometry(QtCore.QRect(40, 210, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btnCheckout.setFont(font)
        self.btnCheckout.setObjectName(_fromUtf8("btnCheckout"))
        self.btnCheckin = QtGui.QPushButton(main_window)
        self.btnCheckin.setGeometry(QtCore.QRect(330, 210, 271, 141))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btnCheckin.setFont(font)
        self.btnCheckin.setObjectName(_fromUtf8("btnCheckin"))
        self.label = QtGui.QLabel(main_window)
        self.label.setGeometry(QtCore.QRect(0, 10, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lblStatus = QtGui.QLabel(main_window)
        self.lblStatus.setGeometry(QtCore.QRect(0, 90, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "セルフ貸出機", None))
        self.btnCheckout.setText(_translate("main_window", "貸出", None))
        self.btnCheckin.setText(_translate("main_window", "返却", None))
        self.label.setText(_translate("main_window", "セルフ貸出返却機", None))
        self.lblStatus.setText(_translate("main_window", "選んでタッチしてください", None))

