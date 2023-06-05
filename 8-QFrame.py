from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.frame1 = QFrame(self) #QFrame oluşturuldu
        self.frame1.setFrameShape(QFrame.VLine)
        self.frame1.setFrameShape(QFrame.HLine)
        self.frame1.setLineWidth(10)

        self.tbutton =QToolButton(self)
        self.tbutton.setGeometry(50,50,100,100)

        """self.frame2 = QFrame(self.tbutton)
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.frame2.setFrameShadow(QFrame.Sunken)
        self.frame2.setLineWidth(10)
        self.frame2.setGeometry(0,0,100,100)"""#Zaten butonun üzerinde oluştuğu için kaydırma boyutları 0 verildi
        
        self.frame3 = QFrame(self.tbutton)
        self.frame3.setFrameShape(QFrame.Panel)
        self.frame3.setFrameShadow(QFrame.Sunken)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.frame3.setLineWidth(10)
        self.frame3.setGeometry(0,0,100,100)

        self.tbutton.setToolTip("<p>Birinci satır.</p><p>İkinci satır.</p>") #Burası html kodları ile ayarlanıyor.
        
            
        self.resize(800,500)
        self.show()

app = QApplication([])
window = main()
app.exec()