# Programme 03 - signaux et slots avec arguments
from PyQt4.QtCore import SIGNAL, SLOT
from PyQt4.QtGui import QApplication, QWidget,\
    QLineEdit, QLabel, QHBoxLayout
import sys
 
if __name__=='__main__':
    App = QApplication(sys.argv)
    Window = QWidget()
    Window.setWindowTitle("Arguments")
    Layout = QHBoxLayout(Window)
    Line = QLineEdit()
    Layout.addWidget(Line)
    Label = QLabel()
    Layout.addWidget(Label)
    Line.connect(Line, SIGNAL("textChanged(QString)"),\
        Label, SLOT("setText(QString)"))
    Window.show()
    App.exec_()