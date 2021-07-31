import pyqtgraph as pg 
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *
def createDock(area, dock_name, location , xSize, ySize, isClosable):
        
        dock_cus = Dock(dock_name, size=(xSize,ySize), closable=isClosable)
        area.addDock(dock_cus, location)


