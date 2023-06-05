# Genel olarak ana pencere olarak QMainWindow kullanılır

# QMainWindow, PyQt ve PySide gibi Python tabanlı grafik kullanıcı 
# arayüzü (GUI) kütüphanelerinde kullanılan bir sınıftır. QMainWindow, 
# bir masaüstü uygulamasının ana penceresini temsil eder. Bu sınıf, 
# genellikle çoklu belge arabirimlerine (MDI) ve tek bir belge 
# arabirimine (SDI) sahip uygulamalarda kullanılır.

# QMainWindow, kullanıcı arayüzünü yönetmek için gerekli olan birçok 
# özelliği ve işlevi sağlar. Bu özellikler arasında bir menü çubuğu, 
# araç çubukları, durum çubuğu ve bir ana içerik alanı bulunur. 
# QMainWindow sınıfı, bu bileşenleri düzenlemek, ayarlamak ve yönetmek 
# için işlevler ve yöntemler sağlar.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # self.setWindowOpacity(0.5) # Saydamlık
        self.central = QWidget()

        self.dock = QDockWidget()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock, Qt.Vertical) 
        self.setCentralWidget(self.central)
        
        # ToolBar
        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setMinimumHeight(100)

        # StatusBar
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.setStatusTip("Window station")

        # MenuBar
        self.menubar = QMenuBar()
        self.setMenuBar(self.menubar)
         

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()