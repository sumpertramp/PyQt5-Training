from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()
        
        self.line = QLineEdit(self) #Line Edit oluşturuldu
        # self.line.setText("LineEdit")
        # print(self.line.text())

        self.line.setPlaceholderText("Adınızı Giriniz.") #Line içinde silik silinebilir yazı. 
        # self.line.setReadOnly(True) #Yazılabilir özelliği kaldırıldı
        self.line.setFrame(False) # Etraftaki çizgi kaldırıldı
        self.line.setGeometry(40,40,100,100) #Konumu ve boyutu ayarlandı
        self.line.setClearButtonEnabled(True) # Bir yazdıktan sonra silmek için çarpı çıkıyor
        
        
        self.resize(400,400)
        self.show()

app = QApplication([])
window = main()
app.exec()
