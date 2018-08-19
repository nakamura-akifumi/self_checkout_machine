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
        checkin_window.resize(800, 480)
        self.btnCancel = QtGui.QPushButton(checkin_window)
        self.btnCancel.setGeometry(QtCore.QRect(690, 0, 110, 58))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.lblTitle = QtGui.QLabel(checkin_window)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 800, 58))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle.sizePolicy().hasHeightForWidth())
        self.lblTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.user_name_2 = QtGui.QLabel(checkin_window)
        self.user_name_2.setGeometry(QtCore.QRect(70, 120, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_name_2.setFont(font)
        self.user_name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name_2.setObjectName(_fromUtf8("user_name_2"))
        self.btnOk = QtGui.QPushButton(checkin_window)
        self.btnOk.setGeometry(QtCore.QRect(260, 410, 280, 60))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.btnOk.setFont(font)
        self.btnOk.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.status_label = QtGui.QLabel(checkin_window)
        self.status_label.setGeometry(QtCore.QRect(10, 60, 780, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.status_label.setFont(font)
        self.status_label.setFrameShape(QtGui.QFrame.Box)
        self.status_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.item_identifier = QtGui.QLineEdit(checkin_window)
        self.item_identifier.setGeometry(QtCore.QRect(170, 120, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.item_identifier.setFont(font)
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.item_label = QtGui.QLabel(checkin_window)
        self.item_label.setGeometry(QtCore.QRect(530, 122, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.item_label.setFont(font)
        self.item_label.setFrameShape(QtGui.QFrame.Box)
        self.item_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.item_label.setObjectName(_fromUtf8("item_label"))
        self.tableView = QtGui.QTableView(checkin_window)
        self.tableView.setGeometry(QtCore.QRect(60, 180, 701, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableView.setFont(font)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.lblTitle.raise_()
        self.btnCancel.raise_()
        self.user_name_2.raise_()
        self.btnOk.raise_()
        self.status_label.raise_()
        self.item_identifier.raise_()
        self.item_label.raise_()
        self.tableView.raise_()

        self.retranslateUi(checkin_window)
        QtCore.QMetaObject.connectSlotsByName(checkin_window)
        checkin_window.setTabOrder(self.item_identifier, self.btnOk)
        checkin_window.setTabOrder(self.btnOk, self.btnCancel)

    def retranslateUi(self, checkin_window):
        checkin_window.setWindowTitle(_translate("checkin_window", "返却", None))
        self.btnCancel.setText(_translate("checkin_window", "キャンセル", None))
        self.lblTitle.setText(_translate("checkin_window", "返却", None))
        self.user_name_2.setText(_translate("checkin_window", "所蔵ID", None))
        self.btnOk.setText(_translate("checkin_window", "返却する", None))
        self.status_label.setText(_translate("checkin_window", "１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０", None))
        self.item_label.setText(_translate("checkin_window", "this is item label", None))

