from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, qApp, QAction, QDesktopWidget, QWidget
import sys


class SystemTray:
    def __init__(self, qw):
        super().__init__()
        self.app = app
        self.qw = qw
        QApplication.setQuitOnLastWindowClosed(False)

        self.qw.show()
        self.tp = QSystemTrayIcon(self.qw)
        self.initTrayIcon()
        self.run()

    def initTrayIcon(self):
        self.tp.setIcon(QIcon('./d.ico'))

    def quitApp(self):
        self.qw.show()
        re = QMessageBox.question(self.qw, "info", "quit",
                                  QMessageBox.Yes | QMessageBox.No,
                                  QMessageBox.No)
        if re == QMessageBox.Yes:
            self.tp.setVisible(False)
            qApp.quit()

    def message(self):
        # 提示信息被点击方法
        print("弹出的信息被点击了")

    def act(self, reason):
        # 主界面显示方法
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            self.qw.show()

    def run(self):
        self.a1 = QAction('显示', triggered=self.qw.show)
        self.a2 = QAction('退出', triggered=self.quitApp)
        self.logMenu = QMenu("日志")
        self.a3 = QAction('启用', checkable=True)
        self.a4 = QAction('禁用', checkable=True)
        self.proxyMenu = QMenu("代理")
        self.a5 = QAction('自动获取', checkable=True)
        self.a6 = QAction('手动获取', checkable=True)
        self.a7 = QAction('关闭获取', checkable=True)
        self.logMenu.addAction(self.a3)
        self.logMenu.addAction(self.a4)
        self.proxyMenu.addAction(self.a5)
        self.proxyMenu.addAction(self.a6)
        self.proxyMenu.addAction(self.a7)
        self.tpMenu = QMenu()
        self.tpMenu.addAction(self.a1)
        self.tpMenu.addSeparator()
        self.tpMenu.addMenu(self.logMenu)
        self.tpMenu.addSeparator()
        self.tpMenu.addMenu(self.proxyMenu)
        self.tpMenu.addSeparator()
        self.tpMenu.addAction(self.a2)
        self.tp.setContextMenu(self.tpMenu)
        self.tp.show()
        self.tp.showMessage('hello', 'Yes', icon=0)
        self.tp.messageClicked.connect(self.message)
        self.tp.activated.connect(self.act)
        sys.exit(self.app.exec_())


class Window(QWidget):
    # 主窗口类
    def __init__(self):
        # move()方法移动了窗口到屏幕坐标x=300, y=300的位置.
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        # 主窗口布局实现略。。。
        self.setWindowTitle('Test')  # 设置标题
        self.setWindowIcon(QIcon('./d.ico'))  # 设置标题图标
        self.resize(300, 250)  # 设置窗体大小
        self.setFixedSize(self.width(), self.height())  # 固定窗口大小
        self.center()  # 窗体屏幕居中显示
        self.tray()  # 程序实现托盘

    def tray(self):
        # 创建托盘程序
        ti = SystemTray(self)

    def center(self):
        # 窗口居中方法
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    # 创建一个app程序
    app = QApplication(sys.argv)
    # 创建窗口
    win = Window()
    sys.exit(app.exec_())
