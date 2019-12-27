from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import pyqtSlot
from random import randint
import sys

class Ui(QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('board1.ui', self)

        self.Score_1 = 0
        self.Score_2 = 0
        self.Step_1 = 0
        self.Step_2 = 0

        self.updateStep(1, self.Step_1)
        self.updateStep(2, self.Step_2)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Board Game")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))

        self.score_1.setText("SCORE_1: " + str(self.Score_1))
        self.score_2.setText("SCORE_2: " + str(self.Score_2))

        self.step_1.setText("STEP_1: " + str(self.Step_1))
        self.step_2.setText("STEP_2: " + str(self.Step_2))
        
        self.DICE_1.clicked.connect(self.button_clicked_1)
        self.DICE_2.clicked.connect(self.button_clicked_2)

    def updateStep(self, flag, step):
        player_1 = [self.b1_0,self.b1_1,self.b1_2,self.b1_3,self.b1_4,self.b1_5,
                    self.b1_6,self.b1_7,self.b1_8,self.b1_9,self.b1_10,self.b1_11,
                    self.b1_12,self.b1_13,self.b1_14,self.b1_15,self.b1_16,self.b1_17,
                    self.b1_18,self.b1_19,self.b1_20,self.b1_21]
        player_2 = [self.b2_0,self.b2_1,self.b2_2,self.b2_3,self.b2_4,self.b2_5,
                    self.b2_6,self.b2_7,self.b2_8,self.b2_9,self.b2_10,self.b2_11,
                    self.b2_12,self.b2_13,self.b2_14,self.b2_15,self.b2_16,self.b2_17,
                    self.b2_18,self.b2_19,self.b2_20,self.b2_21]
        
        if flag == 1:
            for button in player_1:
                button.hide()
            player_1[step].show()
        else:
            for button in player_2:
                button.hide()
            player_2[step].show()
        
        
    @pyqtSlot()
    def button_clicked_1(self):
        print("clicked_1")
        random = randint(1,6)

        self.Score_1 += random
        self.Step_1 += random

        if self.Step_1 > 21:
            self.Step_1 = 21
        if self.Step_1 == 4:
            self.Step_1 = 8
        if self.Step_1 == 12:
            self.Step_1 = 16
        
        self.updateStep(1, self.Step_1)

        self.score_1.setText("SCORE_1: " + str(self.Score_1))
        self.step_1.setText("STEP_1: " + str(self.Step_1))

    @pyqtSlot()
    def button_clicked_2(self):
        print("clicked_2")
        random = randint(1,6)

        self.Score_2 += random
        self.Step_2 += random

        if self.Step_2 > 21:
            self.Step_2 = 21
        if self.Step_2 == 4:
            self.Step_2 = 8
        if self.Step_2 == 12:
            self.Step_2 = 16
            
        self.updateStep(2, self.Step_2)

        self.score_2.setText("SCORE_2: " + str(self.Score_2))
        self.step_2.setText("STEP_2: " + str(self.Step_2))

def window():
    app = QApplication(sys.argv)
    win = Ui()
    win.show()
    sys.exit(app.exec_())

window()
