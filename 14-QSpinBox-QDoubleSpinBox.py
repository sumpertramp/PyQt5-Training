#QSpinBox, kullanıcının bir sayı değerini arttırıp azaltabileceği bir arayüz sağlar. 
#Kullanıcı, arttırma ve azaltma düğmelerine tıklayarak veya doğrudan sayı değerini girerek 
#değeri değiştirebilir.
#QSpinBox, özellikle kullanıcı tarafından ayarlanması gereken bir değer olduğunda veya bir 
#parametrenin sayısal bir değerle belirlenmesi gerektiğinde kullanışlıdır. Örneğin, bir grafik 
#çizim programında, kullanıcının bir çizgi kalınlığı veya renk değerini belirlemesi 
#gerektiğinde QSpinBox kullanılabilir.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.spin = QSpinBox(self)
        self.spin.setRange(1,100) #Gideceği min ve max noktalar ayarlandı
        self.spin.setGeometry(10,10,100,25)

        self.spin.setMinimum(10)#Sadece min değerini ayarlama
        self.spin.setMaximum(20)#Sadece max değerini ayarlama

        self.spin.setAlignment(Qt.AlignRight)#İçerisindeki yazının en sağda olması
        print(self.spin.value) #İçerisindeki değeri yazdırma
        self.spin.setValue(20) #İçerisindeki değeri set etme
        print(self.spin.value())

        self.spin.setSingleStep(5) #Kaçar kaçar artıp azalacağını ayarlama
        self.spin.setSuffix(" TL") #Sonuna yazı-birim ekleme
        self.spin.setPrefix("% ") #Başına sembol ekleme

        self.double = QDoubleSpinBox(self) #Double türünde spin box oluşturuldu
        self.double.setGeometry(10,30,100,25)
        self.double.setSingleStep(0.01) #Artıi adımı belirlendi
        self.double.setDecimals(3)#Double sayının virgülden sonra kaç haneli olduğu ayarlandı



        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec() 