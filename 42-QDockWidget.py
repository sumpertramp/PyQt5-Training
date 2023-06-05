from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        #DockWidget kurmadan önce CentralWidget'a ihtiyacımız var
        self.centra1 = QWidget()

        self.dock = QDockWidget()

        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock, Qt.Vertical)
        self.dock.setWidget(QScrollArea())
        
        self.dock.setWindowTitle("DockWidget")
        
        #self.dock.setFeatures(QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetMovable) #Taşınabilir ve ekran boyutu ayarlanabilir özelliği kaldırıldı
        
        #Başlangıçta nasıl açılacağını belirleme
        self.dock.setFloating(True) #Pencereden ayrı bir şekilde açılması

        self.setCentralWidget(self.centra1)
        
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()