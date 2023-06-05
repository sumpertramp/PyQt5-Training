from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.label_km = QLabel( "Distance Traveled:", self)
        self.label_average = QLabel( "Average Fuel Consumption:", self)
        self.label_price = QLabel("Fuel Cost:" , self)
        self.label_result = QLabel("Result: ", self)
        
        self.label_km.move(20,20)
        self.label_average.move(20, 60)
        self.label_price.move(20,100)
        self.label_result.move(220,140)

        self.label_result.setFont(QFont("Tahoma", 18))
        self.label_result.resize(120,30)

        self.line_km = QLineEdit(self)
        self.line_average = QLineEdit(self)
        self.line_price = QLineEdit(self)

        self.line_km.move(180,20)
        self.line_average.move(180,60)
        self.line_price.move(180,100)

        self.button_compute = QPushButton("Compute",self)
        self.button_compute.move(80, 140)
        self.button_compute.clicked.connect(self.count)

        self.label_error = QLabel("Error", self)
        self.label_error.move(25,180)
        self.label_error.resize(300, 50)
        self.label_error.setAlignment(Qt.AlignCenter)
        self.label_error.setFont(QFont("Tahoma", 10))

        self.setWindowTitle("Fuel Expense")

        self.resize = (450, 450)
        self.show()
    
    def count(self):
        #Bütün veriler girilmiş mi?
        #Bütün veriler sayısal mı?
        #Bütün veriler pozitif mi?

        self.line_list = [self.line_km, self.line_average, self.line_price]

        for i in self.line_list:
            if i.text().strip() != "":
                if i.text().replace(".", "").isnumeric() or i.text().replace(",", "").isnumeric():
                    pass
                else:
                    self.label_error.setText("Please enter numeric characters.")
                    break
            else:
                self.label_error.setText("Please do not leave the fields blank." )
                break
        else:
            result = float(self.line_km.text().replace(",", "."))*float(self.line_average.text().replace(",","."))*float(self.line_price.text().replace(",", "."))/100
            self.label_result.setText("%0.2f" % result)
            self.label_error.setText("Error")
            print("Success")
            
app = QApplication([])
window = main()
app.exec()