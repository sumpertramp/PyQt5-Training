#Menü arkaplan ==> 60,60,60
#Menü yazıları ==> 191,191,191
#ToolBar Arkaplan ==> 51,51,51
#StatusBar Arkaplan ==> 0,122,204

#CustomizeWindowHint
#WİndowTitleHint
#WindowMinimizeButtonHint
#WindowMaximizeButtonHİnt
#WindowMinMaxButtonHint
#WindowCloseButtonHint
#WindowStaysOnToHint
#WindowStaysOnBottomHint

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        #FramelessWindowHint  ==> Windows'dan gelen otomatik özellikleri kabul etmeme
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.CustomizeWindowHint | 
                            Qt.WİndowTitleHint | 
                            Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHİnt |
                            Qt.WindowMinMaxButtonHint |
                            Qt.WindowCloseButtonHint |
                            Qt.WindowStaysOnToHint |
                            Qt.WindowStaysOnBottomHint)



        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()