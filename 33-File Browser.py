
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*
import os #İşletim sistemi ile çalışmak için eklendi
import time
class main(QWidget):
    def __init__(self):
        super().__init__()

        self.tree = QTreeWidget(self)
        self.tree.setGeometry(20,20,450,450)

        path = os.getcwd()
        top_text = path.split("\\")[-1]

        stat = os.stat(path)
        print(stat)

        self.item = QTreeWidgetItem()
        self.item.setText(0,top_text)
        self.tree.addTopLevelItem(self.item)
        self.tree.setColumnCount(4) #Kolon sayısını arttırma

        self.tree_setup(path, self.item)
        
        self.resize(800,500)
        self.show()
    
    def tree_setup(self, p, item):
        walk = os.walk(p)
        
        #"enumerate" kelimesi, Python programlama dilinde bir dizi, 
        #liste veya diğer yineleyiciler üzerinde yineleme yaparken 
        #elemanın indeksini ve değerini birlikte döndüren bir fonksiyon
        for i, j in enumerate(walk):
            if i == 0:
                for k, l in enumerate(j):
                    if k != 0:
                        for m in l:
                            stat = os.stat(p+"\\"+m)
                            timer = time.localtime(stat[-2])
                            file_time = "{}/{}/{}".format(timer[2],timer[1],timer[0])
                            
                            file_size = stat[-4]//1024 #Ondalıklı kısım oluşmasın diye
                            
                            item_child = QTreeWidgetItem()
                            item_child.setText(0, m)
                            item_child.setText(1,p)
                            item_child.setText(2, file_time)
                            item_child.setText(3, str(file_size)+ "KB")
                            item.addChild(item_child)

                            if os.path.isdir(p+"\\"+m):
                                print("BAŞARILI")
                                self.tree_setup(p + "\\" + m, item_child)


app = QApplication([])
window = main()
app.exec()