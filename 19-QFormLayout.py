#QFormLayout, PyQt ve Qt Framework tarafından sağlanan bir layout (düzen) sınıfıdır. 
#Bu sınıf, kullanıcıların form elemanlarını (etiket, metin kutusu, spin box, vs.) 
#kolayca düzenlemesine ve düzenlemesine olanak tanır.
#QFormLayout, genellikle bir form veya diyalog kutusunda kullanılır ve her satırda 
#bir etiket ve bir form elemanı bulunur. Bu elemanlar, kullanıcının bir giriş 
#yapmasına veya bir seçim yapmasına izin verir.
#QFormLayout, form elemanlarını yatay olarak düzenlemek için QHBoxLayout veya dikey 
#olarak düzenlemek için QVBoxLayout ile birlikte kullanılabilir. Her form elemanı, 
#QLabel veya QLineEdit gibi uygun bir widget ile birlikte QFormLayout'a eklenir. 
#QLabel, etiket olarak kullanılırken, QLineEdit, spin box veya diğer widget'lar, 
#form elemanı olarak kullanılır.
#QFormLayout, otomatik olarak etiketler ve form elemanları arasında boşluklar ekler 
#ve etiketlerin hizalamasını kontrol etmek için birkaç farklı yöntem sağlar. Ayrıca, 
#satırları eklemek veya silmek için uygun yöntemler de sağlar.
#Özetle, QFormLayout, form tabanlı bir arayüz oluştururken widget'ları düzenlemek 
#için kullanışlı bir sınıftır. Bu sınıf, form elemanlarını etiketlerle kolayca 
#eşleştirmenize, arayüzü düzenli tutmanıza ve verileri kullanıcılardan toplamanıza 
#veya göstermenize yardımcı olur.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.form = QFormLayout(self)
        self.form.addWidget(QPushButton("Click"))
        self.form.setVerticalSpacing(50) #50'lik boşluk oluşturma
        self.form.setHorizontalSpacing(100) #100'lük yatay boşluk
        #Aynı satıra birden başka widgets eklemek istiyorsak addRow kullanılır
        
        self.button = QPushButton("Add")
        self.form.addRow(QLabel("Name:"), QLineEdit())
        self.form.addRow(QLabel("Surname:"), QLineEdit())

        self.form.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint) #Genişleme olayını iptal etme
        self.form.setFormAlignment(Qt.AlignBottom) #Aşağı doğru iteleme
        
        #Şu ana kadar 3 satır var. Satırlara indis vermek için:
        #self.form.removeRow(1) #1. indisli elemanı çıkarttık
        
        #self.form.removeRow(self.button) #Bunu kaldırmaz, çünkü bunun için indis bilgisi kullanmak gerekiyor
       
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()