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
        # self.setFixedSize(400, 200)
        
        self.m_label=QLabel(self.trUtf8("Hello, world!"), self)
        self.m_label.move(150,75)

	self.m_bouton=QPushButton(self.trUtf8("Set coucou..."), self)
        self.m_bouton.move(150,100)
        
        self.m_bouton_quit=QPushButton(self.trUtf8("Quit"), self)
        self.m_bouton_quit.move(150,175)

	self.connect(self.m_bouton, SIGNAL("clicked()"), self.setlabel)
	self.connect(self.m_bouton_quit, SIGNAL("clicked()"), qApp, SLOT("quit()"))
	
	self.fd = os.open(myfifor, os.O_RDONLY)
	self.notifier = QSocketNotifier(self.fd, QSocketNotifier.Read)
	self.connect(self.notifier, SIGNAL('activated(int)'), self.readAllData)
	
	self.w=QWidget()
	self.w.m_label=QLabel(self.trUtf8("Salut, le monde!"), self.w)
	self.w.m_label.setFixedWidth(100)
        self.w.m_label.move(150,75)
	
    def setlabel(self):
	self.m_label.setText(self.trUtf8("coucou..."))

    def readAllData(self):
      bufferSize = 1024
      while True:
	data = os.read(self.fd, bufferSize)
	if not data:
	  break
	#self.w.m_label.setText(self.trUtf8(repr(data)))
	# self.repaint()
	
	self.w.m_label.setText(self.trUtf8(data))
	
	# self.w.m_label.setText(self.trUtf8("jazz jazz jazz *3"))
	self.w.show()
