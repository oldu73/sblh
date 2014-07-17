#! /usr/bin/python
#-*-coding: utf-8 -*-
import os,sys,MySQLdb
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QSocketNotifier, SIGNAL

myfifor = "ctopyfifo"
myfifow = "pytocfifo"

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="pamsti001")
cur1 = db.cursor()
cur2 = db.cursor()
cur3 = db.cursor()

projlist = None
readdata = None

class myguiapp(QWidget):
    def __init__(self):
	global projlist

        QWidget.__init__(self)

        self.w1label1=QLabel(self.trUtf8("pamsti001 sys running..."), self)
        self.w1label1.move(10,10)

        self.w1button2=QPushButton(self.trUtf8("Quit"), self)
        self.w1button2.move(150,175)

	self.connect(self.w1button2, SIGNAL("clicked()"), self.closeAll)
	
	self.fdr = os.open(myfifor, os.O_RDONLY)
	self.notifier_r = QSocketNotifier(self.fdr, QSocketNotifier.Read)
	self.connect(self.notifier_r, SIGNAL('activated(int)'), self.readAllData)
	
	self.w2=QWidget()
	self.w2.setMinimumWidth(400)
	self.w2.label1=QLabel(self.trUtf8("init wait..."), self.w2)
	self.w2.label1.setFixedWidth(150)
	self.w2.label1.move(150,75)
	  
	self.w2.button1=QPushButton(self.trUtf8("OK"), self.w2)
	self.w2.button1.move(150,175)
	
	self.w2.projcombo = QComboBox(self.w2)
	self.w2.projcombo.move(10,10)
	
	cur2.execute("SELECT projnumb,clientname,clientprojid,clientlocation FROM projdesc001")
	projlist = cur2.fetchall()
  
	for item1 in projlist:
	  tmpstr1 = ""
	  for item2 in item1:
	    tmpstr1 += item2.decode('latin-1').encode("utf-8") + " / "
	  self.w2.projcombo.addItem(self.trUtf8(tmpstr1))

	self.connect(self.w2.button1, SIGNAL("clicked()"), self.writeAllData)

    def readAllData(self):
	global readdata
	bufferSize = 1024
	while True:
	  data = os.read(self.fdr, bufferSize)
	  if not data:
	    break
	  readdata = self.trUtf8(data)
	  cur1.execute("SELECT firstname, lastname FROM person001 WHERE rfid = %s",readdata)
	  person = cur1.fetchone()
	  # person is a tuple
	  self.w2.label1.setText(self.trUtf8(str(person[0]) + " " + str(person[1])))  
	  self.w2.show()

    def writeAllData(self):
	global projlist,readdata
	fdw = os.open(myfifow, os.O_WRONLY)
	os.write(fdw, "Ok\0")
	os.close(fdw)

	try:
	  # Execute the SQL command
	  cur3.execute("INSERT INTO timeisup001(rfid,projnumb) VALUES('%s','%s')"%(readdata,self.trUtf8(projlist[self.w2.projcombo.currentIndex()][0])))
	  # Commit your changes in the database
	  db.commit()
	except:
	  # Rollback in case there is any error
	  db.rollback()

	self.w2.close()
          
    def closeAll(self):
	# Close all cursors
	cur1.close()
	cur2.close()
	cur3.close()	  
	# Close databases
	db.close()
	
	qApp.quit()


