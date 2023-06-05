#QTreeWidget, PyQt ve Qt Framework'te kullanılan bir widget'tır. 
#PyQt, Python programlama dilini Qt Framework ile entegre eden bir 
#arayüz kütüphanesidir. QTreeWidget, ağaç yapılı verileri görüntülemek
#ve düzenlemek için kullanılan bir kullanıcı arayüzü öğesidir.
#QTreeWidget, ağaç yapısıyla ilişkilendirilmiş verileri hiyerarşik bir 
#şekilde görüntüler. Her bir öğe, ağaç yapısının düğümleri olarak temsil 
#edilir. Öğeler alt düğümlere (çocuklara) sahip olabilir ve böylece ağaç 
#yapısı oluşturulabilir. Öğeler, başlık, metin, simge veya özel veriler 
#gibi çeşitli özelliklerle ilişkilendirilebilir.
#QTreeWidget, kullanıcıların ağaç yapısını genişletebilmesine, 
#daraltabilmesine ve düzenleyebilmesine olanak tanır. Öğelerin 
#sürükle-bırak özelliği, düzenlemesi, gizlenmesi ve sıralanması gibi 
#işlemler de desteklenir. Ayrıca, kullanıcıların belirli bir öğeyle 
#ilgili eylemler gerçekleştirmek için bağlantılar ve olaylar oluşturmasına
#izin verir.
#QTreeWidget, genellikle büyük miktarda hiyerarşik veriyi temsil etmek 
#veya sunmak için kullanılır. Örneğin, dosya sistemi yapısını veya 
#kategori-alt kategori ilişkisini göstermek gibi senaryolarda
#kullanılabilir.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.tree = QTreeWidget(self)
        self.tree.setGeometry(20,20,300,450)
        self.tree.setHeaderLabel("Header")

        self.item1 = QTreeWidgetItem() #KEndi itemini oluşturmak zorundayız.
        self.item1.setText(0, "item 1") #İlk eleman sutunu
        self.item1.setText(1, "./") #Birinci sütundaki texti değiştirme
        self.item2 = QTreeWidgetItem()
        self.item2.setText(0, "Item 2")

        self.item3 = QTreeWidgetItem()
        self.item3.setText(0, "Item 3")

        self.tree.addTopLevelItem(self.item1) #İtemleri ekleme
        self.tree.addTopLevelItems([self.item2, self.item3]) #Küme olarak ekleme
        self.tree.insertTopLevelItem(2,self.item1.clone()) #İtemin clonunu ekleme

        self.tree.setHeaderItem(self.item2.clone()) #Başlığı item2'ye set etme

        self.tree.setColumnCount(3)
        self.tree.setHeaderLabels(["Klasör/Dosya", "Yolu", "Değiştirme Tarihi"])

        print(self.tree.topLevelItemCount) #İtem sayısını verir

        print(self.tree.topLevelItem(0).text(0)) #0ıncı itemin textini yazdırma
        print(self.tree.topLevelItem(0).text(1))

        self.tree.setCurrentItem(self.item1) #Güncel seçili item belirleme
        print(self.tree.currentItem().text(0))

        print(self.tree.indexOfTopLevelItem(self.item3)) #item3'ün indeksini alma

        #self.item1.addChild() #sadece 1 item ekleme
        self.item1.addChildren([self.item2.clone(), self.item2.clone(), self.item2.clone()])
        #self.tree.setItemsExpandable(False) #Açılma olayını ekleme

        self.tree.expandItem(self.item1) #İtemi açık getirme
        self.tree.collapseItem(self.item1) #Tekrar kapalı getirmeye ayarlama

         
        
        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()