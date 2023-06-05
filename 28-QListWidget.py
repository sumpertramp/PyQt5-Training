from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.list = QListWidget(self)
        self.list.setGeometry(20,20,300,450)

        self.list.addItem("Item1")
        self.list.addItems(["Pencil", "Eraser", "Book"])

        self.item = QListWidgetItem("Ball", self.list)
        self.item2 = QListWidgetItem("Notebook", self.list)
        self.item2.setText("Pen")

        self.item.setIcon(QIcon("x.png"))
        self.item2.setIcon(QIcon("ball.png"))
        
        self.list.insertItem(2,"Item2")

        for i in range(20):
            self.list.addItem(self.item.clone())


        print(self.list.count()) #Listedeki eleman sayısını öğrenme

        self.list.setCurrentItem(self.item) #Herhangi bir itemi seçili olarak açma
        self.list.setCurrentRow(3)

        print(self.list.currentItem().text())
        print(self.list.currentRow())

        #self.list.sortItems(Qt.AscendingOrder) #Artan sıralama
        self.list.sortItems(Qt.DescendingOrder) #Azalan sıralama

        item = self.list.takeItem(1) #İçeriye indis verip o eleman alınır, 1. itemi alır
        print(item.text())
        item.setText("Pen2") #Listeye sokmadan listeyi etkilemez
        self.list.insertItem(1, item) #listeye burda ekleniyor Item listeden alnıp her yere eklenebilir
        
        #self.list.clear() #Listeyi temizler

        #self.list.setFlow(QListView.LeftToRight) #İtemleri sağdan sola sıralama
        self.list.setRowHidden(5,True) #5. indisli eleman gizlendi

        self.list.setViewMode(QListView.ListMode) 
        #self.list.setViewMode(QListView.IconMode)
        
        self.list.setWrapping(True) #Boyutu aştığında liste yana doğru kayıyor.
        
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()