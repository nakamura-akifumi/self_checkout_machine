# coding: utf-8
from PyQt4 import QtCore
import binascii
import nfc
from enju_adapter import *
from logging import getLogger
import settings

logger = getLogger(__name__)


class FelicaWalker(QtCore.QThread):
    sig_fetch_cardid = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(FelicaWalker, self).__init__(parent)
        self.stopped = False
        self.clf = None

    def setup(self):
        self.stopped = False
        self.clf = None

    def stop(self):
        logger.debug("@stop-1 felica_walker")
        if self.clf:
            logger.debug("@stop-20 clf felica_walker")
            self.clf.close()
            logger.debug("@stop-21 clf felica_walker")
            self.clf = None

        logger.debug("@stop-23 felica_walker")
        self.finished.emit()

        logger.debug("@stop-30 felica_walker")

    def run(self):
        logger.debug("@run-1 felica_walker")

        self.clf = nfc.ContactlessFrontend('usb')
        try:
            logger.debug("@run-10 felica_walker")
            self.clf.connect(rdwr={'on-connect': self.on_connect})
            logger.debug("@run-11 felica_walker")
        finally:
            if self.clf:
                self.clf.close()
                self.clf = None


        self.stop()
        self.finished.emit()

    def on_connect(self, tag):
        logger.debug("@on_connect-1 felica_walker")

        tag_idm = binascii.hexlify(tag.idm)

        logger.debug("touched: {}".format(tag_idm))

        self.sig_fetch_cardid.emit(tag_idm)

        return True

