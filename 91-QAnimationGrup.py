from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class main(QWidget):
    def __init__(self):
        super().__init__()

        # Ana pencere içindeki bir alt widget oluşturuluyor
        self.widget = QWidget(self)
        self.widget.setGeometry(50, 50, 100, 50)
        self.widget.setStyleSheet("background-color: red;")

        # Alt widget üzerinde bir pozisyon animasyonu oluşturuluyor
        self.anim1 = QPropertyAnimation(self.widget, b"pos")
        self.anim1.setEndValue(QPoint(200, 200))
        self.anim1.setEasingCurve(QEasingCurve.OutBounce)
        self.anim1.setDuration(2000)
        # self.anim1.start()  # Pozisyon animasyonu başlatılmış ancak şu anda yorum satırı olarak bırakılmış

        # Alt widget üzerinde bir boyut animasyonu oluşturuluyor
        self.anim2 = QPropertyAnimation(self.widget, b"size")
        self.anim2.setEndValue(QSize(200, 200))
        self.anim2.setEasingCurve(QEasingCurve.OutBounce)
        self.anim2.setDuration(2000)
        # self.anim2.start()  # Boyut animasyonu başlatılmış ancak şu anda yorum satırı olarak bırakılmış

        """ 
        # Sırayla animasyonun gerçekleşmesini sağlayan bir animasyon grubu oluşturuluyor
        self.animgroup = QSequentialAnimationGroup()
        self.animgroup.addAnimation(self.anim1)
        self.animgroup.addAnimation(self.anim2)
        self.animgroup.start()  # Animasyon grubu başlatılmış ancak şu anda yorum satırı olarak bırakılmış
        """

        # Paralel (aynı anda) animasyonun gerçekleşmesini sağlayan bir animasyon grubu oluşturuluyor
        self.animgroup = QParallelAnimationGroup()
        self.animgroup.addAnimation(self.anim1)
        self.animgroup.addAnimation(self.anim2)
        self.animgroup.start()  # Animasyon grubu başlatılmış ancak şu anda yorum satırı olarak bırakılmış

        self.resize(800, 500)
        self.show()

app = QApplication([])
window = main()
app.exec()