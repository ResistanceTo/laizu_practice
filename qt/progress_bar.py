from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # 显示窗体内容

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 50, 200, 25)  #设置进度条位置及大小
        self.btn = QPushButton('开始', self)
        self.btn.move(50, 90)
        self.btn.clicked.connect(
            self.doAction)  #点击按钮时执行的动作函数指定为self.doAction()
        # self.btn.setGeometry(50, 90, 40, 25)

        self.timer = QBasicTimer()  #构建一个计数器
        self.step = 0  #设置基数
        self.setGeometry(300, 300, 280, 170)  # 设置整个窗体的大小
        self.setWindowTitle('进度条')  #设置窗口标题
        # self.setWindowIcon('logo2.png') #设置窗口图标
        self.show()

    def timerEvent(self, *args, **kwargs):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.step += 1
        self.pbar.setValue(self.step)  #timer每次重围时将self.step 赋值给pbar

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100, self)
            self.btn.setText('停止')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个QT应用对象
    ex = Example()
    sys.exit(app.exec_())
