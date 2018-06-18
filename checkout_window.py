# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_form/checkout_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import binascii
import nfc

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


class Walker(QtCore.QThread):

    sig_status = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Walker, self).__init__(parent)
        self.stopped = False
        self.mutex = QtCore.QMutex()

    def setup(self):
        self.stopped = False

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def run(self):
        clf = nfc.ContactlessFrontend('usb')
        try:
            clf.connect(rdwr={'on-connect': self.on_connect})
        finally:
            clf.close()

        self.stop()
        self.finished.emit()

    def on_connect(self, tag):
        print "touched"
        tag_idm = binascii.hexlify(tag.idm)
        print tag_idm

        self.sig_status.emit(tag_idm)
        return True


class Ui_checkout_window(object):
    def setupUi(self, checkout_window):
        checkout_window.setObjectName(_fromUtf8("checkout_window"))
        checkout_window.resize(640, 480)
        self.user_identifer = QtGui.QLineEdit(checkout_window)
        self.user_identifer.setGeometry(QtCore.QRect(140, 70, 341, 51))
        self.user_identifer.setObjectName(_fromUtf8("user_identifer"))
        self.item_identifier = QtGui.QLineEdit(checkout_window)
        self.item_identifier.setGeometry(QtCore.QRect(140, 210, 341, 51))
        self.item_identifier.setObjectName(_fromUtf8("item_identifier"))
        self.status_label = QtGui.QLabel(checkout_window)
        self.status_label.setGeometry(QtCore.QRect(130, 360, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.status_label.setFont(font)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.user_name = QtGui.QLabel(checkout_window)
        self.user_name.setGeometry(QtCore.QRect(140, 140, 341, 41))
        self.user_name.setObjectName(_fromUtf8("user_name"))

        self.retranslateUi(checkout_window)
        QtCore.QMetaObject.connectSlotsByName(checkout_window)

        # extend
        self.walker = Walker()
        self.walker.sig_status.connect(self.update_status)
        #self.walker.finished.connect(self.finish_search)

        self.walker.setup()
        self.walker.start()


    @QtCore.pyqtSlot(str)
    def update_status(self, tag_idm):
        self.status_label.setText("tag idm: %s" % tag_idm)

    def retranslateUi(self, checkout_window):
            checkout_window.setWindowTitle(_translate("checkout_window", "Dialog", None))
            self.status_label.setText(_translate("checkout_window", "this is status label", None))
            self.user_name.setText(_translate("checkout_window", "TextLabel", None))

