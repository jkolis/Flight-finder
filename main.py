import sys

from mainwindow import Ui_MainWindow
from PySide2 import QtWidgets, QtGui, QtCore

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
