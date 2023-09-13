from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        # Bir QTimer nesnesi oluştur ve 1000 milisaniye (1 saniye) aralıklarla zaman aşımı 
        # sinyalini gönder
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()

        # Zaman aşımı sinyali (timeout) "success" adlı bir işlevle bağlanır
        self.timer.timeout.connect(self.success)

        
        # Bir kontrol değişkeni başlat
        self.control = 0
        
        # Bir QPushButton oluştur ve ana pencereye ekleyin
        self.button = QPushButton(self)
        
        # Ana pencereyi belirtilen boyuta (800x500 piksel) ayarla ve göster
        self.resize = (2000,2000)
        self.show()
    
    # Her zaman aşımında çalışacak olan "success" işlevini tanımla
    def success(self):

        # "control" değişkenini 1 artır
        self.control += 1

         # Eğer "control" 5 ise, zamanlayıcıyı durdur ve 3000 milisaniye (3 saniye) sonra 
         # "button_resize" işlemini çağır
        if self.control == 5:
            self.timer.stop()
            self.timer.singleShot(3000, Qt.PreciseTimer, self.button_resize)
        
         # "button" adlı düğmeyi genişlik ve yükseklik olarak her seferinde 10 birim artır
        self.button.resize(self.button.width()+10, self.button.height())
        print("Başarılı")
    
    # "button_resize" işlevini tanımla
    def button_resize(self):

        # "button" adlı düğmeyi genişlik olarak 50 birim ve yükseklik olarak 20 birim artır
        self.button.resize(self.button.width()+50, self.button.height()+20)
            
app = QApplication([])
window = main()
app.exec()