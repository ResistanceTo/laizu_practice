from PySide2 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_layout.setSpacing(0)



def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    # 增加任务栏图标
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("d.ico"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
    gui.setWindowIcon(icon)
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()