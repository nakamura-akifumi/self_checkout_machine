# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkin_window.ui'
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

class Ui_checkin_window(object):
    def setupUi(self, checkin_window):
        checkin_window.setObjectName(_fromUtf8("checkin_window"))
        checkin_window.resize(640, 480)
        self.item_identifier = QtGui.QTextEdit(checkin_window)
        self.item_identifier.setGeometry(QtCore.QRect(220, 90, 241, 51))
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.label = QtGui.QLabel(checkin_window)
        self.label.setGeometry(QtCore.QRect(100, 110, 60, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(checkin_window)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 60, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(checkin_window)
        QtCore.QMetaObject.connectSlotsByName(checkin_window)

    def retranslateUi(self, checkin_window):
        checkin_window.setWindowTitle(_translate("checkin_window", "Form", None))
        self.label.setText(_translate("checkin_window", "TextLabel", None))
        self.label_2.setText(_translate("checkin_window", "TextLabel", None))

