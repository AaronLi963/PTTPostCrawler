from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
# UI
import QT.main_ui as ui
from PyPtt import PTT
import util
import json


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
        self.setUserInfo()
        self.labelBuffer = []

    def setUserInfo(self):
        try:
            with open("user.json") as f:
                userInfo = json.load(f)
                self.inputPTTID.setText(userInfo.get("id",""))
                self.inputPTTPassword.setText(userInfo.get("password",""))
                self.inputPTTAID.setText(userInfo.get("aid",""))
        except:
            pass

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
            self.bottonLoadPosts.clicked.connect(self.getPosts)
     
    def getPosts(self):
        aid, board = util.ParseAID(self.inputPTTAID.text())
        post_info = ptt_bot.get_post(board, post_aid=aid)
        self.textArticleTitle.setText(post_info.title)
        self.scrollPost.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.postWidget = QWidget()
        self.scrollLayout = QVBoxLayout()
        if len(post_info.push_list) > 15:
            post_info.push_list = post_info.push_list[-15:]
        for push_info in post_info.push_list:
            pushType = '推'
            if push_info == PTT.data_type.push_type.BOO:
                pushType = '噓'
            elif push_info == PTT.data_type.push_type.ARROW:
                pushType = '->'
            author = push_info.author
            content = push_info.content
            buffer = pushType + ' ' + author + '\n  ' + content
            label = QLabel(buffer)
            label.adjustSize()
            self.scrollLayout.addWidget(label)
        self.postWidget.setLayout(self.scrollLayout)
        self.scrollPost.setWidget(self.postWidget)
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())