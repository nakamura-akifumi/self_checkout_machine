from PyQt4 import QtCore
import binascii
import nfc
import requests
import settings


class FelicaWalker(QtCore.QThread):

    sig_status = QtCore.pyqtSignal(str)
    sig_user_profile = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(FelicaWalker, self).__init__(parent)
        self.stopped = False
        self.mutex = QtCore.QMutex()

    def setup(self):
        self.stopped = False

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True
        self.finished.emit()

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

        access_url = settings.app['access_url']
        response = requests.post(access_url, data={'tag': tag_idm})
        print response.status_code
        print response.text

        self.sig_user_profile.emit(response.text)

        return True

