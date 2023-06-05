#QAbstractItemView, PyQt ve Qt framework'ünün bir parçası olan bir 
#sınıftır. Bu sınıf, kullanıcıya bir veri modelini temsil eden ve verilerin
# görüntülendiği bir arayüz sağlar. PyQt'de QAbstractItemView, tablo (QTableView), ağaç (QTreeView), liste (QListView) gibi çeşitli görünüm sınıflarının temel sınıfıdır.
#QAbstractItemView, model-view-controller (MVC) tasarım desenine dayalıdır.
#Bu desen, veri kaynağını (model), kullanıcı arayüzünü (görünüm) ve aralarında iletişimi sağlayan bir kontrolcüyü ayırarak uygulamanın esnekliğini artırır. QAbstractItemView, bu yapıda görünüm görevini üstlenir ve veri modeliyle etkileşim halinde kullanıcıya verileri gösterir.
#QAbstractItemView sınıfı, verileri görüntülemek için çeşitli yöntemler 
#ve özellikler sağlar. Örneğin, verilerin düzenlenebilmesini sağlar, 
#seçili öğeleri belirleyebilir, sıralama ve filtreleme işlemleri yapabilir,
#özelleştirilmiş hücre düzenleri ve stilleri uygulayabilir ve veri 
#değişikliklerini takip edebilir.
#Bu sınıf ayrıca kullanıcının görünümdeki verilere etkileşimde 
#bulunmasını da sağlar. Örneğin, kullanıcı tıklamaları, fare hareketleri
#ve klavye girişleri gibi olayları işleyerek kullanıcının verilere 
#erişimini ve etkileşimini sağlar.
#QAbstractItemView, veri tabanlı uygulamalar, liste görüntüleme, 
#tablo görüntüleme veya ağaç görüntüleme gibi farklı senaryolarda 
#kullanılabilir. Bu sınıf, verilerin düzenli bir şekilde görüntülenmesi,
#düzenlenmesi ve yönetilmesi için güçlü bir temel sağlar.

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)
        self.list = QListWidget()
        self.tree = QTreeWidget()
        self.table = QTableWidget(10,3)

        self.tree.setColumnCount(3)

        self.hbox.addWidget(self.list)
        self.hbox.addWidget(self.tree)
        self.hbox.addWidget(self.table)

        self.list.addItems(["Kalem", "Kitap", "Cetvel", "Sikgi", "Defter"])
        self.item = QTreeWidgetItem()
        self.item.setText(0, "Item")
        self.tree.addTopLevelItems([self.item, self.item.clone(), self.item.clone(), self.item.clone(),self.item.clone(), self.item.clone()])

        self.list.setAlternatingRowColors(True) # Liste görünümünde alternatif satır renklendirmesini etkinleştirir.
        self.tree.setAlternatingRowColors(True) # Ağaç görünümünde alternatif satır renklendirmesini etkinleştirir.
        self.table.setAlternatingRowColors(True) # Tablo görünümünde alternatif satır renklendirmesini etkinleştirir.

        '''self.list.setSelectionMode(QAbstractItemView.SingleSelection) # Liste görünümünde tekli seçim modunu ayarlar.
        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)  # Ağaç görünümünde tekli seçim modunu ayarlar.
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)  # Tablo görünümünde tekli seçim modunu ayarlar.
        
        self.list.setSelectionMode(QAbstractItemView.MultiSelection) # Liste görünümünde tekli seçim modunu ayarlar.
        self.tree.setSelectionMode(QAbstractItemView.MultiSelection)  # Ağaç görünümünde çoklu seçim modunu ayarlar.
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)  # Tablo görünümünde çoklu seçim modunu ayarlar.

        self.list.setSelectionMode(QAbstractItemView.ExtendedSelection) # Liste görünümünde tekli seçim modunu ayarlar.
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Ağaç görünümünde çoklu seçim modunu ayarlar.
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)  # Tablo görünümünde çoklu seçim modunu ayarlar.

        self.list.setSelectionBehavior(QAbstractItemView.SelectItems) # Listede seçim davranışını, yalnızca öğelerin seçilmesine izin vermek olarak ayarlar.
        self.tree.setSelectionBehavior(QAbstractItemView.SelectItems) # Ağaçta seçim davranışını, yalnızca öğelerin seçilmesine izin vermek olarak ayarlar.
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems) # Tabloda seçim davranışını, yalnızca öğelerin seçilmesine izin vermek olarak ayarlar.

        self.list.setSelectionBehavior(QAbstractItemView.SelectRows) # Listede seçim davranışını, yalnızca satırların seçilmesine izin vermek olarak ayarlar.
        self.tree.setSelectionBehavior(QAbstractItemView.SelectRows) # Ağaçta seçim davranışını, yalnızca satırların seçilmesine izin vermek olarak ayarlar.
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows) # Tabloda seçim davranışını, yalnızca satırların seçilmesine izin vermek olarak ayarlar.

        self.list.setSelectionBehavior(QAbstractItemView.SelectColumns) # Listede seçim davranışını, yalnızca sütunların seçilmesine izin vermek olarak ayarlar.
        self.tree.setSelectionBehavior(QAbstractItemView.SelectColumns) # Ağaçta seçim davranışını, yalnızca sütunların seçilmesine izin vermek olarak ayarlar.
        self.table.setSelectionBehavior(QAbstractItemView.SelectColumns) # Tabloda seçim davranışını, yalnızca sütunların seçilmesine izin vermek olarak ayarlar.'''

        self.list.setDragEnabled(True) # Liste üzerinde sürükle ve bırak işlemini etkinleştirir.
        self.tree.setDragEnabled(True) # Tree üzerinde sürükle ve bırak işlemini etkinleştirir.
        self.table.setDragEnabled(True) # Table üzerinde sürükle ve bırak işlemini etkinleştirir.
        
        self.list.setDragDropMode(QAbstractItemView.DragDrop) # Liste üzerinde sürükle ve bırak işlemi için sürükle ve bırak modunu ayarlar. Kullanıcı, tablodaki öğeleri sürükleyip bırakarak veri taşıyabilir veya başka bir bileşene bırakabilir.
        self.tree.setDragDropMode(QAbstractItemView.DragDrop) 
        self.table.setDragDropMode(QAbstractItemView.InternalMove)  #Tam taşıma işlemi, kopyasının kalmaması durumu

        self.resize(700,700)
        self.show()

app = QApplication([])
window = main()
app.exec()