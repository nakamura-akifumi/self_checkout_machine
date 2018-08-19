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
        checkout_window.resize(800, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(checkout_window.sizePolicy().hasHeightForWidth())
        checkout_window.setSizePolicy(sizePolicy)
        self.user_identifer = QtGui.QLineEdit(checkout_window)
        self.user_identifer.setGeometry(QtCore.QRect(170, 120, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.user_identifer.setFont(font)
        self.user_identifer.setObjectName(_fromUtf8("user_identifer"))
        self.item_identifier = QtGui.QLineEdit(checkout_window)
        self.item_identifier.setGeometry(QtCore.QRect(170, 170, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.item_identifier.setFont(font)
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.status_label = QtGui.QLabel(checkout_window)
        self.status_label.setGeometry(QtCore.QRect(10, 60, 780, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(22)
        self.status_label.setFont(font)
        self.status_label.setFrameShape(QtGui.QFrame.Box)
        self.status_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.status_label.setMidLineWidth(0)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.user_name = QtGui.QLabel(checkout_window)
        self.user_name.setGeometry(QtCore.QRect(59, 120, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(18)
        self.user_name.setFont(font)
        self.user_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name.setObjectName(_fromUtf8("user_name"))
        self.btnCancel = QtGui.QPushButton(checkout_window)
        self.btnCancel.setGeometry(QtCore.QRect(690, 0, 110, 58))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancel.setFont(font)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.user_name_2 = QtGui.QLabel(checkout_window)
        self.user_name_2.setGeometry(QtCore.QRect(70, 170, 80, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(18)
        self.user_name_2.setFont(font)
        self.user_name_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name_2.setObjectName(_fromUtf8("user_name_2"))
        self.profile_label = QtGui.QLabel(checkout_window)
        self.profile_label.setGeometry(QtCore.QRect(530, 122, 260, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(18)
        self.profile_label.setFont(font)
        self.profile_label.setFrameShape(QtGui.QFrame.Box)
        self.profile_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.profile_label.setObjectName(_fromUtf8("profile_label"))
        self.lblTitle = QtGui.QLabel(checkout_window)
        self.lblTitle.setGeometry(QtCore.QRect(0, 0, 800, 58))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(36)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.item_label = QtGui.QLabel(checkout_window)
        self.item_label.setGeometry(QtCore.QRect(530, 172, 260, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(18)
        self.item_label.setFont(font)
        self.item_label.setFrameShape(QtGui.QFrame.Box)
        self.item_label.setFrameShadow(QtGui.QFrame.Sunken)
        self.item_label.setObjectName(_fromUtf8("item_label"))
        self.btnOK = QtGui.QPushButton(checkout_window)
        self.btnOK.setGeometry(QtCore.QRect(260, 410, 280, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.btnOK.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(21)
        font.setBold(False)
        font.setWeight(50)
        self.btnOK.setFont(font)
        self.btnOK.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.tableView = QtGui.QTableView(checkout_window)
        self.tableView.setGeometry(QtCore.QRect(60, 240, 701, 161))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("TakaoGothic"))
        font.setPointSize(16)
        self.tableView.setFont(font)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.lblTitle.raise_()
        self.user_identifer.raise_()
        self.item_identifier.raise_()
        self.status_label.raise_()
        self.user_name.raise_()
        self.btnCancel.raise_()
        self.user_name_2.raise_()
        self.profile_label.raise_()
        self.item_label.raise_()
        self.btnOK.raise_()
        self.tableView.raise_()

        self.retranslateUi(checkout_window)
        QtCore.QMetaObject.connectSlotsByName(checkout_window)

    def retranslateUi(self, checkout_window):
        checkout_window.setWindowTitle(_translate("checkout_window", "貸出", None))
        self.status_label.setText(_translate("checkout_window", "１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０", None))
        self.user_name.setText(_translate("checkout_window", "利用者ID", None))
        self.btnCancel.setText(_translate("checkout_window", "キャンセル", None))
        self.user_name_2.setText(_translate("checkout_window", "所蔵ID", None))
        self.profile_label.setText(_translate("checkout_window", "this is profiles label", None))
        self.lblTitle.setText(_translate("checkout_window", "貸出", None))
        self.item_label.setText(_translate("checkout_window", "this is item label", None))
        self.btnOK.setText(_translate("checkout_window", "貸出する", None))

