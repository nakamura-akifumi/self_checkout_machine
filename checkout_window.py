# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form/checkout_window.ui'
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

class Ui_checkout_window(object):
    def setupUi(self, checkout_window):
        checkout_window.setObjectName(_fromUtf8("checkout_window"))
        checkout_window.resize(640, 480)
        self.user_identifer = QtGui.QLineEdit(checkout_window)
        self.user_identifer.setGeometry(QtCore.QRect(200, 80, 341, 41))
        self.user_identifer.setObjectName(_fromUtf8("user_identifer"))
        self.item_identifier = QtGui.QLineEdit(checkout_window)
        self.item_identifier.setGeometry(QtCore.QRect(200, 180, 341, 41))
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.status_label = QtGui.QLabel(checkout_window)
        self.status_label.setGeometry(QtCore.QRect(70, 390, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.user_name = QtGui.QLabel(checkout_window)
        self.user_name.setGeometry(QtCore.QRect(20, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.user_name.setFont(font)
        self.user_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name.setObjectName(_fromUtf8("user_name"))
        self.btnReturn = QtGui.QPushButton(checkout_window)
        self.btnReturn.setGeometry(QtCore.QRect(560, 40, 81, 51))
        self.btnReturn.setObjectName(_fromUtf8("btnReturn"))
        self.user_name_2 = QtGui.QLabel(checkout_window)
        self.user_name_2.setGeometry(QtCore.QRect(20, 180, 161, 41))
        self.user_name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name_2.setObjectName(_fromUtf8("user_name_2"))
        self.profile_label = QtGui.QLabel(checkout_window)
        self.profile_label.setGeometry(QtCore.QRect(50, 130, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.profile_label.setFont(font)
        self.profile_label.setObjectName(_fromUtf8("profile_label"))
        self.status_label_3 = QtGui.QLabel(checkout_window)
        self.status_label_3.setGeometry(QtCore.QRect(0, 10, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.status_label_3.setFont(font)
        self.status_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label_3.setObjectName(_fromUtf8("status_label_3"))
        self.item_image = QtGui.QGraphicsView(checkout_window)
        self.item_image.setGeometry(QtCore.QRect(420, 260, 171, 111))
        self.item_image.setObjectName(_fromUtf8("item_image"))
        self.item_label = QtGui.QLabel(checkout_window)
        self.item_label.setGeometry(QtCore.QRect(90, 290, 251, 61))
        self.item_label.setObjectName(_fromUtf8("item_label"))
        self.btnCheckout = QtGui.QPushButton(checkout_window)
        self.btnCheckout.setGeometry(QtCore.QRect(300, 300, 81, 51))
        self.btnCheckout.setObjectName(_fromUtf8("btnCheckout"))

        self.retranslateUi(checkout_window)
        QtCore.QMetaObject.connectSlotsByName(checkout_window)

    def retranslateUi(self, checkout_window):
        checkout_window.setWindowTitle(_translate("checkout_window", "貸出", None))
        self.status_label.setText(_translate("checkout_window", "this is status label", None))
        self.user_name.setText(_translate("checkout_window", "利用者ID", None))
        self.btnReturn.setText(_translate("checkout_window", "戻る", None))
        self.user_name_2.setText(_translate("checkout_window", "所蔵ID", None))
        self.profile_label.setText(_translate("checkout_window", "this is profiles label", None))
        self.status_label_3.setText(_translate("checkout_window", "貸出", None))
        self.item_label.setText(_translate("checkout_window", "TextLabel", None))
        self.btnCheckout.setText(_translate("checkout_window", "貸出", None))

