import keyboard  #监听键盘
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QWidget, QShortcut, QLabel, QApplication, QHBoxLayout

class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("Try Ctrl+a", self)
        self.shortcut = QShortcut(QKeySequence("Ctrl+a"), self)
        self.shortcut.activated.connect(self.on_open)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
        self.resize(150, 100)
        self.show()
        # keyboard.add_hotkey('ctrl+alt', self.test, args=('b',))
        keyboard.add_hotkey('f1', self.test_a)
        keyboard.add_hotkey('ctrl+alt', self.quit_app)

    @pyqtSlot()
    def on_open(self):
        print("Opening!")

    def test_a(self):
        print('aaa')

    def test(self, x):
        print(x)

    def quit_app(self):
        print(1)
        del self
        exit()
        print(2)
    

app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())






# if __name__ == '__main__':
#     keyboard.add_hotkey('f1', test_a)
#     #按f1输出aaa
#     keyboard.add_hotkey('ctrl+alt', test, args=('b',))
#     #按ctrl+alt输出b
#     keyboard.wait()
#     #wait里也可以设置按键，说明当按到该键时结束