from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.menubar = QMenuBar()

        menu1 = self.menubar.addMenu("Menu 1")
        menu2 = self.menubar.addMenu("Menu 2")

        action1 = self.menubar.addAction("Action 1")
        action2 = self.menubar.addAction("Exit")
        action3 = menu1.addAction("Action 3")
        action4 = menu1.addAction("Action 4")
        action5 = menu1.addAction("Action 5")

        menu3 = menu1.addMenu("Menu 3")
        action6 = menu3.addAction("Action 6")

        #Tıkladığında uygulamayı kapatma
        action2.triggered.connect(self.close)
        
        action4.setShortcut("Ctrl+X")

        self.setMenuBar(self.menubar)

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()