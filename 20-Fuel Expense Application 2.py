#Form Layout kullanarak aynı projeyi yapma
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout(self)
        self.form.setVerticalSpacing(30)

        self.form.addRow(QLabel("Distance traveled:"), QLineEdit())
        self.form.addRow(QLabel("Average consuption:"), QLineEdit())
        self.form.addRow(QLabel("Fuel cost:"), QLineEdit())
        
        self.button = QPushButton("Calculate")
        self.label_result = QLabel("Result:")
        self.hbox = QHBoxLayout()
        self.hbox.setAlignment(Qt.AlignRight)
        self.hbox.setSpacing(50)
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.label_result)
        self.hbox.addSpacing(100)
        self.form.addRow(self.hbox)

        self.hbox2 = QHBoxLayout()
          
        self.label_error = QLabel("Error!")
        self.label_error.setAlignment(Qt.AlignCenter)
        self.hbox2.addWidget(self.label_error)
        self.form.addRow(self.hbox2)
        


        self.resize(350,180)
        self.show()

app = QApplication([])
window = main()
app.exec() 