
#PyQt 6 Release 1
#Caleb Schear
#20250608-CS-PyQt6_Hello_World_1.py

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a Title for your Widget
        self.setWindowTitle("Hello World")

        #set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        my_label = qtw.QLabel("Hello World")
        self.layout().addWidget(my_label)

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

