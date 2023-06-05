from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toolbar = QToolBar()
        self.toolbar.addAction(QIcon("Ball.png"), "Ball")
        self.toolbar.addAction(QIcon("Ball.png"), "Ball")
        self.toolbar.addAction(QIcon("Ball.png"), "Ball")
        self.toolbar.addSeparator()  #Çizgi ile ayırmak için
        self.toolbar.addAction(QIcon("Ball.png"), "Ball")
        self.toolbar.addAction(QIcon("Ball.png"), "Ball")
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.toolbar.setIconSize(QSize(100,100)) #Icon Size belirleme
        self.toolbar.setAllowedAreas(Qt.TopToolBarArea) #İzin verilen alanın sadece yukarı olması
        #Aynı anda iki alana izin verme
        self.toolbar.setAllowedAreas(Qt.TopToolBarArea | Qt.LeftToolBarArea)
        self.toolbar.setFloatable(False) #main Windowun dışına artık çıkamıyor
        self.toolbar.setMovable(False) #Taşınabilir özelliğini kaldırma

        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec();