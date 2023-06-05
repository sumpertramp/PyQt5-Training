#Crome tab düzenini taklit etme

from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

css ="""
    QTabBar::tab{
       width: 100px;
       height: 35px;
       padding-right: 90px;
       border: none;
       }
    
    QTabBar::tab::hover{
       background-color: whitesmoke;
    }

    QTabBar::tab::selected{
       background-color:white;
       border-top-left-radius: 8px;
       border-top-right-radius: 8px;
    }
   
   QTabBar::close-button{
    image: url(x.png);
    padding: 3px;
    border-radius: 8px;
    }
    
    QTabBar::close-button::hover{
    background-color:#bbb;
    }
"""
class main(QWidget):
    def __init__(self):
        super().__init__()

        self.hbox = QHBoxLayout(self)
        self.hbox.setContentsMargins(0,0,0,0)

        self.tab_widget = QTabWidget()
        self.hbox.addWidget(self.tab_widget)

        self.tab_widget.addTab(QWidget(), "Tab1")
        self.tab_widget.addTab(QWidget(), "Tab2")
        self.tab_widget.addTab(QWidget(), "Tab3")

        self.tab_widget.setStyleSheet(css)
        self.tab_widget.setTabsClosable(True)

        self.tab_widget.tabCloseRequested.connect(self.tab_close) #Çarpıya basılan tabın indexini verir

        self.tbutton = QToolButton(self.tab_widget)
        self.tbutton.setText("+")
        w= self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+8, 4)
        self.tbutton.setFont(QFont("Calibri", 16))
        self.tbutton.setStyleSheet("QToolButton{padding: 0 0 2px 2px;border:none; height:22px; border-radius:12px; width:22px;}QToolButton::hover{background-color: #bbb;}QToolButton::pressed{background-color: #ddd;}")
        self.tbutton.clicked.connect(self.add_tab)
        
        self.resize(700,700)
        self.show()
    
    def tab_close(self, i):
        self.tab_widget.removeTab(i)
        #Pencere kapatılınca +'nın en sağdaki tabın kenarına gelmesi:
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+8,5)
    
    def add_tab(self):
        self.tab_widget.addTab(QWidget(),"New tab")
        w = self.tab_widget.tabBar().sizeHint().width()
        self.tbutton.move(w+8,5)
app = QApplication([])
window = main()
app.exec()