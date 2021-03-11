# This Python file uses the following encoding: utf-8
import sys
import os
from test import Ui_gui
from scalp import *
from bot import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile


class gui(QWidget):
    def __init__(self):
        super(gui, self).__init__()
        self.ui = Ui_gui()
        self.ui.setupUi(self)
        self.ui.selectAllButton.clicked.connect(self.selectAll)
        self.ui.lowerBoundDiffBox.valueChanged['int'].connect(self.setMax)
        self.ui.upperBoundDiffBox.valueChanged['int'].connect(self.setMin)
        self.ui.updateListButton.clicked.connect(self.updateList)
        self.ui.createButton.clicked.connect(self.createContest)

    def createContest(self):
        createVJudge()

    def updateList(self):
        self.ui.createButton.setEnabled(False)
        max_page = getMaxPage()
        f = open('problems.csv', 'w')
        for i in range(1, max_page+1):
            self.ui.progressBar.setValue(i*100//max_page)
            update(f, i)
        f.close()
        self.ui.createButton.setEnabled(True)
        QtWidgets.QMessageBox.about(self, 'Success!', 'Done updating the problem list')

    def setMax(self, val):
        if val > self.ui.upperBoundDiffBox.value():
            self.ui.upperBoundDiffBox.setValue(val)

    def setMin(self, val):
        if val < self.ui.lowerBoundDiffBox.value():
            self.ui.lowerBoundDiffBox.setValue(val)
    
    def selectAll(self):
        if self.ui.selectAllButton.text() == 'Select All':
            self.ui.selectAllButton.setText('Unselect All')
        else:
            self.ui.selectAllButton.setText('Select All')

        self.ui.checkBox.toggle()
        self.ui.checkBox_2.toggle()
        self.ui.checkBox_3.toggle()
        self.ui.checkBox_4.toggle()
        self.ui.checkBox_5.toggle()
        self.ui.checkBox_6.toggle()
        self.ui.checkBox_7.toggle()
        self.ui.checkBox_8.toggle()
        self.ui.checkBox_9.toggle()
        self.ui.checkBox_10.toggle()
        self.ui.checkBox_11.toggle()
        self.ui.checkBox_12.toggle()
        self.ui.checkBox_13.toggle()
        self.ui.checkBox_14.toggle()
        self.ui.checkBox_15.toggle()
        self.ui.checkBox_16.toggle()
        self.ui.checkBox_17.toggle()
        self.ui.checkBox_18.toggle()
        self.ui.checkBox_19.toggle()
        self.ui.checkBox_20.toggle()
        self.ui.checkBox_21.toggle()
        self.ui.checkBox_22.toggle()
        self.ui.checkBox_23.toggle()
        self.ui.checkBox_24.toggle()
        self.ui.checkBox_25.toggle()
        self.ui.checkBox_26.toggle()
        self.ui.checkBox_27.toggle()
        self.ui.checkBox_28.toggle()
        self.ui.checkBox_29.toggle()
        self.ui.checkBox_30.toggle()
        self.ui.checkBox_31.toggle()
        self.ui.checkBox_32.toggle()
        self.ui.checkBox_33.toggle()
        self.ui.checkBox_34.toggle()
        self.ui.checkBox_35.toggle()
        self.ui.checkBox_36.toggle()
        

if __name__ == "__main__":
    app = QApplication([])
    widget = gui()
    widget.show()
    sys.exit(app.exec_())
