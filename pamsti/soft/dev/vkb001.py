#!/usr/bin/python

import sys,string
from PyQt4 import QtGui

keyblayout = string.ascii_lowercase + string.digits
letterref = 0

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

buttons = {}

for i in range(4):
    for j in range(10):
        # keep a reference to the buttons
        buttons[(i, j)] = QtGui.QPushButton(keyblayout[letterref%36])
        buttons[(i, j)].setFixedWidth(20)
        buttons[(i, j)].setFixedHeight(20)
        # add to the layout
        layout.addWidget(buttons[(i, j)], i, j)
        letterref+=1

widget.setLayout(layout)
widget.show()
sys.exit(app.exec_())


