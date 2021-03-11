# This Python file uses the following encoding: utf-8
import sys
import os
from time import sleep
from random import randint
from form import Ui_gui
from scalp import *
from bot import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile, QUrl


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

    def lfind(self, send, listprb, index):
        f = open ('used.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            if line == listprb[index]:
                return True
        for i in send:
            if i == listprb[index]:
                return True;
        return False

    def valid(self, x, i, low, high, tags, band):
        if x[i][4] == ' ':
            return False
        if band:
            for j in tags:
                if x[i][2].find(j) == -1:
                    return False
            return int(x[i][4]) >= low and int(x[i][4]) <= high
        else:
            for j in tags:
                if x[i][2].find(j) != -1:
                    return int(x[i][4]) >= low and int(x[i][4]) <= high;
            return False

    def createContest(self):
        contest_dur = self.ui.hoursBox.text() + ":" + self.ui.minutesBox.text() + ":" + self.ui.secondsBox.text()
        tags = []
        if self.ui.checkBox.isChecked():
            tags.append('implementation')
        if self.ui.checkBox_2.isChecked():
            tags.append('math')
        if self.ui.checkBox_3.isChecked():
            tags.append('greedy')
        if self.ui.checkBox_4.isChecked():
            tags.append('dp')
        if self.ui.checkBox_5.isChecked():
            tags.append('data structures')
        if self.ui.checkBox_6.isChecked():
            tags.append('brute force')
        if self.ui.checkBox_7.isChecked():
            tags.append('constructive algorithms')
        if self.ui.checkBox_8.isChecked():
            tags.append('graphs')
        if self.ui.checkBox_9.isChecked():
            tags.append('sortings')
        if self.ui.checkBox_10.isChecked():
            tags.append('binary search')
        if self.ui.checkBox_11.isChecked():
            tags.append('dfs and similar')
        if self.ui.checkBox_12.isChecked():
            tags.append('trees')
        if self.ui.checkBox_13.isChecked():
            tags.append('strings')
        if self.ui.checkBox_14.isChecked():
            tags.append('number theory')
        if self.ui.checkBox_15.isChecked():
            tags.append('combinatorics')
        if self.ui.checkBox_16.isChecked():
            tags.append('two pointers')
        if self.ui.checkBox_17.isChecked():
            tags.append('bitmasks')
        if self.ui.checkBox_18.isChecked():
            tags.append('geometry')
        if self.ui.checkBox_19.isChecked():
            tags.append('dsu')
        if self.ui.checkBox_20.isChecked():
            tags.append('probabilities')
        if self.ui.checkBox_21.isChecked():
            tags.append('shortest paths')
        if self.ui.checkBox_22.isChecked():
            tags.append('divide and conquer')
        if self.ui.checkBox_23.isChecked():
            tags.append('hashing')
        if self.ui.checkBox_24.isChecked():
            tags.append('games')
        if self.ui.checkBox_25.isChecked():
            tags.append('interactice')
        if self.ui.checkBox_26.isChecked():
            tags.append('flows')
        if self.ui.checkBox_27.isChecked():
            tags.append('matrices')
        if self.ui.checkBox_28.isChecked():
            tags.append('string suffix structures')
        if self.ui.checkBox_29.isChecked():
            tags.append('fft')
        if self.ui.checkBox_30.isChecked():
            tags.append('graph matchings')
        if self.ui.checkBox_31.isChecked():
            tags.append('ternary search')
        if self.ui.checkBox_32.isChecked():
            tags.append('meet-in-the-middle')
        if self.ui.checkBox_33.isChecked():
            tags.append('expression parsing')
        if self.ui.checkBox_34.isChecked():
            tags.append('2-sat')
        if self.ui.checkBox_35.isChecked():
            tags.append('chinese remainder theorem')
        if self.ui.checkBox_36.isChecked():
            tags.append('schedules')        

        listprb = []
        send = []

        f = open('problems.csv', 'r')
        lines = f.readlines()

        for i in lines:
            listprb.append(i.split(','))

        for i in range(len(listprb) - 1, -1, -1):
            if not(self.valid(listprb, i, int(self.ui.lowerBoundDiffBox.text()), int(self.ui.upperBoundDiffBox.text()), tags, self.ui.ANDcheck.isChecked())):
                del listprb[i]
        while len(send) != int(self.ui.numProbBox.text()):
            index = randint(0, len(listprb)-1)
            if self.lfind(send, listprb, index):
                continue
            else:
                send.append(listprb[index][0])
                with open('used.txt', 'a') as u:
                    u.write(listprb[index][0])
                    u.write('\n')
                    u.close()

        f.close()
        url = createVJudge(self.ui.titleTextEdit.toPlainText(), self.ui.passwordTextEdit.toPlainText(), contest_dur, send)
        text = '<a href="'
        text += url
        text += '">contest link</a>'
        self.ui.linkText.setText(text)


    def updateList(self):
        self.ui.createButton.setEnabled(False)
        max_page = getMaxPage()
        f = open('problems.csv', 'w', encoding="utf-8")
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
            val = True
        else:
            self.ui.selectAllButton.setText('Select All')
            val = False

        self.ui.checkBox.setChecked(val)
        self.ui.checkBox_2.setChecked(val)
        self.ui.checkBox_3.setChecked(val)
        self.ui.checkBox_4.setChecked(val)
        self.ui.checkBox_5.setChecked(val)
        self.ui.checkBox_6.setChecked(val)
        self.ui.checkBox_7.setChecked(val)
        self.ui.checkBox_8.setChecked(val)
        self.ui.checkBox_9.setChecked(val)
        self.ui.checkBox_10.setChecked(val)
        self.ui.checkBox_11.setChecked(val)
        self.ui.checkBox_12.setChecked(val)
        self.ui.checkBox_13.setChecked(val)
        self.ui.checkBox_14.setChecked(val)
        self.ui.checkBox_15.setChecked(val)
        self.ui.checkBox_16.setChecked(val)
        self.ui.checkBox_17.setChecked(val)
        self.ui.checkBox_18.setChecked(val)
        self.ui.checkBox_19.setChecked(val)
        self.ui.checkBox_20.setChecked(val)
        self.ui.checkBox_21.setChecked(val)
        self.ui.checkBox_22.setChecked(val)
        self.ui.checkBox_23.setChecked(val)
        self.ui.checkBox_24.setChecked(val)
        self.ui.checkBox_25.setChecked(val)
        self.ui.checkBox_26.setChecked(val)
        self.ui.checkBox_27.setChecked(val)
        self.ui.checkBox_28.setChecked(val)
        self.ui.checkBox_29.setChecked(val)
        self.ui.checkBox_30.setChecked(val)
        self.ui.checkBox_31.setChecked(val)
        self.ui.checkBox_32.setChecked(val)
        self.ui.checkBox_33.setChecked(val)
        self.ui.checkBox_34.setChecked(val)
        self.ui.checkBox_35.setChecked(val)
        self.ui.checkBox_36.setChecked(val)
        

if __name__ == "__main__":
    app = QApplication([])
    widget = gui()
    widget.show()
    sys.exit(app.exec_())
