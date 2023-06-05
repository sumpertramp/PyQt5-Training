from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

font = QFont()  #Font tanımlanarak bütün özellikleri ayarlandı
font.setFamily("Consolas")
font.setPointSize(40)
font.setBold(True)
font.setItalic(True)


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Label", self) #PEncerede Text adı Label olan bir yazı oluşturuldu
        self.label.move(100, 100) #Label x ekseninde 100, y ekseninde 800 kaydırıldı  
       
        print(self.label.text()) #Bu kod ile labelin textini alabiliriz
        self.label.setText("Label 2"*4) #Label texti değiştirme ve 4 kere yazdırma
        
        self.label.setFont(QFont("Tahoma",24, 100, True)) #Yazı tipi, boyut, kalınlık, italik(true, false) ayarı
        self.label.setFont(font) #Yukarıdaki tanımadığımız fonta set ettik
        
        self.label.setFrameShape(QFrame.Box) #Labelin çevresindeki çerçeve ayarlandı
        self.label.setLineWidth(10) #Çerçeve kalınlığı ayarlandı

        self.label.resize(600,300) #Çerçeve boyutları ayarlandı
        #self.label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) #Label çerçevenin en üstünün tam ortasına taşındı
        #self.label.setAlignment(Qt.AlignCenter) 
        #self.label.setAlignment(Qt.AlignRigt | Qt.AlignBottom)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignCenter) #Çerçeve en sağın tam ortasına taşındı
        self.label.clear() #Labeldeki metni siler



        self.label.adjustSize() #Metin çerçevesini metne göre boyutlandırdı
        self.label.setWordWrap(True) #Alt satıra inme durumu aktifletirirldi
        self.resize = (100, 500)
        self.show()

app = QApplication([])
window = main()
app.exec()
