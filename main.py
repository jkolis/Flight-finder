from mainwindow import Ui_MainWindow
from PySide2 import QtWidgets, QtGui, QtCore

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

# import find_routes as fr
# import airport_data as apd
# import airlines_data as ald
#
# # testowe dane
# airport_weights_dic = dict(zip(list(apd.airport_rated)[3:14], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))
# airlines_weights_dic = dict(zip(list(ald.airlines_rated)[3:12], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# source = "Warsaw"
# dest = "Zaragoza"
#
# # print(fr.rate_sorted_paths(source, dest, airport_weights_dic, airlines_weights_dic))
# print(fr.get_sorted_paths(source, dest, airport_weights_dic, airlines_weights_dic))
