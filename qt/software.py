'''
实现表单设计
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys, math


class table(QWidget):
    def __init__(self):
        super(table, self).__init__()
        self.setWindowTitle("测试软件")
        #self.resize(400,300)
        grid = QGridLayout()

        label1 = QLabel("姓名")
        label2 = QLabel("省市县")
        label3 = QLabel("详细地址")
        label4 = QLabel("办理业务")
        label5 = QLabel("是否贵宾")
        label6 = QLabel("手机号码")
        label7 = QLabel("电话号码")

        l1 = QLineEdit()
        l2 = QLineEdit()
        l3 = QLineEdit()
        l4 = QLineEdit()
        l5 = QLineEdit()
        l6 = QLineEdit()

        b1 = QPushButton("提交")
        b2 = QPushButton("清空")
        b3 = QPushButton("测试")

        q1 = QComboBox()
        q1.addItem("办卡")
        q1.addItem("资讯")
        q1.addItem("存款")
        q1.addItem("取款")

        r1 = QRadioButton("是")
        r2 = QRadioButton("否")
        grid.setSpacing(10)

        grid.addWidget(label1, 1, 0)
        grid.addWidget(l1, 1, 1)

        grid.addWidget(label2, 2, 0)
        grid.addWidget(l2, 2, 1)
        grid.addWidget(label3, 2, 3)
        grid.addWidget(l3, 2, 4)

        grid.addWidget(label4, 3, 0)
        grid.addWidget(q1, 3, 1)
        grid.addWidget(label5, 4, 0)
        grid.addWidget(r1, 4, 1)
        grid.addWidget(r2, 4, 2)

        grid.addWidget(label6, 5, 0)
        grid.addWidget(l4, 5, 1)
        grid.addWidget(label7, 6, 0)
        grid.addWidget(l5, 6, 1)
        grid.addWidget(l6, 6, 2)

        grid.addWidget(b1, 7, 0)
        grid.addWidget(b2, 7, 1)
        grid.addWidget(b3, 7, 2)

        # grid.addWidget(label3, 3, 0, 5, 1, Qt.AlignCenter)#占据伸缩比为5行1列
        # grid.addWidget(l3, 3, 1, 5, 1)  #占据比例为5行1列

        self.setLayout(grid)

        b2.clicked.connect(l1.clear)
        b2.clicked.connect(l2.clear)
        b2.clicked.connect(l3.clear)
        b2.clicked.connect(l4.clear)
        b2.clicked.connect(l5.clear)
        b2.clicked.connect(l6.clear)
        b2.clicked.connect(r2.click)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    p = table()
    p.show()
    sys.exit(app.exec_())