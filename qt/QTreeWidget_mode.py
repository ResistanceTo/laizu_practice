# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#     #window系统提供的模式
#     model = QDirModel()
#     #创建一个QTreeView的控件
#     tree = QTreeView()
#     #为控件添加模式
#     tree.setModel(model)

#     tree.setWindowTitle('QTreeView例子')
#     tree.resize(640, 480)

#     tree.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
import qtawesome


class TreeWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(TreeWidgetDemo, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')

        self.tree = QTreeWidget()
        #设置列数
        self.tree.setColumnCount(2)
        #设置树形控件头部的标题
        self.tree.setHeaderLabels(['Key', 'Value'])

        #设置根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'Root')
        root.setIcon(0, QIcon(qtawesome.icon('ei.align-justify')))

        # todo 优化2 设置根节点的背景颜色
        brush_red = QBrush(Qt.red)
        root.setBackground(0, brush_red)
        brush_blue = QBrush(Qt.blue)
        root.setBackground(1, brush_blue)

        #设置树形控件的列的宽度
        self.tree.setColumnWidth(0, 150)

        #设置子节点1
        child1 = QTreeWidgetItem()
        child1.setText(0, 'child1')
        child1.setText(1, 'ios')
        child1.setIcon(0, QIcon(qtawesome.icon('mdi.apple-ios')))

        #todo 优化1 设置节点的状态
        child1.setCheckState(0, Qt.Checked)

        root.addChild(child1)

        #设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '')
        child2.setIcon(0, QIcon(qtawesome.icon('mdi.cellphone-android')))

        #设置子节点3
        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')
        child3.setIcon(0, QIcon(qtawesome.icon('fa.android')))

        #加载根节点的所有属性与子控件
        self.tree.addTopLevelItem(root)

        #TODO 优化3 给节点添加响应事件
        self.tree.clicked.connect(self.onClicked)

        #节点全部展开
        self.tree.expandAll()
        self.setCentralWidget(self.tree)

    def onClicked(self, qmodeLindex):
        item = self.tree.currentItem()
        print('Key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeWidgetDemo()
    tree.show()
    sys.exit(app.exec_())
