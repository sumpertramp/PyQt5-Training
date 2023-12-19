from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        # Ana pencere içindeki bir alt widget oluşturuluyor
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 50, 100, 50)  # Widget'ın başlangıç boyutu ve konumu
        self.widget.setStyleSheet("background-color: red;")  # Widget'ın arka plan rengi

        # QVariantAnimation kullanılarak bir renk animasyonu oluşturulmuş ancak şu anda yorum satırı olarak bırakılmış
        '''
        self.animation = QVariantAnimation(
            startValue=QColor("red"),
            endValue=QColor("blue"),
            valueChanged=self.anim,
            duration=5000
        )
        '''

        # QVariantAnimation kullanılarak bir boyut animasyonu oluşturuluyor
        self.animation = QVariantAnimation()
        self.animation.setStartValue(QRect(50, 50, 50, 50))  # Başlangıç boyutu ve konumu (x, y, genişlik, yükseklik)
        self.animation.setEndValue(QRect(50, 500, 50, 50))  # Bitiş boyutu ve konumu (x, y, genişlik, yükseklik)
        self.animation.setDuration(2000)  # Animasyonun süresi (ms)
        self.animation.valueChanged.connect(self.rect)  # Her değer değişiminde çağrılacak fonksiyon
        self.animation.start()  # Animasyonu başlat

        self.resize(800, 500)
        self.show()

    def rect(self, v):
        # Her değer değişiminde çağrılan fonksiyon, widget'ın boyutunu günceller
        self.widget.setGeometry(v)

    def anim(self, v):
        # Renk animasyonu için kullanılan fonksiyon, şu anda yorum satırı olarak bırakılmış
        self.widget.setStyleSheet("background-color: %s" % v.name())

app = QApplication([])
window = main()
app.exec()