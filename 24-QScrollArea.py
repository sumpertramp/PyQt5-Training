
#QScrollArea, PyQt ve Qt framework'ünün bir parçası olan bir sınıftır.
#Qt, masaüstü uygulamaları oluşturmak için kullanılan popüler bir C++ 
#framework'üdür ve PyQt, Qt framework'ünü Python programlama diline 
#bağlayan bir Python bağlayıcısıdır.
#QScrollArea, bir kullanıcı arabirimi öğesinin içeriğini görüntülemek 
#için bir kaydırma alanı sağlar. Bu, içeriği belirli bir boyuta sığdırmak
#ve kullanıcının içeriği görüntülemek için dikey veya yatay kaydırma 
#işlevselliğini kullanmasına olanak tanır. Genellikle büyük metin blokları, görüntüler veya başka karmaşık içerikler gibi içeriğin fazla yer kapladığı durumlarda kullanılır.
#QScrollArea sınıfı, öğeleri içine yerleştirebileceğiniz ve daha sonra 
#bu öğeleri kaydırılabilir bir pencerede görüntüleyebileceğiniz bir 
#konteyner olarak kullanılır. ScrollArea, bir QWidget'in alt sınıfıdır 
#ve içeriğini görüntülemek için içinde başka bir widget'i (genellikle bir QVBoxLayout veya bir QGridLayout içinde) barındırabilir.
#QScrollArea'nın işlevselliği, belirli bir boyutu aşan içeriği 
#görüntülemek için yatay ve dikey kaydırma çubukları sağlamakla sınırlı 
#değildir. Örneğin, içeriğin yeniden boyutlandırılması, belli bir konuma 
#kaydırılması veya belirli bir konuma kaydırılması gibi farklı işlemleri
#de destekleyebilir.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.area = QScrollArea(self)
        self.area.setGeometry(10,10,250,200)
        self.area.setFrameShape(QFrame.Box)

        self.widget =QWidget()

        self.vbox = QVBoxLayout(self.widget)
        
        for i in range(15):
            self.vbox.addWidget(QPushButton("Click"))
        
        #Sadece mause ile kontrol edilen gizli bir area için:

        self.area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) #Her ikisi de sürekli görünür yapıldı
        self.area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.area.setWidgetResizable(True) #Widget scrol area ile aynı botutta ayarlandı
        
        self.area.setWidget(self.widget)

        self.resize(300,250)
        self.show()

app = QApplication([])
window = main()
app.exec()