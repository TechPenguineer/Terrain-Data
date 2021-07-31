import pyqtgraph as pg 
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np
from docks.main import createDock
from pyqtgraph.dockarea import *

version = "1.0.0"
# CREATE APP WINDOW
app = pg.mkQApp("")
win = QtGui.QMainWindow()
area = DockArea()
win.setCentralWidget(area)
win.resize(1000,500)
win.setWindowTitle("Terrain Data - " + version)

def default_dock():
    createDock(area, "Viewer", 'top', 600, 400, False)
    createDock(area, "Console", 'bottom', 600, 200, False)
    createDock(area, "Controler", 'right', 200, 200, False)



win.showMaximized()
win.show()


if __name__ == '__main__':
    pg.exec()
    default_dock()