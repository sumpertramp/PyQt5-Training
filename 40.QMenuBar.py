from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

# main sınıfı QMainWindow sınıfından türetiliyor
class main(QMainWindow):
    def __init__(self):
        # QMainWindow sınıfının __init__ metodunu çağırarak başlangıç ayarlarını yap
        super().__init__()

        # Menü çubuğunu oluştur
        self.menubar = QMenuBar()

        # Menü çubuğuna "Menu 1" ve "Menu 2" adlı iki menü ekleniyor
        menu1 = self.menubar.addMenu("Menu 1")
        menu2 = self.menubar.addMenu("Menu 2")

        # Menü çubuğuna "Action 1" ve "Exit" adlı iki eylem ekleniyor
        action1 = self.menubar.addAction("Action 1")
        action2 = self.menubar.addAction("Exit")

        # "Action 3", "Action 4" ve "Action 5" adlı üç eylem "Menu 1" menüsüne ekleniyor
        action3 = menu1.addAction("Action 3")
        action4 = menu1.addAction("Action 4")
        action5 = menu1.addAction("Action 5")

        # "Menu 3" adlı bir alt menü "Menu 1" menüsüne ekleniyor
        menu3 = menu1.addMenu("Menu 3")

        # "Action 6" adlı bir eylem "Menu 3" alt menüsüne ekleniyor
        action6 = menu3.addAction("Action 6")

        # "Exit" eyleminin tetiklendiğinde uygulamayı kapatma işlevini bağla
        action2.triggered.connect(self.close)
        
        # "Action 4" eylemi için kısayol belirle (Ctrl+X)
        action4.setShortcut("Ctrl+X")

        # Menü çubuğunu ana pencereye ekle
        self.setMenuBar(self.menubar)

        # Ana pencerenin boyutunu ayarla ve göster
        self.resize(700, 700)
        self.show()

# PyQt uygulaması oluştur
app = QApplication([])

# main sınıfından bir pencere oluştur
window = main()

# Uygulamayı başlat
app.exec()
