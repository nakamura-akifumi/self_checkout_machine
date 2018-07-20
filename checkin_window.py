# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form/checkin_window.ui'
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
        self.btnReturn = QtGui.QPushButton(checkin_window)
        self.btnReturn.setGeometry(QtCore.QRect(510, 30, 81, 51))
        self.btnReturn.setObjectName(_fromUtf8("btnReturn"))
        self.status_label_3 = QtGui.QLabel(checkin_window)
        self.status_label_3.setGeometry(QtCore.QRect(0, 1, 641, 40))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.status_label_3.setFont(font)
        self.status_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_3.setObjectName(_fromUtf8("status_label_3"))
        self.user_name_2 = QtGui.QLabel(checkin_window)
        self.user_name_2.setGeometry(QtCore.QRect(50, 120, 161, 41))
        self.user_name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name_2.setObjectName(_fromUtf8("user_name_2"))
        self.btnCheckin = QtGui.QPushButton(checkin_window)
        self.btnCheckin.setGeometry(QtCore.QRect(500, 330, 81, 51))
        self.btnCheckin.setObjectName(_fromUtf8("btnCheckin"))
        self.status_label = QtGui.QLabel(checkin_window)
        self.status_label.setGeometry(QtCore.QRect(150, 420, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.item_identifier = QtGui.QLineEdit(checkin_window)
        self.item_identifier.setGeometry(QtCore.QRect(220, 120, 341, 41))
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))

        self.retranslateUi(checkin_window)
        QtCore.QMetaObject.connectSlotsByName(checkin_window)

    def retranslateUi(self, checkin_window):
        checkin_window.setWindowTitle(_translate("checkin_window", "Form", None))
        self.btnReturn.setText(_translate("checkin_window", "戻る", None))
        self.status_label_3.setText(_translate("checkin_window", "返却", None))
        self.user_name_2.setText(_translate("checkin_window", "所蔵ID", None))
        self.btnCheckin.setText(_translate("checkin_window", "返却", None))
        self.status_label.setText(_translate("checkin_window", "this is status label", None))

