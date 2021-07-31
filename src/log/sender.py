import pyqtgraph as pg 
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.console
import numpy as np
from pyqtgraph.console import Console
from pyqtgraph.dockarea import *

def console_logger(dock):
    w2 = pg.console.ConsoleWidget()
    dock.addWidget(w2)
def console_sender(dock_widget):
    ...