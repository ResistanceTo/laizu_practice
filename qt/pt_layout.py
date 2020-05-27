# '''
# 绝对布局方式,通过move的XY坐标方式来控制控件的位置
# '''
# from PyQt5.QtWidgets import *
# import sys, math

# class absolutelayout(QWidget):
#     def __init__(self):
#         super(absolutelayout, self).__init__()
#         self.setWindowTitle("绝对布局方式")
#         self.label1 = QLabel("欢迎", self)
#         self.label1.move(15, 20)

#         self.label2 = QLabel("欢迎", self)
#         self.label2.move(35, 40)

#         self.label3 = QLabel("欢迎", self)
#         self.label3.move(55, 80)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = absolutelayout()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 水平盒布局方式
# '''
# from PyQt5.QtWidgets import *
# import sys, math

# class hboxlayout(QWidget):
#     def __init__(self):
#         super(hboxlayout, self).__init__()
#         self.setWindowTitle("水平盒布局方式")
#         self.layout = QHBoxLayout()

#         self.label1 = QLabel("欢迎")
#         self.label2 = QLabel("欢迎")
#         self.label3 = QLabel("欢迎")
#         self.label4 = QLabel("欢迎")
#         self.label5 = QLabel("欢迎")

#         self.layout.addWidget(self.label1)
#         self.layout.addWidget(self.label2)
#         self.layout.addWidget(self.label3)
#         self.layout.addWidget(self.label4)
#         self.layout.addWidget(self.label5)

#         # 设置水平盒布局的控件间距大小
#         self.layout.setSpacing(100)
#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = hboxlayout()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 设置控件的伸缩量
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class absolutelayout(QWidget):
#     def __init__(self):
#         super(absolutelayout, self).__init__()
#         self.setWindowTitle("设置伸缩量")
#         self.resize(800, 100)
#         self.layout = QHBoxLayout()

#         self.btn1 = QPushButton("按钮1")
#         self.btn2 = QPushButton("按钮2")
#         self.btn3 = QPushButton("按钮3")
#         self.btn4 = QPushButton("按钮4")
#         self.btn5 = QPushButton("按钮5")

#         #将前五个按钮放在左边显示
#         self.layout.addStretch(0)  #设置布局的伸缩量-默认右对齐方式
#         self.layout.addWidget(self.btn1)
#         self.layout.addWidget(self.btn2)
#         self.layout.addWidget(self.btn3)
#         self.layout.addWidget(self.btn4)
#         self.layout.addWidget(self.btn5)

#         #将第6个和第7个按钮放在右边显示
#         self.btn6 = QPushButton("按钮6")
#         self.btn7 = QPushButton("按钮7")
#         self.layout.addStretch(1)
#         self.layout.addWidget(self.btn6)
#         self.layout.addWidget(self.btn7)

#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = absolutelayout()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 水平盒布局方式控件对齐方式
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class absolutelayout(QWidget):
#     def __init__(self):
#         super(absolutelayout, self).__init__()
#         self.setWindowTitle("控件对齐方式")
#         self.layout = QHBoxLayout()

#         self.label1 = QLabel("欢迎")
#         self.label2 = QLabel("欢迎")
#         self.label3 = QLabel("欢迎")
#         self.label4 = QLabel("欢迎")
#         self.label5 = QLabel("欢迎")

#         #设置水平盒布局的对齐方式layout.addwidget(控件，控件位置长度比例，对齐方式)
#         self.layout.addWidget(self.label1, 2, Qt.AlignLeft | Qt.AlignTop)
#         self.layout.addWidget(self.label2, 1, Qt.AlignLeft | Qt.AlignTop)
#         self.layout.addWidget(self.label3, 1, Qt.AlignLeft | Qt.AlignBottom)
#         self.layout.addWidget(self.label4, 1, Qt.AlignLeft | Qt.AlignBottom)
#         self.layout.addWidget(self.label5, 1, Qt.AlignLeft)

#         # 设置水平盒布局的控件间距大小
#         self.layout.setSpacing(20)
#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = absolutelayout()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 垂直盒布局方式
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class vboxlayout(QWidget):
#     def __init__(self):
#         super(vboxlayout, self).__init__()
#         self.setWindowTitle("垂直盒布局方式")
#         self.resize(100, 2000)
#         self.layout = QVBoxLayout()

#         self.label1 = QPushButton("欢迎")
#         self.label2 = QPushButton("欢迎")
#         self.label3 = QPushButton("欢迎")
#         self.label4 = QPushButton("欢迎")
#         self.label5 = QPushButton("欢迎")

#         #设置垂直盒布局的对齐方式layout.addwidget(控件，控件位置长度比例，对齐方式)
#         self.layout.addWidget(self.label1)
#         self.layout.addWidget(self.label2)
#         self.layout.addWidget(self.label3)
#         self.layout.addWidget(self.label4)
#         self.layout.addWidget(self.label5)

