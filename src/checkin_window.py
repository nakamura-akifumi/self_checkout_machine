# coding: utf-8
from PyQt4 import QtGui
from ui_checkin_window import Ui_checkin_window
from felica_walker import *
import json
import settings

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class CheckinWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckinWindow, self).__init__(parent)
        self.ui = Ui_checkin_window()
        self.ui.setupUi(self)

        self.ui.item_identifier.returnPressed.connect(self.enterkey_item_identifier)

        self.ui.btnCancel.clicked.connect(self.clicked_btnCancel)
        self.ui.btnOk.clicked.connect(self.clicked_btnOk)
        self.ui.status_label.setText(_fromUtf8("返却物のバーコードを読み込んでください"))
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

    def goodShow(self):
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        brp = QtGui.QApplication.desktop().screenGeometry(screen).bottomRight()
        if brp.x() == (800-1) and brp.y() == (480-1):
            # for raspberry-pi 7inch touch-screen
            self.showFullScreen()
        else:
            self.show()

    def enterkey_item_identifier(self):
        item_identifier = self.ui.item_identifier.text()
        logger.debug("enterkey pressed : @@1 id={}".format(item_identifier))

        self.checkin_item(item_identifier)

    def clicked_btnCancel(self):
        self.window().close()

    def clicked_btnOk(self):
        item_identifier = self.ui.item_identifier.text()
        logger.debug("clicked_btnOk pressed : @@1 id={}".format(item_identifier))

        self.checkin_item(item_identifier)

    def checkin_item(self, item_identifier):
        self.ui.status_label.setText("返却処理中です。")

        if settings.app['run_mode'] == 'api':
            access_url = settings.app['api']['access_url']
            cert = settings.app['api']['cert']

            server_adapter = EnjuAdapter(access_url, cert)
            logger.debug("checkin item: {}".format(item_identifier))
            res = server_adapter.checkin(item_identifier)

            print res.text
            jsonString = res.text

            try:
                s = unicode(jsonString)
                results = json.loads(s)
            except ValueError as e:
                logger.error("args:{0}".format(e.args))
                logger.error("message:{0}".format(e.message))
                logger.error("{0}".format(e))
                self.ui.status_label.setText("サーバからの応答情報にエラーがありました。({})".format(e.args))
                return

            if results['status'] != '200' and results.has_key('errors'):
                x = results['errors'][0]
                if x['status'] == 623: # invalid item
                    self.ui.status_label.setText("読み込んだ番号は不正です。正しい番号か確認ください")
                    self.ui.item_identifier.setText('')
                else:
                    self.ui.status_label.setText("エラーが発生しました。コード={} 番号={}".format(x['status'], item_identifier))
                    self.ui.item_identifier.setText('')

            else:
                self.ui.status_label.setText("返却処理を行いました。")
                self.ui.item_identifier.setText('')

        else:
            logger.debug("run mode is [slack]")

