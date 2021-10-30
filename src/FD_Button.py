import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
   

class Test(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.buttonA = QtWidgets.QPushButton('Click!', self)
        self.buttonA.clicked.connect(self.showDialog)
        self.buttonA.move(100, 50)

        self.labelA = QtWidgets.QLabel(self)
        self.labelA.move(110, 100)

        self.setGeometry(100, 100, 300, 200)

    def showDialog(self):

        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        fname = QFileDialog.getExistingDirectory()

        print(fname)

            # テキストエディタにファイル内容書き込み

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit( app.exec_() )