#! /usr/bin/python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QSocketNotifier, SIGNAL
import os,sys

myfifor = "ctopyfifo"
myfifow = "pytocfifo"

class myguiapp(QWidget):
    def __init__(self):
      
        QWidget.__init__(self)
        
        self.w1label1=QLabel(self.trUtf8("Hello, world!"), self)
        self.w1label1.move(150,75)

	self.w1button1=QPushButton(self.trUtf8("Set coucou..."), self)
        self.w1button1.move(150,100)
        
        self.w1button2=QPushButton(self.trUtf8("Quit"), self)
        self.w1button2.move(150,175)

	self.connect(self.w1button1, SIGNAL("clicked()"), self.setw1label1)
	self.connect(self.w1button2, SIGNAL("clicked()"), qApp, SLOT("quit()"))
	
	self.fdr = os.open(myfifor, os.O_RDONLY)
	self.notifier_r = QSocketNotifier(self.fdr, QSocketNotifier.Read)
	self.connect(self.notifier_r, SIGNAL('activated(int)'), self.readAllData)
	
	self.w2=QWidget()
	self.w2.label1=QLabel(self.trUtf8("Salut, le monde!"), self.w2)
	self.w2.label1.setFixedWidth(100)
	self.w2.label1.move(150,75)
	  
	self.w2.button1=QPushButton(self.trUtf8("OK"), self.w2)
	self.w2.button1.move(150,175)
	  
	self.connect(self.w2.button1, SIGNAL("clicked()"), self.writeAllData)
	
    def setw1label1(self):
	self.w1label1.setText(self.trUtf8("coucou..."))

    def readAllData(self):
	bufferSize = 1024
	while True:
	  data = os.read(self.fdr, bufferSize)
	  if not data:
	    break	
	  self.w2.label1.setText(self.trUtf8(data))
	  self.w2.show()

    def writeAllData(self):
	  fdw = os.open(myfifow, os.O_WRONLY)
	  os.write(fdw, "Ok\0")
	  os.close(fdw)
	  self.w2.close()
          
