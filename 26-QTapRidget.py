from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(10,10,600,450)
        
        self.widget1 = QWidget()
        self.button1 = QPushButton("Click1", self.widget1)
        self.widget2 = QWidget()
        self.button2 = QPushButton("Click2", self.widget2)
        self.widget3 = QWidget()
        self.button3 = QPushButton("Click3", self.widget3)
        self.widget4 = QWidget()

        self.tab_widget.addTab(self.widget1, QIcon("icon.png"), "Tab1")
        self.tab_widget.addTab(self.widget2, QIcon("icon.png"), "Tab2")
        self.tab_widget.addTab(self.widget3, QIcon("icon.png"), "Tab3")

        self.tab_widget.removeTab(1)  #Tab kaldırma
        self.tab_widget.insertTab(1,self.widget4, "Tab4")  #Tab ekleme

        print(self.tab_widget.indexOf(self.widget4))  #Indexini yazdırma
        print(self.tab_widget.count()) #Sayısını yazdırma

        #self.tab_widget.setTabEnabled(2, False) #Diseable yapma
        #self.tab_widget.setTabVisible(2, False) #Görünürlüğünü kaldırma
        
        self.tab_widget.setTabToolTip(0,"Show the content of Tab1")

        self.tab_widget.setMovable(True) #Sekmelerin taşınabilir olması
        self.tab_widget.setTabsClosable(True) #Sekmelerin kapatılabilir olması

        self.tab_widget.setCurrentIndex(2) #Açıldığında aktif tabı ayarlama
        #self.tab_widget.setCurrentWidget(4)
        
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()