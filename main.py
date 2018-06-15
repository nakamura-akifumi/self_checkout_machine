# coding: utf-8
from PyQt4 import QtCore, QtGui
import sys
import yaml
import os
from main_window import Ui_main_window
from checkin_window import Ui_checkin_window


class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.ui.btnCheckin.clicked.connect(self.sayHello)
        self.checkin_window = self

    def other_windows(self, checkin_window):
        self.checkin_window = checkin_window

    def sayHello(self):
        print "Hello, world"
        self.checkin_window.show()


class CheckinWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(CheckinWindow, self).__init__(parent)
        self.ui = Ui_checkin_window()
        self.ui.setupUi(self)

def main():
    message_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'messages.yaml')
    with open(message_file) as stream:
        msg = yaml.load(stream)

    msg = msg['main']

    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    checkin = CheckinWindow()
    w.checkin_window = checkin
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
