# coding: utf-8
from PyQt4 import QtCore, QtGui
import sys
import yaml
import os
from main_window import Ui_main_window
from checkin_window import Ui_checkin_window
from checkout_window import Ui_checkout_window
import binascii
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

    def other_windows(self, checkin_window, checkout_window):
        self.checkin_window = checkin_window
        self.checkout_window = checkout_window

    def open_checkin(self):
        self.checkin_window.show()

    def open_checkout(self):
        self.checkout_window.show()




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


def main():
    message_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'messages.yaml')
    with open(message_file) as stream:
        msg = yaml.load(stream)

    msg = msg['main']

    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    checkin = CheckinWindow()
    checkout = CheckoutWindow()
    w.checkin_window = checkin
    w.checkout_window = checkout
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
