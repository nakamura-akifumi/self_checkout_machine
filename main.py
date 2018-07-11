# coding: utf-8
from PyQt4 import QtCore, QtGui
import sys
import json
from main_window import Ui_main_window
from checkin_window import Ui_checkin_window
from checkout_window import Ui_checkout_window
from felica_walker import *
from enju_adapter import *
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

        desktop = QtGui.qApp.desktop()
        drect = desktop.availableGeometry()
        print( u'利用可能デスクトップの位置・大きさ : %s' % drect )

        #move(drect.topLeft());
        #self.ui.restoreGeometry(settings.value("myWidget/geometry").toByteArray());

    def open_checkin(self):
        self.checkin_window.show()

    def open_checkout(self):
        self.checkout_window = CheckoutWindow()
        self.checkout_window.walker.start()
        self.checkout_window.show()

    def check_devices(self):
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
        self.ui.btnCheckout.clicked.connect(self.clicked_btnCheckout)
        self.walker = FelicaWalker()
        self.walker.sig_status.connect(self.update_status)
        self.walker.sig_user_profile.connect(self.update_user_profile)
        self.walker.finished.connect(self.finish_read)



        self.walker.setup()
        self.walker.start()

        self.update_status_init()

    def clicked_btnCheckout(self):
        self.walker.stop()

        access_url = settings.app['access_url']
        cert = ""

        user_number = self.ui.user_identifer.text()
        item_identifier = self.ui.item_identifier.text()
        server_adapter = EnjuAdapter(access_url, cert)
        server_adapter.checkout(user_number, item_identifier)



    def clicked_btnReturn(self):
        self.walker.stop()
        self.close()

    def update_status_init(self):
        self.ui.status_label.setText("カードをかざしてください。")
        self.ui.profile_label.setText("")

    @QtCore.pyqtSlot(str)
    def update_status(self, tag_idm):
        self.ui.status_label.setText("tag idm: %s" % tag_idm)

    @QtCore.pyqtSlot(str)
    def update_user_profile(self, jsonString):
        s = unicode(jsonString)
        profile = json.loads(s)
        if profile['status'] == '404':
            self.ui.status_label.setText("利用者情報に登録されていません")
        else:
            self.ui.status_label.setText("カードを読み取りました")

        self.ui.profile_label.setText("%s" % profile['name'])
        self.ui.user_identifer.setText("%s" % profile['user_number'])
        self.ui.item_identifier.setFocus()

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
