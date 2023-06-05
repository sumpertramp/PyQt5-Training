from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout(self)
        
        self.grid.addWidget(QPushButton("Click1"), 0, 0, 1, 1)
        self.grid.addWidget(QPushButton("Click2"), 0, 1, 1, 1)
        self.grid.addWidget(QPushButton("Click3"), 0, 2, 1, 1)
        self.grid.addWidget(QPushButton("Click4"), 1, 0, 1, 2)

        print(self.grid.rowCount())
        print(self.grid.columnCount())

        self.grid.setSpacing(0)

        for i in range(3):
            for j in range(3):
                self.grid.addWidget(QPushButton("Clicl"), i, j, 1, 1)

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()