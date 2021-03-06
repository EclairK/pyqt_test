# - * - coding: utf8 - *

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random # 今回は乱数を使用するのでimportします。

import datetime


############################
##
## ウィンドウ用のクラスです。
##
############################
class plotGraph(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = '適当にグラフを打つよウィンドウ'
        self.width = 700
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.setWindowLayout()
        self.statusBar()

    def setWindowLayout(self):

        ### メニューバーアクションの定義 ###
        exitAction = QAction('&終了', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('ウィンドウを閉じるよ')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('ファイル')
        fileMenu.addAction(exitAction)

        self.w = QWidget()

        ### 実際にグラフを打つPlotCanvasクラスのインスタンスを生成します。 ###
        self.m = PlotCanvas(self, width=5, height=4)

        ### ボタンを作成します。 ###
        self.plt_button = QPushButton('グラフを打つよ', self)
        self.plt_button.clicked.connect(self.m.plot)
        self.del_button = QPushButton('グラフを消すよ', self)
        self.del_button.clicked.connect(self.m.clear)

        ### GridLayoutを使用します。 ###
        main_layout = QGridLayout()

        ### GridLayoutのどこに何を配置するのか指定します。 ###
        main_layout.addWidget(self.m, 0, 0, 5, 4)
        main_layout.addWidget(self.plt_button, 0, 11, 1, 1)
        main_layout.addWidget(self.del_button, 0, 11, 2, 1)

        timer = QTimer(self)
        timer.timeout.connect(self.getDateTime)
        timer.start(1000)

        self.w.setLayout(main_layout)
        self.setCentralWidget(self.w)
        self.show()

    def getDateTime(self):
        dt = datetime.datetime.today()
        dt_str = dt.strftime('%Y年%m月%d日 %H時%M分%S秒')
        self.statusBar().showMessage('日時' + ' ' + dt_str)


##################################
##
## 実際にグラフを描画するクラスです。
##
##################################
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        super(PlotCanvas, self).__init__(self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(
                self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding
                )
        FigureCanvas.updateGeometry(self)
        self.plot()

    def plot(self):
        self.axes.cla()
        self.data = [random.random() for i in range(25)]
        self.axes.plot(self.data, 'r-')
        self.axes.set_title('PyQt5 & Matplotlib Graph')
        self.draw()

    def clear(self):
        self.axes.cla()
        self.draw()


def main():
    app = QApplication(sys.argv)
    gui = plotGraph()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()