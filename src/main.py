# coding: utf-8
from PyQt4 import QtGui
import sys
from ui_main_window import Ui_main_window
from checkin_window import Ui_checkin_window
from checkout_window import Ui_checkout_window
from felica_walker import *
from enju_adapter import *
import settings
import nfc
from mylogger import get_logger


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
        self.checkin_window = CheckinWindow()
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
            logger.warn("Not find felica device (USB)")
            self.ui.lblStatus.setStyleSheet("QLabel { background-color : red; color : blue; }")
            self.ui.lblStatus.setText("IDカードリーダーが見つかりません。")


class Filter(QtCore.QObject):
    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # do custom stuff
            print 'focus out'

            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            return False

        return False


class CheckinWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckinWindow, self).__init__(parent)
        self.ui = Ui_checkin_window()
        self.ui.setupUi(self)

        #self._filter = Filter()

        self.ui.btnCancel.clicked.connect(self.clicked_btnCancel)
        self.ui.btnOk.clicked.connect(self.clicked_btnOk)
        #self.ui.item_identifier.installEventFilter(self._filter)
        self.ui.status_label.setText("返却物のバーコードを読み込んでください")
        self.ui.item_label.setText("")

        style_prop_title_bar = settings.app['style']['title_bar']
        style_prop_ok_button = settings.app['style']['ok_button']
        style_prop_cancel_button = settings.app['style']['cancel_button']

        self.ui.lblTitle.setStyleSheet("QLabel { " + style_prop_title_bar + " }")
        self.ui.btnOk.setStyleSheet("QPushButton { " + style_prop_ok_button + " }")
        self.ui.btnCancel.setStyleSheet("QPushButton { " + style_prop_cancel_button + " }")


        self.center

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def clicked_btnCancel(self):
        self.window().close()

    def clicked_btnOk(self):
        access_url = settings.app['access_url']
        cert = settings.app['cert']

        self.ui.status_label.setText("返却処理中です。")
        item_identifier = self.ui.item_identifier.text()
        server_adapter = EnjuAdapter(access_url, cert)
        results = server_adapter.checkin(item_identifier)
        logger.debug("checkin: return")
        print results

        self.ui.status_label.setText("返却処理を行いました。")


class CheckoutWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckoutWindow, self).__init__(parent)
        self.ui = Ui_checkout_window()
        self.ui.setupUi(self)

        style_prop_title_bar = settings.app['style']['title_bar']
        style_prop_ok_button = settings.app['style']['ok_button']
        style_prop_cancel_button = settings.app['style']['cancel_button']

        self.ui.lblTitle.setStyleSheet("QLabel { " + style_prop_title_bar + " }")
        self.ui.btnOK.setStyleSheet("QPushButton { " + style_prop_ok_button + " }")
        self.ui.btnCancel.setStyleSheet("QPushButton { " + style_prop_cancel_button + " }")

        self.ui.btnCancel.clicked.connect(self.clicked_btnCancel)
        self.ui.btnOK.clicked.connect(self.clicked_btnOk)
        self.walker = FelicaWalker()
        self.walker.sig_status.connect(self.update_status)
        self.walker.sig_user_profile.connect(self.update_user_profile)
        self.walker.finished.connect(self.finish_read)

        self.walker.setup()
        self.walker.start()

        self.update_status_init()

        self.center

    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def clicked_btnOk(self):
        self.walker.stop()

        access_url = settings.app['access_url']
        cert = settings.app['cert']

        self.ui.status_label.setText("貸出処理中です。")
        user_number = self.ui.user_identifer.text()
        item_identifier = self.ui.item_identifier.text()
        server_adapter = EnjuAdapter(access_url, cert)
        results = server_adapter.checkout(user_number, item_identifier)
        logger.debug("checkout: return")
        print results

        self.ui.status_label.setText("貸出処理を行いました。")
        self.ui.profile_label.setText("")

    def clicked_btnCancel(self):
        logger.debug("@1 clicked_btnReturn ")
        self.walker.stop()
        logger.debug("@3 clicked_btnReturn ")
        self.window().close()

    def update_status_init(self):
        self.ui.status_label.setText("IDカード(利用者カード)をかざしてください。")
        self.ui.profile_label.setText("")
        self.ui.item_label.setText("")

    @QtCore.pyqtSlot(str)
    def update_status(self, tag_idm):
        self.ui.status_label.setText("tag idm: %s" % tag_idm)

    @QtCore.pyqtSlot(str)
    def update_user_profile(self, jsonString):
        name = ''
        user_number = ''
        try:
            s = unicode(jsonString)
            results = json.loads(s)
        except ValueError as e:
            logger.error("args:{0}".format(e.args))
            logger.error("message:{0}".format(e.message))
            logger.error("{0}".format(e))
            self.ui.status_label.setText("サーバからの応答情報にエラーがありました。({})".format(e.args))
            return

        if results['status'] == 400 and len(results['errors']) > 0:
            error = results[0]
            if error['status'] == '501':
                self.ui.status_label.setText("利用者情報に登録されていません")
        else:
            result = results['results'][0]
            self.ui.status_label.setText("カードを読み取りました")
            name = unicode(result['name'])
            user_number = unicode(result['user_number'])

        self.ui.profile_label.setText("%s" % name)
        self.ui.user_identifer.setText("%s" % user_number)
        self.ui.item_identifier.setFocus()

    @QtCore.pyqtSlot()
    def finish_read(self):
        self.walker.wait()


def main():
    logger = get_logger(__name__)
    logger.debug("start self_checkout_machine")

    settings.init()
    #print settings.app

    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.check_devices()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
