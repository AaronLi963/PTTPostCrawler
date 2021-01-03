from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
# UI
import QT.main_ui as ui
from PyPtt import PTT


ptt_bot = PTT.API()

class MainWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PTT推文顯示器")
        # self.setFixedSize(960, 840)
        self.bottonLogin.clicked.connect(self.loginPTT)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar) 
        self.msgBox = QMessageBox()

    def loginPTT(self):
        pttID = self.inputPTTID.text()
        pttPW = self.inputPTTPassword.text()
        if pttID == "" or pttPW == "":
            self.statusBar.showMessage("請輸入帳號密碼", 5000)
            return

        try: 
            self.statusBar.showMessage("登入中")
            ptt_bot.login(pttID, pttPW)
        except PTT.exceptions.LoginError:
            self.msgBox.setText("登入失敗")
            self.msgBox.show()
        except PTT.exceptions.WrongIDorPassword:
            self.msgBox.setText("帳號或密碼錯誤")
            self.msgBox.show()
        except PTT.exceptions.LoginTooOften:
            self.msgBox.setText("請稍後再登入")
            self.msgBox.show()
        except Exception : 
            self.msgBox.setText("unknown error")
            self.msgBox.show()
        else :
            self.statusBar.showMessage("登入成功: " + pttID, 5000)
     




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())