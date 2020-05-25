

# 数值和进度条联动
# import sys
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
#     QVBoxLayout, QApplication)
 
 
# class Example(QWidget):
    
#     def __init__(self):
#         super().__init__()
        
#         self.initUI()
        
        
#     def initUI(self):
        
#         lcd = QLCDNumber(self)
#         sld = QSlider(Qt.Horizontal, self)
 
#         vbox = QVBoxLayout()
#         vbox.addWidget(lcd)
#         vbox.addWidget(sld)
 
#         self.setLayout(vbox)
#         sld.valueChanged.connect(lcd.display)
        
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Signal & slot')
#         self.show()
        
 
# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# 多个按钮绑定同一个槽，分辨是哪个按钮
# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
 
 
# class Example(QMainWindow):
    
#     def __init__(self):
#         super().__init__()
        
#         self.initUI()
        
        
#     def initUI(self):      
 
#         btn1 = QPushButton("Button 1", self)
#         btn1.move(30, 50)
 
#         btn2 = QPushButton("Button 2", self)
#         btn2.move(150, 50)
      
#         btn1.clicked.connect(self.buttonClicked)            
#         btn2.clicked.connect(self.buttonClicked)
        
#         self.statusBar()
        
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event sender')
#         self.show()
        
        
#     def buttonClicked(self):
      
#         sender = self.sender()
#         self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# 点击按钮出现选色板，且可以改变frame的颜色
# import sys
# from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
#     QColorDialog, QApplication)
# from PyQt5.QtGui import QColor
 
 
# class Example(QWidget):
    
#     def __init__(self):
#         super().__init__()
        
#         self.initUI()
        
        
#     def initUI(self):      
 
#         col = QColor(0, 0, 0) 
 
#         self.btn = QPushButton('Dialog', self)
#         self.btn.move(20, 20)
 
#         self.btn.clicked.connect(self.showDialog)
 
#         self.frm = QFrame(self)
#         self.frm.setStyleSheet("QWidget { background-color: %s }" 
#             % col.name())
#         self.frm.setGeometry(130, 22, 100, 100)            
        
#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Color dialog')
#         self.show()
        
        
#     def showDialog(self):
      
#         col = QColorDialog.getColor()
 
#         if col.isValid():
#             self.frm.setStyleSheet("QWidget { background-color: %s }"
#                 % col.name())
            
        
# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, 
    QSizePolicy, QLabel, QFontDialog, QApplication)
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
 
        vbox = QVBoxLayout()
 
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        
        btn.move(20, 20)
 
        vbox.addWidget(btn)
 
        btn.clicked.connect(self.showDialog)
        
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
 
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)          
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')
        self.show()
        
        
    def showDialog(self):
 
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())