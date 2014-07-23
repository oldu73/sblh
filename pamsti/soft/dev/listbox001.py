from PyQt4 import QtGui, QtCore
import sys, os

class Dialog_01(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow,self).__init__()

        myQWidget = QtGui.QWidget()
        myBoxLayout = QtGui.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidget = QtGui.QListWidget()
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)

        for i in range(100):
            item=QtGui.QListWidgetItem()
            name='A'+'%04d'%i
            item.setText(name)                        
            self.listWidget.addItem(item) 

        myBoxLayout.addWidget(self.listWidget)      

        Button_01 = QtGui.QPushButton("Print Current Items")
        Button_01.clicked.connect(self.printCurrentItems)
        myBoxLayout.addWidget(Button_01)


    def printCurrentItems(self):
        print "Current Items are : ", self.listWidget.currentItem()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog_1 = Dialog_01()
    dialog_1.show()
    dialog_1.resize(720,480)
    sys.exit(app.exec_())