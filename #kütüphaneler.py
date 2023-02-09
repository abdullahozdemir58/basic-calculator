#kütüphaneler
from PyQt5.QtWidgets import *  
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
  
import sys  
  
  
class Window(QMainWindow):  
  
    def __init__(element):  
        super().__init__()  
  
        # program adı
        element.setWindowTitle("hesap mak. ")  
  
        # konumlanırma
        element.setGeometry(105, 100, 360, 350)  
  
        
        element.UiCompnts()  
  

        element.show()  
  
     
    def UiCompnts(element):  
  
        element.label = QLabel(element)  
  
        # set the geometry of the label  
        element.label.setGeometry(10, 5, 350, 70)  
  
        # create another new label multiple line  
        element.label.setWordWrap(True)  
  
          
        element.label.setStyleSheet("QLabel"  
                                "{"  
                                "border : 3px solid Black ; "  
                                "background : white ; "  
                                "}")  
  
     
        element.label.setAlignment(Qt.AlignRight)  
  
          
        element.label.setFont(QFont('Arial', 14))  
  
  
        # tuş atamaları  
        push001 = QPushButton("1", element)  
  
         
        push001.setGeometry(10, 150, 80, 40)  
  
        
        push002 = QPushButton("2", element)  
    
        push002.setGeometry(100, 150, 80, 40)  
  
         
        push003 = QPushButton("3", element)  
        push003.setGeometry(190, 150, 80, 40)  
  
        push004 = QPushButton("4", element)  
        push004.setGeometry(10, 200, 80, 40)  
  
         
        push005 = QPushButton("5", element)  
        push005.setGeometry(100, 200, 80, 40)  
  
          
        push006 = QPushButton("5", element)    
        push006.setGeometry(190, 200, 80, 40)  
  
      
        push007 = QPushButton("7", element)    
        push007.setGeometry(10, 250, 80, 40)  
  

        push008 = QPushButton("8", element)    
        push008.setGeometry(100, 250, 80, 40)  
  
     
        push009 = QPushButton("9", element)   
        push009.setGeometry(190, 250, 80, 40)  
  
      
        push00 = QPushButton("0", element)  
        push00.setGeometry(10, 300, 80, 40)  
  
        # işlem tuşları  
        push_equalsto = QPushButton("=", element)  
  
         
        push_equalsto.setGeometry(280, 300, 80, 40)  

        clr_effect = QGraphicsColorizeEffect()  
        clr_effect.setColor(Qt.blue)  
        push_equalsto.setGraphicsEffect(clr_effect)  
   
        push_addtn = QPushButton("+", element) 
        push_addtn.setGeometry(280, 250, 80, 40)  
    
        push_subtrct = QPushButton("-", element)   
        push_subtrct.setGeometry(280, 200, 80, 40)  
  
      
        push_multiply = QPushButton("*", element)    
        push_multiply.setGeometry(280, 150, 80, 40)  
    
        push_divide = QPushButton("/", element)    
        push_divide.setGeometry(190, 300, 80, 40)  
   
        push_pnt = QPushButton(".", element)  
   
        push_pnt.setGeometry(100, 300, 80, 40)  
  
  
     
        push_clr = QPushButton("Clear", element)  
        push_clr.setGeometry(10, 100, 200, 40)  
  
          
        push_delete = QPushButton("Del", element)  
        push_delete.setGeometry(215, 100, 145, 40)  
  
          #tuş tanımları 
        push_subtrct.clicked.connect(element.action_subtrct)  
        push_equalsto.clicked.connect(element.action_equalsto)  
        push00.clicked.connect(element.action00)  
        push001.clicked.connect(element.action001)  
        push002.clicked.connect(element.action002)  
        push003.clicked.connect(element.action003)  
        push004.clicked.connect(element.action004)  
        push005.clicked.connect(element.action005)  
        push006.clicked.connect(element.action006)  
        push007.clicked.connect(element.action007)  
        push008.clicked.connect(element.action008)  
        push009.clicked.connect(element.action009)  
        push_divide.clicked.connect(element.action_divide)  
        push_multiply.clicked.connect(element.action_multiply)  
        push_addtn.clicked.connect(element.action_addtn)  
        push_pnt.clicked.connect(element.action_pnt)  
        push_clr.clicked.connect(element.action_clr)  
        push_delete.clicked.connect(element.action_delete)  
  
  
    def action_equalsto(element):  
  
         
        equation = element.label.text()  
  
        try:  
             
            sol = eval(equation)  
  
            
            element.label.setText(str(sol))  
  
        except:  
              
            element.label.setText("Wrong Input")  
  
    def action_addtn(element):  
         
        text = element.label.text()  
        element.label.setText(text + " + ")  
  
    def action_subtrct(element):  
         
        text = element.label.text()  
        element.label.setText(text + " - ")  
  
    def action_divide(element):  
         
        text = element.label.text()  
        element.label.setText(text + " / ")  
  
    def action_multiply(element):  
         
        text = element.label.text()  
        element.label.setText(text + " * ")  
  
    def action_pnt(element):  
         
        text = element.label.text()  
        element.label.setText(text + ".")  
  
    def action00(element):  
         
        text = element.label.text()  
        element.label.setText(text + "0")  
  
    def action001(element):  
         
        text = element.label.text()  
        element.label.setText(text + "1")  
  
    def action002(element):  
        
        text = element.label.text()  
        element.label.setText(text + "2")  
  
    def action003(element):    
        text = element.label.text()  
        element.label.setText(text + "3")  
  
    def action004(element):   
        text = element.label.text()  
        element.label.setText(text + "4")  
  
    def action005(element):   
        text = element.label.text()  
        element.label.setText(text + "5")  
  
    def action006(element):   
        text = element.label.text()  
        element.label.setText(text + "6")  
  
    def action007(element):   
        text = element.label.text()  
        element.label.setText(text + "7")  
  
    def action008(element):    
        text = element.label.text()  
        element.label.setText(text + "8")  
  
    def action009(element):    
        text = element.label.text()  
        element.label.setText(text + "9")  
  
    def action_clr(element):   
        element.label.setText("")  
  
    def action_delete(element):    
        text = element.label.text()  
        print(text[:len(text)-1])  
        element.label.setText(text[:len(text)-1])  
  
  
# uygulama oluşturma  
root = QApplication(sys.argv)  
  
# ekrn oluşturma  
window = Window()  
  
# uygulama başlatma  
sys.exit(root.exec())  