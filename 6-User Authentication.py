from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.login = login(self)

        self.resize(800,500)

class login(QWidget):
    def __init__(self, parent = main):
        super().__init__()

        self.label_user = QLabel(self)
        self.label_password = QLabel(self)

        self.label_user.move(20,20)
        self.label_passrword = QLabel("Password", self)

        self.resize(300,200)
        self.show()

app = QApplication([])
window = main()
app.exec()        