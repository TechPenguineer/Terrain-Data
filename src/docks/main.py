import pyqtgraph as pg 
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np

from pyqtgraph.dockarea import *
def createDocks(area):
        d1 = Dock("Viewer", size=(600,500))    
        d2 = Dock("Console Dock", size=(300,200), closable=False)

        area.addDock(d1, 'top')
        area.addDock(d2, 'bottom')

