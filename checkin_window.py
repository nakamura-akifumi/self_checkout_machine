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
        checkin_window.resize(640, 503)
        self.btnReturn = QtGui.QPushButton(checkin_window)
        self.btnReturn.setGeometry(QtCore.QRect(560, 50, 81, 51))
        self.btnReturn.setObjectName(_fromUtf8("btnReturn"))
        self.title_label = QtGui.QLabel(checkin_window)
        self.title_label.setGeometry(QtCore.QRect(0, 10, 641, 40))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.user_name_2 = QtGui.QLabel(checkin_window)
        self.user_name_2.setGeometry(QtCore.QRect(50, 140, 101, 41))
        self.user_name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name_2.setObjectName(_fromUtf8("user_name_2"))
        self.btnCheckin = QtGui.QPushButton(checkin_window)
        self.btnCheckin.setGeometry(QtCore.QRect(460, 360, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnCheckin.setFont(font)
        self.btnCheckin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnCheckin.setObjectName(_fromUtf8("btnCheckin"))
        self.status_label = QtGui.QLabel(checkin_window)
        self.status_label.setGeometry(QtCore.QRect(0, 440, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.item_identifier = QtGui.QLineEdit(checkin_window)
        self.item_identifier.setGeometry(QtCore.QRect(170, 140, 341, 41))
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.item_label = QtGui.QLabel(checkin_window)
        self.item_label.setGeometry(QtCore.QRect(50, 200, 561, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.item_label.setFont(font)
        self.item_label.setObjectName(_fromUtf8("item_label"))

        self.retranslateUi(checkin_window)
        QtCore.QMetaObject.connectSlotsByName(checkin_window)
        checkin_window.setTabOrder(self.item_identifier, self.btnCheckin)
        checkin_window.setTabOrder(self.btnCheckin, self.btnReturn)

    def retranslateUi(self, checkin_window):
        checkin_window.setWindowTitle(_translate("checkin_window", "返却", None))
        self.btnReturn.setText(_translate("checkin_window", "戻る", None))
        self.title_label.setText(_translate("checkin_window", "返却", None))
        self.user_name_2.setText(_translate("checkin_window", "所蔵ID", None))
        self.btnCheckin.setText(_translate("checkin_window", "返却実行", None))
        self.status_label.setText(_translate("checkin_window", "this is status label", None))
        self.item_label.setText(_translate("checkin_window", "this is item label", None))

