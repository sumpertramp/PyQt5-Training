#Tablo oluşturma

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget(5,5,self)
        self.table.setGeometry(20,20,750,450)

        print(self.table.columnCount()) #Sutun sayısını yazdırma
        print(self.table.rowCount()) #Satır sayısını yazdırma

        #self.table.setColumnCount(10)  #Column sayısını set etme
        #self.table.setRowCount(10)  #Row sayısını set etme
        
        self.item = QTableWidgetItem()
        self.item.setText("Item 1") #Itemi tabloda istenen konuma atma
        self.table.setItem(2,2,self.item)

        self.table.setHorizontalHeaderItem(2,self.item.clone())  #2.sutunun başlığını değiştirdik
        self.table.setHorizontalHeaderLabels(["Başlık 1", "Başlık 2", "Başlık 3"])  #Label olarak sütun başlıklarını değiştirme

        self.table.setVerticalHeaderItem(3, self.item.clone())  #Row yani satıra item belirtme

        self.table.setCurrentCell(4,4)  #Seçili gelen itemi belirtme
        self.table.setCurrentItem(self.item)
        print(self.table.currentItem().text())  #Güncel itemi yazdırma

        self.table.setColumnHidden(2,True)  #Bir sutunu gizli yapma
        self.table.setRowHidden(2,True)  #Bir satırı gizli yapma

        self.table.setRowHeight(2,200)  #Boyut ayarlama
        #self.table.setColumnWidth(0,200)  #Boyut ayarlama

        #self.table.setShowGrid(False)  #Grid kapatma
        self.table.setGridStyle(Qt.DashLine)  #Grid türü belirleme
        #self.table.setGridStyle(Qt.DotLine)
        #self.table.setGridStyle(Qt.SolidLine)

        self.table.setSortingEnabled(True)
        #self.table.setSpan(0,0,1,4)  #Herhangi bir sütun ya da satırı kapsamasını sağlamak

        self.item = QTableWidgetItem()
        self.item.setText("KAlem aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.table.setItem(0,0,self.item)
        self.table.setWordWrap(True)  #İtemi kapsayacak şekilde tablonun şekillenmesini sağlamak
        
        
        self.resize(800,500)
        self.show()

app = QApplication([])
window = main()
app.exec()