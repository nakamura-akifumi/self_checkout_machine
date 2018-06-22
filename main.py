# coding: utf-8
from PyQt4 import QtCore, QtGui
import sys
import json
from main_window import Ui_main_window
from checkin_window import Ui_checkin_window
from checkout_window import Ui_checkout_window
from felica_walker import *
import settings
import nfc


class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.btnCheckin.clicked.connect(self.open_checkin)
        self.ui.btnCheckout.clicked.connect(self.open_checkout)
        self.checkin_window = self
        self.checkout_window = self
        self.felica_walker = FelicaWalker()

    def open_checkin(self):
        self.checkin_window.show()

    def open_checkout(self):
        self.checkout_window = CheckoutWindow()
        self.checkout_window.walker.start()
        self.checkout_window.show()

    def check_devices(self):
        #FelicaWalker()
        try:
            clf = nfc.ContactlessFrontend('usb')
            clf.close()
        except IOError:
            print "Not find felica device (USB)"
            self.ui.lblStatus.setStyleSheet("QLabel { background-color : red; color : blue; }")
            self.ui.lblStatus.setText("リーダーが見つかりません。")


class CheckinWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckinWindow, self).__init__(parent)
        self.ui = Ui_checkin_window()
        self.ui.setupUi(self)


class CheckoutWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckoutWindow, self).__init__(parent)
        self.ui = Ui_checkout_window()
        self.ui.setupUi(self)

        self.ui.btnReturn.clicked.connect(self.clicked_btnReturn)
        self.walker = FelicaWalker()
        self.walker.sig_status.connect(self.update_status)
        self.walker.sig_user_profile.connect(self.update_user_profile)
        self.walker.finished.connect(self.finish_read)

        self.walker.setup()
        self.walker.start()

    def clicked_btnReturn(self):
        self.walker.stop()
        self.close()

    @QtCore.pyqtSlot(str)
    def update_status(self, tag_idm):
        self.ui.status_label.setText("tag idm: %s" % tag_idm)

    @QtCore.pyqtSlot(str)
    def update_user_profile(self, jsonString):
        s = unicode(jsonString)
        profile = json.loads(s)
        self.ui.status_label.setText("%s" % profile['name'])

    @QtCore.pyqtSlot()
    def finish_read(self):
        self.walker.wait()

def main():
    settings.init()

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.check_devices()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
