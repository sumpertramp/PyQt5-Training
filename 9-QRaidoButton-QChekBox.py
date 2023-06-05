#Seçim kutucukları olarak kullanılabilir.
#Radio Buttondaki seçeneklerden sadece birisi seçilebilir.
#CheckBox'da ise seçeneklerden birden fazlası seçilebilir


from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.radio1 = QRadioButton("Male", self)
        self.radio2 = QRadioButton("Female", self)
        
        self.radio2.move(60,0)
        
        #Farklı bir radiobutton grubu varsa farklı bir widget oluşturulur.
        self.widget = QWidget(self)
        self.widget.setGeometry(300,100,200,200)

        self.radio3 = QRadioButton ("Marry", self.widget)
        self.radio4 = QRadioButton ("Single", self.widget)
        self.radio4.move(60,0)

        self.label = QLabel("What cities have you visited so far?", self)
        self.check1 = QCheckBox("London", self)
        self.check2 = QCheckBox( "Paris", self)
        self.check3 = QCheckBox( "Istanbul", self)
        self.check1.setIcon(QIcon("Ball.png"))
        
        self.label.move(20,80)
        self.check1.move(20,120)
        self.check2.move(80,120)
        self.check3.move(140,120)

        self.check3.setCheckable(False) #Bu özellik butonun seçilebilir olmasını kaldırır. Radio Button için de geçerlidir.
        
        self.radio3.setChecked(True) #Varsayılan olarak seçilmiş halde gelir
        self.check2.setChecked(True)

        boolean = self.check2.isChecked()  #Seçimleri bir yere true ya da false olarak bir yere kaydetmek için kullanılır.
        print(boolean)
        
        self.resize(800,500)
        self.show()

app = QApplication([])
window = main()
app.exec()