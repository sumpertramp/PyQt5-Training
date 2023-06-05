from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.label_name = QLabel("Name:", self)
        self.label_surname = QLabel("Surname:", self)
        self.label_age = QLabel("Age:", self)
        self.label_gender = QLabel("Gender:", self)
        self.label_number = QLabel("Phone Number", self)
        self.label_email = QLabel("E-mail", self)
        self.label_height = QLabel("Height", self)
        self.label_weight = QLabel("Weight", self)
        self.label_blood = QLabel("Blood type:", self)

        self.line_name = QLineEdit(self)
        self.line_surname = QLineEdit(self)
        self.line_age = QLineEdit(self)
        #self.line_gender = QLineEdit(self)
        self.line_number = QLineEdit(self)
        self.line_email = QLineEdit(self)
        self.line_heigh = QLineEdit(self)
        self.line_weight = QLineEdit(self)
        #self.line_blood = QLineEdit(self)

        self.label_name.move(20,20)
        self.label_surname.move(180,20)
        self.label_age.move(20,100)
        self.label_gender.move(20,180)
        self.label_number.move(20,260)
        self.label_email.move(20,340)
        self.label_height.move(20,420)
        self.label_weight.move(180,420)
        self.label_blood.move(20,500)

        self.line_name.move(20,40)
        self.line_surname.move(220,40)
        self.line_age.move(20,120)
        #self.line_gender.move(20,20)
        self.line_number.move(20,280)
        self.line_email.move(20,360)
        self.line_heigh.move(20,440)
        self.line_weight.move(220,440)
        #self.line_blood.move(20,20)

        self.radio_male = QRadioButton("Male",self)
        self.radio_female = QRadioButton("Female", self)
        
        self.radio3 = QRadioButton("", self)
        self.radio3.setVisible(False)
        
        self.radio_male.move(20,200)
        self.radio_female.move(100,200)

        self.combo_blood = QComboBox(self)
        self.combo_blood.addItems(["A+", "A-", "B+", "B-", "0+", "0-", "AB+", "AB-"])
        self.combo_blood.move(20,520)

        self.button_save = QPushButton("Save", self)
        self.button_delete = QPushButton("Delete", self)
        self.button_exit = QPushButton("Exit", self)
        
        self.button_save.move(100,600)
        self.button_delete.move(180,600)
        self.button_exit.move(260,600)

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.VLine)
        self.frame.move(380,50)
        self.frame.setLineWidth(3)
        self.frame.resize(3,550)

        self.resize(800,650)
        self.show()

        self.button_exit.clicked.connect(self.close)
        self.button_delete.clicked.connect(self.reset)
    
    def reset(self):
        
        self.line_name.setText("")
        self.line_surname.setText("")
        self.line_age.setText("")
        self.line_number.setText("")
        self.line_email.setText("")
        self.line_heigh.setText("")
        self.line_weight.setText("")
        
        #Radio butonu sıfırlamak zor olduğu için yeni bir görünmez radio buton yapıp onu çek ettiriyoruz.
        #Bu sayede görünür radio butonlarımızın tiki silinmiş oluyor.
        #self.radio_male.setChecked(False)
        #self.radio_female.setChecked(False)
        self.radio3.setChecked(True)
        self.combo_blood.setCurrentIndex(-1)
        
app = QApplication([])
window = main()
app.exec()