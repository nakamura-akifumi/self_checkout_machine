# coding: utf-8
from PyQt4 import QtGui, QtCore
from ui_checkout_window import Ui_checkout_window
from felica_walker import *
from enju_adapter import *


class CheckoutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(CheckoutWindow, self).__init__(parent)
        self.ui = Ui_checkout_window()
        self.ui.setupUi(self)

        self.model = None
        self.basket_id = None
        self.session_value = None
        self.table_data = []

        style_prop_title_bar = settings.app['style']['title_bar']
        style_prop_ok_button = settings.app['style']['ok_button']
        style_prop_cancel_button = settings.app['style']['cancel_button']

        self.ui.lblTitle.setStyleSheet("QLabel { " + style_prop_title_bar + " }")
        self.ui.btnOK.setStyleSheet("QPushButton { " + style_prop_ok_button + " }")
        self.ui.btnCancel.setStyleSheet("QPushButton { " + style_prop_cancel_button + " }")

        headers = ['書名', '所蔵情報ID', '返却期限']
        self.model = MyTableModel(self.table_data, headers, self)
        self.createTable()

        self.ui.item_identifier.returnPressed.connect(self.enterkey_item_identifier)
        self.ui.btnCancel.clicked.connect(self.clicked_btnCancel)
        self.ui.btnOK.clicked.connect(self.clicked_btnOk)
        self.walker = FelicaWalker()
        self.walker.sig_fetch_cardid.connect(self.fetch_cardid)
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

    def createTable(self):
        # create the view
        tv = self.ui.tableView

        # set the table model
        tv.setModel(self.model)

        # hide grid
        tv.setShowGrid(False)

        # hide vertical header
        tv.verticalHeader().setVisible(False)

        # set horizontal header properties
        hh = tv.horizontalHeader()
        hh.setStretchLastSection(False)

        tv.setColumnWidth(0, 340)
        tv.setColumnWidth(1, 200)
        tv.setColumnWidth(2, 120)

        # set row height
        nrows = len(self.table_data)
        for row in xrange(nrows):
            tv.setRowHeight(row, 18)

        return tv

    def enterkey_item_identifier(self):
        item_identifier = self.ui.item_identifier.text()
        logger.debug("enterkey pressed : @@1 id={}".format(item_identifier))

        if settings.app['run_mode'] == 'api':
            access_url = settings.app['api']['access_url']
            cert = settings.app['api']['cert']

            server_adapter = EnjuAdapter(access_url, cert)
            logger.debug("add item: {}".format(item_identifier))
            res = server_adapter.add_checkout_item(self.session_value, self.basket_id, item_identifier)

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

                if x['status'] == 523:  # invalid item
                    self.ui.status_label.setText("読み込んだ番号は不正です。正しい番号か確認ください")
                    self.ui.item_identifier.setText('')
                elif x['status'] == 422:
                    msg = x['message']
                    logger.info("xxx")
                    logger.info(msg)
                    self.ui.status_label.setText(msg)
                    self.ui.item_identifier.setText('')
                else:
                    self.ui.status_label.setText("エラーが発生しました。コード={} 番号={}".format(x['status'], item_identifier))
                    self.ui.item_identifier.setText('')

            else:
                data1 = results['results']
                if data1['status'] == 'ok':
                    item = []
                    item.append(data1['items'][0]['name'])
                    item.append(data1['items'][0]['item_identifier'])
                    item.append(data1['items'][0]['due_date'])

                    self.ui.tableView.model().beginInsertRows(QtCore.QModelIndex(), len(self.table_data), 1)
                    self.table_data.append(item)
                    self.ui.tableView.model().endInsertRows()

                    logger.debug("append success")
                else:
                    self.ui.status_label.setText("{}".format(data1['msg']))
                    self.ui.item_identifier.setText('')

        else:
            logger.debug("run mode is [slack]")

        self.ui.item_identifier.setText('')


    def clicked_btnOk(self):
        self.walker.stop()

        if settings.app['run_mode'] == 'api':
            access_url = settings.app['api']['access_url']
            cert = settings.app['api']['cert']

            self.ui.status_label.setText("貸出処理中です。")
            server_adapter = EnjuAdapter(access_url, cert)
            results = server_adapter.checkout(self.session_value, self.basket_id)

            if results.status_code == 500:
                self.ui.status_label.setText("サーバ側でエラーが発生しました。(500)")
                return

            self.model.removeRows(0, len(self.table_data))

            self.table_data = []
            self.basket_id = None
            self.session_value = None

            logger.debug("checkout: return")
            print results
        else:
            logger.debug("run mode is [slack]")

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
        self.basket_id = None
        self.session_value = None


    @QtCore.pyqtSlot(str)
    def fetch_cardid(self, tag_idm):
        logger.debug("fetch_cardid tag={}".format(tag_idm))
        self.ui.status_label.setText("tag idm: %s" % tag_idm)

        progress = QtGui.QProgressDialog("カード情報照会中", 'Cancel', 0, 100)
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.setAutoReset(True)
        progress.setAutoClose(True)
        progress.setMinimum(0)
        progress.setMaximum(100)
        progress.resize(200, 100)
        progress.setWindowTitle("カード情報照会中")
        progress.setCancelButton(None)
        progress.show()
        progress.setValue(0)
        QtGui.QApplication.processEvents()

        if settings.app['run_mode'] == 'api':
            access_url = settings.app['api']['access_url']
            cert = settings.app['api']['cert']

            server_adapter = EnjuAdapter(access_url, cert)
            logger.debug("send tag: {}".format(tag_idm))
            response = server_adapter.cardid2user_with_basket(tag_idm)
        else:
            logger.debug("run mode is [slack]")

        self.update_user_profile(response.text)

    @QtCore.pyqtSlot(str)
    def update_user_profile(self, jsonString):
        name = ''
        user_number = ''
        basket_id = ''
        self.basket_id = None
        self.session_value = None

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
            error = results['errors'][0]
            if error['status'] == '501':
                self.ui.status_label.setText("利用者情報に登録されていません")
            else:
                logger.error("error. status={} message={}".format(error['status'], error['message']))
                self.ui.status_label.setText("サーバでエラーが発生しました。({})".format(error['message']))
        else:
            result = results['results'][0]
            name = unicode(result['name'])
            user_number = unicode(result['user_number'])
            basket_id = unicode(result['basket_id'])
            session_value = unicode(result['session_value'])
            self.ui.status_label.setText("カードを読み取りました。")

        self.basket_id = basket_id
        self.session_value = session_value
        self.ui.profile_label.setText("%s" % name)
        self.ui.user_identifer.setText("%s" % user_number)
        logger.debug("basket_id={} session_value={}".format(self.basket_id, self.session_value))

        if self.basket_id:
            self.ui.item_identifier.setFocus()
        else:
            self.ui.user_identifer.setFocus()

    @QtCore.pyqtSlot()
    def finish_read(self):
        self.walker.wait()


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.headerdata)

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[col])
        return QtCore.QVariant()

    def removeRows(self, position, rows, parent = QtCore.QModelIndex):
        self.beginRemoveRows(QtCore.QModelIndex(), position, position + rows - 1)
        for i in range(rows):
            value = self.arraydata[position]
            self.arraydata.remove(value)

        self.endRemoveRows()

