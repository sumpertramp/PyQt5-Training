 #QSlider, PyQt ve Qt Framework tarafından sağlanan bir widget (arayüz elemanı) sınıfıdır. QSlider, 
 #kullanıcıların bir değer aralığı içinde bir değer seçmelerine izin veren bir kaydırma çubuğu sağlar.
 #QSlider, yatay veya dikey olarak yerleştirilebilir ve minimum ve maksimum değerler belirlenebilir. 
 #Kullanıcılar, kaydırma çubuğunu sürükleyerek veya klavye veya fare aracılığıyla kaydırarak bir değer 
 #seçebilirler. Ayrıca, QSlider, seçilen değerin değiştiğinde bir sinyal yayınlayabilir, böylece diğer
 # widget'lar veya işlevler bu değişiklikleri fark edebilir ve ona yanıt verebilir.
 #QSlider, genellikle kullanıcıların bir aralık içinde bir değer seçmesi gereken herhangi bir durumda 
 #kullanışlıdır, örneğin bir ses seviyesi kontrolü veya bir parlaklık ayarı gibi.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(20,20,200,40)
        self.slider.setRange(10,150)
        self.slider.setValue(25)
        self.slider.setSliderPosition(30)
        self.slider.setOrientation(Qt.Vertical)
        self.slider.setGeometry(20,20,25,250)
        self.slider.setTickPosition(QSlider.TicksLeft)
        self.slider.setTickInterval(20)
        
        self.label = QLabel(self)
        self.label.setGeometry(240,20,100,25)
        self.label.setText(str(self.slider.value()))
        self.label.setFont(QFont("Tahoma", 18))

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec() 