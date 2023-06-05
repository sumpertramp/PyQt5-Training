from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

font1 = QFont("Tahoma", 22)
font2 = QFont("Tahoma", 12)

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)
        self.vbox_right = QVBoxLayout()
        self.vbox_left = QVBoxLayout()
        self.hbox.addLayout(self.vbox_left)
        self.hbox.addLayout(self.vbox_right)

        self.vbox_left_setup()
        self.vbox_right_setup()
        
        self.resize(500,500)
        self.show()
    
    def get_info (self, c):
        for i in range(4):
            self.label_list[i+1].setText(self.dict_item[c.text()][i])    
    
    def vbox_left_setup(self):
        self.list = QListWidget()
        self.vbox_left.addWidget(self.list)
        self.list.setFont(font2)

        self.item1 = QListWidgetItem("Lenova", self.list)
        self.item2 = QListWidgetItem("HP", self.list)
        self.item3 = QListWidgetItem("Asus", self.list)
        
        self.list.currentItemChanged.connect(self.get_info)
        
        self.dict_item = {
            "Lenovo": ["1TB", "4GB", "2GB", "Available", "3500 TL"],
            "HP": ["512GB", "4GB", "2GB", "Not available", "-----"],
            "Asus": ["1TB", "8GB", "4GB", "Available", "5500 TL"]
        }
    
    def vbox_right_setup(self):
        self.label = QLabel("Product Specifications")
        self.label.setFont(font1)
        self.label.setFrameShape(QFrame.Panel)
        self.vbox_right.addWidget(self.label)
        self.vbox_right.setAlignment(Qt.AlignTop)

        self.form = QFormLayout()
        self.vbox_right.addLayout(self.form)
        
        self.label1 = QLabel("Feature")
        self.label2 = QLabel("Feature")
        self.label3 = QLabel("Feature")
        self.label4 = QLabel("Feature")
        self.label5 = QLabel("Feature")
        self.label6 = QLabel("Capacity of the hard disk:")
        self.label7 = QLabel("Capacity of the ram:")
        self.label8 = QLabel("Capacity of the graphics card:")
        self.label9 = QLabel("Stock status:")
        self.label10 = QLabel("Product price:")
        
        self.label_list = [self.label1, self.label2, self.label3, self.label4, self.label5, self.label6, self.label7, self.label8,self.label9, self.label10]
        for i in self.label_list:
            i.setFont(font2)

        self.form.addRow(self.label6, self.label1)
        self.form.addRow(self.label7, self.label2)
        self.form.addRow(self.label8, self.label3)
        self.form.addRow(self.label9, self.label4)
        self.form.addRow(self.label10, self.label5)
    
app = QApplication([])
window = main()
app.exec()