from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.tree = QTreeWidget(self)
        self.tree.setGeometry(20,20,450,450)

        self.tree.setHeaderLabels(["Header1", "Header2", "Header3"])
        self.tree.setColumnCount(3)

        for i in range(10):
            self.item = QTreeWidgetItem()
            self.item.setText(0, "Item %d" %i)
            self.item.addChildren([self.item.clone(), self.item.clone(), self.item.clone()])
            self.tree.addTopLevelItem(self.item)
        self.item = QTreeWidgetItem()
        self.item.setText(0, "Itemmmmmmmmmmmmmm")  #Bu itemin genişliğine göre header genişliği değişti
        self.tree.addTopLevelItem(self.item)
       
        #self.tree.setColumnWidth(0,10) #Görünüz kısmını ayarlama
        #self.tree.setExpandsOnDoubleClick(False)
        
        #self.tree.setIndentation(200)
        #self.tree.resizeColumnToContents(0) #İçeriğe göre boyutlandırma
        
        self.tree.setSortingEnabled(True) #Azalan ve artan sıralama ayarlama
        self.tree.expandAll() #Hepsini expand etme genişletme yani içeriği açık açılması
        self.tree.collapseAll() #Hepsini kapatma collapse etme
        
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()