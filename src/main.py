# coding: utf-8
from PyQt4 import QtGui, QtCore
import sys
import main_window
import settings
from mylogger import get_logger


def main():
    logger = get_logger(__name__)
    logger.debug("start self_checkout_machine")

    settings.init()
#   print settings.app

    app = QtGui.QApplication(sys.argv)
    window = main_window.MainWindow()
    window.show()
    window.check_devices()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
