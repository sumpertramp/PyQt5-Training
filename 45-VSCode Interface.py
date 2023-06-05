from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

css = """
    QMenuBar{
       background-color:rgb(60,60,60);
       height: 30px;
    }
    QMenuBar::item{
       margin: 0;
       color: rgb(191,191,191);
    }
    QMenuBar::item::selected{
       background-color: rgb(100,100,100)
    }
"""

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        
        self.menubar = QMenuBar()
        self.menubar.addMenu("  File  ") #CSS ile padding vermek yerine bu şekilde boşluk bırakmak daha güel oldu
        self.menubar.addMenu("  Edit  ")
        self.menubar.addMenu("  Selection  ")
        self.menubar.addMenu("  View  ")
        self.menubar.addMenu("  Go  ")
        self.menubar.addMenu("  Run  ")
        self.menubar.addMenu("  Terminal  ")
        self.menubar.addMenu("  Help  ")
        self.setMenuBar(self.menubar)

        self.menubar.setStyleSheet(css)
        
        self.logo = QLabel()
        self.pixmap = QPixmap("Code.png")
        self.logo.setPixmap(self.pixmap) #Resmin kendi boyutu neyse o boyutta açıldı     
        self.logo.setPixmap(self.pixmap.scaled(QSize(20,20), Qt.KeepAspectRatio))
        self.menubar.setCornerWidget(self.logo, Qt.TopLeftCorner)
        
        self.hbox = QHBoxLayout(self.menubar)
        self.hbox.setContentsMargins(self.menubar.sizeHint().width()+30,0,0,0) #Soldan menubarın uzunluğu kadar labeli kaydırma
        self.title = QLabel("This is the title of the window.")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("color: rgb(191,191,191)")
        self.hbox.addWidget(self.title)
        
        self.tbutton1 = QToolButton()
        self.tbutton1 = QToolButton()
        self.tbutton1 = QToolButton()

        self.tbutton1.setIcon(QIcon("minimize.png"))

        self.resize(700,700)
        self.showMaximized() #Ekranı kaplayacak şekilde açma

app = QApplication([])
window = main()
app.exec()