from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        table_dict = {
            "No":[120201,130123,175954,142653,187236],
            "Name":["Kemal", "Zeynep", "Cemal", "Kerim", "Ali"],
            "Surname":["Ali", "Cemal","Kerim", "Ünal","Doğan"],
            "Midterm":[80,75,90,65,60],
            "Final":[75,70,80,90,80],
            "Average":[]
        }

        self.hbox = QHBoxLayout(self)
        self.table = QTableWidget(20,7)
        self.hbox.addWidget(self.table)

        # Elimizde 5 satırlık ve 5 sutunluk veri var

        self.table.setHorizontalHeaderLabels(["No", "Name", "Surname", "Midterm", "Final", "Average"])
  
        for i in range(5):
            for j,k in enumerate(table_dict):
                try:
                    self.item = QTableWidgetItem()
                    self.item.setText(str(table_dict[k][i]))
                    self.table.setItem(i,j, self.item)
                except:
                    pass

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()