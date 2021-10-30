
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QAction,qApp
from PyQt5.QtCore import QTimer
import datetime # 時計を表示するために必要なので必ずimportしましょう。


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'メニューバーがあるウィンドウだよウィンドウ'
        self.width = 500
        self.height = 400
        self.initUI()

    def initUI(self):

        ### メニューバーアクションの定義 ###
        exitAction = QAction('&終了ーーー', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('GUI画面を閉じるよ')
        exitAction.triggered.connect(qApp.quit)

        fireAction = QAction('&ファイア', self)
        fireAction.setShortcut('Ctrl+F')
        fireAction.setStatusTip('アストラルファイアIを付与する')
        

        menubar = self.menuBar()
        fileMenu_main = menubar.addMenu('&ファイル')
        fileMenu_main.addAction(exitAction) # fileMenuにアクションを追加します。
        fileMenu_main.addAction(fireAction) # fileMenuにアクションを追加します。
        fileMenu_edit = menubar.addMenu('&編集')
        fileMenu_edit.addAction(exitAction) # fileMenuにアクションを追加します。

        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)

        self.statusBar()

      
        self.show()






        

def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()