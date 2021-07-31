import pyqtgraph as pg 
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *

version = "1.0.0"
win_title = "Terrain Data - {}", format(version)
# CREATE APP WINDOW
app = pg.mkQApp("")
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)
win.setWindowTitle("E")

win.show()

if __name__ == '__main__':
    pg.exec()