#         # 设置垂直盒布局的控件间距大小
#         self.layout.setSpacing(20)
#         self.setLayout(self.layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = vboxlayout()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 将按钮永远放在窗口的右下角
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class rightbutton(QWidget):
#     def __init__(self):
#         super(rightbutton, self).__init__()
#         self.setWindowTitle("按钮放在窗口的右下角")
#         self.resize(400, 300)

#         ok = QPushButton("确定")
#         cancel = QPushButton("取消")

#         h = QHBoxLayout()
#         h.addStretch(1)
#         h.addWidget(ok)
#         h.addWidget(cancel)

#         v = QVBoxLayout()
#         bt1 = QPushButton("按钮1")
#         bt2 = QPushButton("按钮2")
#         bt3 = QPushButton("按钮3")

#         v.addStretch(0)  #放在上面
#         v.addWidget(bt1)
#         v.addWidget(bt2)
#         v.addWidget(bt3)

#         v.addStretch(1)  #始终保持在放在右下角
#         v.addLayout(h)
#         self.setLayout(v)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = rightbutton()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 实现计算器功能
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class calcu(QWidget):
#     def __init__(self):
#         super(calcu, self).__init__()
#         self.setWindowTitle("栅格布局实现计算器UI")
#         self.resize(400, 300)
#         grid = QGridLayout()

#         names = [
#             "CLS", "Back", "", "Close", "7", "8", "9", "/", "4", "5", "6", "*",
#             "1", "2", "3", "-", "0", ".", "=", "+"
#         ]
#         positions = [(i, j) for i in range(5) for j in range(4)]

#         for position, name in zip(positions, names):  #采用zip组合循环的方式来进行对象的匹配
#             if name == "":
#                 continue
#             print(position)
#             print(name)
#             b = QPushButton(name)
#             # grid.addWidget(b, position[0], position[1])  #放置控件名称，位置坐标x,位置坐标y
#             grid.addWidget(b, *position)  #  *p表示将元组（x,y）转换为x y

#         self.setLayout(grid)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = calcu()
#     p.show()
#     sys.exit(app.exec_())

'''
实现表单设计
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys, math

class table(QWidget):
    def __init__(self):
        super(table, self).__init__()
        self.setWindowTitle("栅格布局实现表单UI设计")
        #self.resize(400,300)
        grid = QGridLayout()

        label1 = QLabel("标题")
        label2 = QLabel("作者")
        label3 = QLabel("内容")

        l1 = QLineEdit()
        l2 = QLineEdit()
        l3 = QTextEdit()
        grid.setSpacing(10)

        grid.addWidget(label1, 1, 0)
        grid.addWidget(l1, 1, 1)

        grid.addWidget(label2, 2, 0)
        grid.addWidget(l2, 2, 1)

        grid.addWidget(label3, 3, 0, 5, 1, Qt.AlignCenter)  #占据伸缩比为5行1列
        grid.addWidget(l3, 3, 1, 5, 1)  #占据比例为5行1列

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = table()
    p.show()
    sys.exit(app.exec_())

# '''
# 实现表单设计
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math

# class tab(QWidget):
#     def __init__(self):
#         super(tab, self).__init__()
#         self.setWindowTitle("表单布局")
#         form = QFormLayout()

#         label1 = QLabel("标题")
#         label2 = QLabel("作者")
#         label3 = QLabel("内容")

#         l1 = QLineEdit()
#         l2 = QLineEdit()
#         l3 = QTextEdit()

#         # 表单布局直接使用addrow(函数)进行表单布局的放置
#         form.addRow(label1, l1)
#         form.addRow(label2, l2)
#         form.addRow(label3, l3)
#         self.setLayout(form)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = tab()
#     p.show()
#     sys.exit(app.exec_())

# '''
# 改变不同控件之间的边界
# '''
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import sys, math


# class splitter(QWidget):
#     def __init__(self):
#         super(splitter, self).__init__()
#         self.setWindowTitle("拖动控件之间的边界")
#         self.setGeometry(300, 300, 300, 200)

#         topleft = QFrame()
#         topleft.setFrameShape(QFrame.StyledPanel)

#         bottom = QTextEdit("编辑器")

#         #设置所包含的控件之间可以水平拖动，基本设置为水平布局
#         splitter1 = QSplitter(Qt.Horizontal)

#         text = QTextEdit("代码区")
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(text)

#         #设置默认的控件之间的大小距离
#         splitter1.setSizes([100, 200])

#         #设置所包含的控件之间可以垂直拖动，设置我垂直布局
#         splitter2 = QSplitter(Qt.Vertical)

#         text = QTextEdit()
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)

#         h = QVBoxLayout()
#         h.addWidget(splitter2)
#         self.setLayout(h)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     p = splitter()
#     p.show()
#     sys.exit(app.exec_())
