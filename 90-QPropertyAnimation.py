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

        # QGraphicsOpacityEffect kullanılarak bir opaklık efekti oluşturulmuş ancak şu anda yorum satırı olarak bırakılmış
        """
        effect = QGraphicsOpacityEffect()
        effect.setOpacity(0.2)
        self.widget.setGraphicsEffect(effect)
        """

        # QPropertyAnimation kullanılarak bir pozisyon animasyonu oluşturuluyor
        self.anim = QPropertyAnimation(self.widget, b"pos")
        self.anim.setEndValue(QPoint(200, 200))  # Bitiş pozisyonu
        self.anim.setDuration(3000)  # Animasyonun süresi (ms)
        self.anim.setEasingCurve(QEasingCurve.InOutBounce)  # Animasyon eğrisi
        self.anim.start()  # Animasyonu başlat

        self.resize(800, 500)
        self.show()

app = QApplication([])
window = main()
app.exec()