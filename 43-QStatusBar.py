from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central = QScrollArea()
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.status.setSizeGripEnabled(False)

        #self.status.showMessage("Loading is success!", 3000) #3 saniye durup kaybolan bir metin eklendi
        #self.status.addWidget(QLabel("Message"), 1) #Labelin kendi textini ekleme
        self.setStatusTip("On the window!") #mauseyi statuse getirince görünen text
        self.status.addPermanentWidget(QLabel("Message", 1))

        self.setCentralWidget(self.central)

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()