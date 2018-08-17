# coding: utf-8
from PyQt4 import QtGui
from ui_main_window import Ui_main_window
import checkout_window
import checkin_window
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

        style_prop_title_bar = settings.app['style']['title_bar']
        style_prop_ok_button = settings.app['style']['ok_button']

        self.ui.lblTitle.setStyleSheet("QLabel { " + style_prop_title_bar + " }")
        self.ui.btnCheckin.setStyleSheet("QPushButton { " + style_prop_ok_button + " }")
        self.ui.btnCheckout.setStyleSheet("QPushButton { " + style_prop_ok_button + " }")

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def open_checkin(self):
        self.checkin_window = checkin_window.CheckinWindow()
        self.checkin_window.show()

    def open_checkout(self):
        self.checkout_window = checkout_window.CheckoutWindow()
        self.checkout_window.walker.start()
        self.checkout_window.show()

    def check_devices(self):
        try:
            clf = nfc.ContactlessFrontend('usb')
            clf.close()
        except IOError:
            logger.warn("Not find felica device (USB)")
            self.ui.lblStatus.setStyleSheet("QLabel { background-color : red; color : blue; }")
            self.ui.lblStatus.setText("IDカードリーダーが見つかりません。")
