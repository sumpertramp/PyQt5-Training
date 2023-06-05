from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

import random as r

winner = [("Stone", "Scissors"), ("Paper", "Stone"), ("Scissors", "Paper")]
loser = [("Stone", "Paper"), ("Paper", "Scissors"), ("Scissors", "Paper")]

font = QFont("Comic Sans MS", 18)

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout(self)
        
        self.hbox1 = QHBoxLayout(self)
        self.hbox2 = QHBoxLayout(self)
        self.hbox3 = QHBoxLayout(self)

        self.tbutton1 = QToolButton()
        self.tbutton2 = QToolButton()
        self.tbutton3 = QToolButton()

        self.tbutton1.setText("Stone")
        self.tbutton2.setText("Paper")
        self.tbutton3.setText("Scissors")

        self.tbutton1.setFont(font)
        self.tbutton2.setFont(font)
        self.tbutton3.setFont(font)

        self.tbutton1.setMinimumSize(90,90)
        self.tbutton2.setMinimumSize(90,90)
        self.tbutton3.setMinimumSize(90,90)

        
        self.hbox1.addWidget(self.tbutton1)
        self.hbox1.addWidget(self.tbutton2)
        self.hbox1.addWidget(self.tbutton3)

        self.label_pc = QLabel("Computer:")
        self.label_pc.setAlignment(Qt.AlignCenter)
        self.label_pc.setFont(font)
        self.label_choose = QLabel("Choose:")
        self.label_choose.setAlignment(Qt.AlignCenter)
        self.label_choose.setFont(font)

        self.hbox2.addWidget(self.label_pc)
        self.hbox2.addWidget(self.label_choose)

        self.label_result = QLabel("Result:")
        self.label_result.setAlignment(Qt.AlignCenter)
        self.label_result.setFont(font)
        
        self.score1 = QLabel("0")
        self.score2 = QLabel("0")
        self.score1.setFrameShape(QFrame.Box)
        self.score2.setFrameShape(QFrame.Box)
        self.score1.setMaximumWidth(80)
        self.score2.setMaximumWidth(80)
        self.score1.setAlignment(Qt.AlignCenter)
        self.score2.setAlignment(Qt.AlignCenter)
        self.score1.setFont(font)
        self.score2.setFont(font)
        
        self.hbox3.addWidget(self.score1)
        self.hbox3.addWidget(self.score2)
        
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addWidget(self.label_result)
        self.vbox.addLayout(self.hbox3)
        
        self.resize(350, 250)
        self.show()

        self.tbutton1.clicked.connect(lambda: self.compare("Stone"))
        self.tbutton2.clicked.connect(lambda: self.compare("Paper"))
        self.tbutton3.clicked.connect(lambda: self.compare("Scissors"))
    
    def compare(self, choose):
        random_pc = r.choice(["Stone", "Paper", "Scissors"])
        #print(random_pc)
        choose_tuple = (choose, random_pc)

        if choose_tuple in winner:
            self.label_result.setText("You are winner!")
            self.score1.setText(str(int(self.score1.text())+1))
            self.label_result.setStyleSheet("color: blue;")
        elif choose_tuple in loser:
            self.label_result("You are lost!")
            self.score2.setText(str(int(self.score2.text())+1))
            self.label_result.setStyleSheet("color: red;")
        else:
            self.label_result.setText("Draw!")
            self.label_result.setStyleSheet("color: green;")        

app = QApplication([])
window = main()
app.exec()