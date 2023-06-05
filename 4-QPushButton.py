from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.button = QPushButton("Tıkla", self) #Button oluşturduk
        self.button.move(100, 100) #Butonu istediğimiz yere taşıdık
        self.button.resize(150,50) #Buton boyutunu ayarladık
        self.button.setFont(QFont("Tahoma", 24)) #Butona text atayıp yazıtipi ve yazı boyutunu ayarladık
        self.button.setText("Tıkla 2") #Buton textini değiştirdik
        
        self.button.setIcon(QIcon("Button_Icon.jpg")) #Butona bir simge atadık. Bu isimde bir jpg dosyası proje dosyasında bulunmalıdır
        self.button.setIconSize(QSize(40,40)) #Buton Icon'unun büyüklüğü ayarlandı
        
        #self.button.setDiseable(True) #Buton aktifliği kaldırıldı
        #self.button.setEnabled(True) #Buton aktif etme

        self.button.setCursor(Qt.PointingHandCursor) #Butonun üzerine fare geldiğinde butona özel değiştirdik
        
        #self.button.clicked.connect(self.close) #Butona tıklandığında başka bir yere bağlama
        self.button.clicked.connect(self.title) #Title için yeni bir fonksiyon oluşturduk. Yoksa çalışmaz.
        self.resize(400, 400)
        self.show()
    
    def title(self): #Burada butona tıklandığında yapması için bir görev oluşturduk
        self.setWindowTitle("Baslık")

app = QApplication([])
window = main()
app.exec()