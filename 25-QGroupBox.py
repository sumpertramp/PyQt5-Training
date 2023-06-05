from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.group = QGroupBox(self)
        self.group.setTitle("Trial")
        self.group.setGeometry(20,20,400, 250)

        self.group.setAlignment(Qt.AlignCenter)

        self.group.setCheckable(True) #Check edilebilir yapıldı
        self.group.setChecked(False) #Açılışta set edilmemiş ayarlandı

        self.vbox = QVBoxLayout()
        self.check1 = QCheckBox("Click1")
        self.check2 = QCheckBox("Click2")
        self.vbox.addWidget(self.check1)
        self.vbox.addWidget(self.check2)

        self.group.setLayout(self.vbox) 

        self.resize(700,700)
        self.show()

        #Goupbpx check edildiğinde içindekilerde otomatik check edilsin isteniyorsa:
        self.group.toggled.connect(self.change)
    def change(self,b):
        if b:
            self.check1.setChecked(True)
            self.check2.setChecked(True)
        else:
            self.check1.setChecked(False)
            self.check2.setChecked(False)

app = QApplication([])
window = main()
app.exec()