#QText edit yapı itibari ile lineedite benziyor. 
#Farkları html kodlarını içeriyor olması ve
#Birden çok satır içerebiliyor olması
#PlainTextEdit appentHtml kullanılarak html alır hale getirilebilir

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.text_edit.setText("Bir örnek yazıdır")

        self.text_edit.setCursorWidth(18) #İmleç kalınlığı ayarlama
        self.text_edit.setAcceptRichText(False) #html özelliğini kaldırma

        self.plain = QPlainTextEdit(self) #html özelliği yok
        self.plain.setPlainText("Örnek Yazıdır.")
        self.plain.move(400,0)
        self.plain.appendHtml("<b>Kalın yazı.<b>") # plainTextEdit'e html ekleme

        self.button = QPushButton("insert", self)
        self.button.clicked.connect(self.insert)
        self.button.move(0,350)

        self.text_edit.setFont(QFont("Tahoma", 30))
        
        self.resize(700,700)
        self.show()
    def insert(self):
        #self.text_edit.insertHtml("<b>Kalın yazı.<b>")
        #self.text_edit.insertPlainText("<b>Kalın yazı.<b>")

        self.text_edit.setFontFamily("Verdana") #Seçilen metni butona tıkladıkdan onra yazı tipi değiştirme
        self.text_edit.setFontPointSize(10) #Seçilen metnin butona tıklayınca yazı boyutunu değiştirme

app = QApplication([])
window = main()
app.exec()        