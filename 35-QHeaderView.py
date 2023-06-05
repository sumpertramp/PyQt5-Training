#QHeaderView, tablo ve liste gibi veri gösterme widget'larında kullanılan
#bir sınıftır. Genellikle başlıkları veya sütun başlıklarını görüntülemek
#ve düzenlemek için kullanılır. Bu sınıf, başlık sıralamasını sağlar, 
#sütunların boyutunu ayarlamaya izin verir ve kullanıcıların başlıkları 
#yeniden düzenlemesine olanak tanır.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)
        self.tree = QTreeWidget()
        self.table = QTableWidget(5,5)
        self.hbox.addWidget(self.tree)
        self.hbox.addWidget(self.table)

        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(["Header1", "Header2", "Header3"])
        self.table.setHorizontalHeaderLabels(["Header1", "Header2", "Header3"])

        self.tree.header().count() #Başlık sayısını sayma
        self.table.horizontalHeader().count() #Başlık sayısını sayma

        #İstediğimiz başlığı gizleme özelliği
        self.tree.header().hideSection(2)
        self.table.horizontalHeader().hideSection(2)

        #Geri getirme
        self.tree.header().showSection(2)
        self.table.horizontalHeader().showSection(2)

        #self.tree.header().setMaximumSectionSize(10)
        self.tree.header().setMinimumSectionSize(150)
        self.tree.header().setDefaultSectionSize(10) #Hepsi kapalı açıldı
        self.tree.header().setStretchLastSection(False) #Stretch özelliğini kapatma

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed) # Yatay başlık alanında sütun boyutlarının sabitlenmesi modunu ayarlar.
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive) # Yatay başlık alanında sütun boyutlarının etkileşimli modunu ayarlar.
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # Yatay başlık alanındaki sütunların içeriğine göre boyutlandırma modunu ayarlar.
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Yatay başlık alanındaki sütunların gerilmeli modunu ayarlar.
        
        self.tree.header().setSectionsClickable(True) # Ağaç görünümü başlığında bölümlerin tıklanabilir olmasını sağlar.
        self.table.horizontalHeader().setSectionsClickable(False) # Tablo yatay başlık alanında bölümlerin tıklanabilir olmamasını sağlar.

        
        # self.tree.header().setSectionsMovable(False) # Ağaç görünümü başlığında bölümlerin taşınabilir olmamasını sağlar.
        self.table.horizontalHeader().setSectionsMovable(True) # Tablo yatay başlık alanında bölümlerin taşınabilir olmasını sağlar.
        

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()