from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.list = QListWidget(self)
        self.list.setGeometry(20,20,300,450)

        self.item1 = QListWidgetItem("Item1", self.list)
        self.item2 = QListWidgetItem("Item2", self.list)
        self.item3 = QListWidgetItem("Item3", self.list)

        self.item1.setFont(QFont("Calibri", 24))
        self.item1.setFont(QFont("Forte", 16))
        self.item1.setFont(QFont("Tahoma", 20))

        self.item3.setTextAlignment(Qt.AlignCenter)

        self.item2.setIcon(QIcon("x.png"))
        self.list.setIconSize(QSize(60,60))

        self.item1.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
        
        self.item3.setSelected(True) #Bu item seçili gelir
        self.item3.setHidden(True) #Item 3 kaldırıldı
        
        self.item1.setToolTip("Show the content of the item1.") #Itemin üzerine gelince açıklamasını ekleme
        self.item2.setToolTip("Show the content of the item2.")
        self.item3.setToolTip("Show the content of the item3.")

        self.item4 = self.item2.cone()
        self.list.addItem(self.item4)    
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()