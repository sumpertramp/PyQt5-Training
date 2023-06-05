#Açılır liste demektir. Genellikle il ve ilçelerin seçimi, 
#adres seçimi, üniversite seçimi gibi listelerde kullanılır

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

d_city = {"İstanbul":["Adalar", "Arnavutköy", "Ataşehir", "Avcılar",
"Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir", "Bayrampaşa"],
"Antalya": ["Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", 
"Manavgat", "Muratpaşa", "Serik"]}

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.combo = QComboBox(self)
        self.combo.setGeometry(20,20,120,25)

        self.combo.addItem("Kitap")
        self.combo.addItem("Kalem")
        self.combo.addItem("Defter")

        self.combo.removeItem(1) #Kalem itemini listeden kaldırdık
        print(self.combo.itemText(0)) #0. itemi ekrana yazdırdık
        
        self.combo.setItemText(1,"Silgi")
        self.combo.setItemIcon(1,QIcon("Silgi.png")) 

        print(self.combo.currentIndex())
        print(self.combo.currentText())

        #self.combo.setCurrentIndex(1) #Silgi seçili geldi
        self.combo.setCurrentText("Silgi")

        self.combo.insertItem(1, "Kalem")#Araya item işleme
        self.combo.insertSeparator(2) #Araya çizgi ekleme
        #self.combo.clear()

        self.radio1 = QRadioButton("İstanbul", self)
        self.radio2 = QRadioButton("Antalya", self)
        self.radio2.move(80,0)

        self.radio1.clicked.connect(self.listing)
        self.radio2.clicked.connect(self.listing)


        self.resize(800,500)
        self.show()
    
    def listing(self):
        
        if self.radio1.isChecked():
            self.combo.clear()
            self.combo.addItems(d_city["İstanbul"])
        
        if self.radio2.isChecked():
            self.combo.clear()
            self.combo.addItems(d_city[self.radio2.text()])    
app = QApplication([])
window = main()
app.exec()
