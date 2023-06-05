#QHBoxLayout ve QVBoxLayout, PyQt ve Qt Framework tarafından sağlanan iki farklı layout (düzen) sınıfıdır. 
#Bu sınıflar, widget'ların düzenini kontrol etmek ve bir arayüzdeki elemanların nasıl konumlandırılacağını 
#belirlemek için kullanılır.
#QHBoxLayout, widget'ları yatay olarak hizalamak için kullanılır. Bu düzen, genellikle yan yana 
#yerleştirilmiş widget'ları düzenlemek için kullanılır.
#VBoxlayout, widget'ları dikey olarak hizalamak için kullanılır. Bu düzen, genellikle üst üste yerleştirilmiş
#widget'ları düzenlemek için kullanılır.
#Her iki sınıf da, içerisindeki widget'ları uygun şekilde boyutlandırmak için gereken alanı hesaplar ve 
#widget'ları hizalar. Ayrıca, QHBoxLayout ve QVBoxLayout sınıfları, içerisindeki widget'ların boyutunu 
#dinamik olarak ayarlamak ve pencerenin yeniden boyutlandırılması gibi olaylara tepki vermek için uygun 
#yöntemler sağlar.
#Özetle, QHBoxLayout ve QVBoxLayout sınıfları, widget'ların düzenini kolayca kontrol etmek ve arayüzlerin 
#tasarımını daha organize hale getirmek için kullanışlıdır.


from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)

        self.button = QPushButton("Click", self)
        self.hbox.addWidget(self.button)
        #self.hbox.addStretch()
        self.hbox.addWidget(QPushButton("Add2")) #Otomatik yan yana dizilip yerleri ayarlandı
        self.hbox.addSpacing(100)#İki buton arasına 100'lük boşluk bırakma
        self.vbox = QVBoxLayout()
        self.hbox.addLayout(self.vbox)
        self.vbox.addWidget(QPushButton("Add3"))
        self.vbox.addWidget(QPushButton("Add4"))
        self.vbox.addWidget(QPushButton("Add5"))

        self.hbox.setContentsMargins(0,0,0,0) #Kenar uzaklıklarını ayarlama
        #self.hbox.setSpacing(50) #Aralık ayarlama
        
        self.hbox.setDirection(QBoxLayout.RightToLeft) #Tasarımı sağa doğru değiştirdik
        self.vbox.setDirection(QBoxLayout.BottomToTop) #Tasarımı aşağıdan yukarıya çevirme
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()