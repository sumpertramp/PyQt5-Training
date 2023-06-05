from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTimeEdit(self) #Sadece saat ve dk bilgisini verir
        self.date = QDateEdit(self) #Gün ay ayıl bilgisini içerir
        self.datetime = QDateTimeEdit(self) #Saat tarih gün ay yıl bilgisini içerir
        
        self.time.setTime(QTime.currentTime())
        self.date.setDate(QDate.currentDate())  
        self.datetime.setDateTime(QDateTime.currentDateTime())
        
        time = QTime(12,12,12)
        time2 = QTime(0,0,0)
        date = QDate(2011,11,11)
        date2 = QDate(2012,12,12)

        self.time.setTime(time)
        self.date.setDate(date)

        self.time.setGeometry(10,10,200,40)
        self.date.setGeometry(250,10,200,40)
        self.datetime.setGeometry(480,10,240,40)

        self.time.setFont(QFont("Consolas",18))
        self.date.setFont(QFont("Consolas",18))
        self.datetime.setFont(QFont("Consolas",18))

        self.time.setTimeRange(time2, time) #Max ve min time ayarlama
        self.date.setDateRange(date, date2) 

        self.resize(600,600)
        self.show()

app = QApplication([])
window = main()
app.exec() 