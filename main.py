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
import time


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
     
    def getPosts(self): # trigger DataThread to get data
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

class DataThread(QThread): # ref https://www.cnblogs.com/linyfeng/p/12239856.html
    statusSignal = pyqtSignal(str)
    titleSignal = pyqtSignal(str)
    postSignal = pyqtSignal(str)

    def __init__(self,board,aid,index):
        super().__init__()
        self.ptt_bot = PTT.API()
        self.index = 0
    
    def setting(self, id, password, board, aid):
        self.id = id
        self.password = password
        self.board = board
        self.aid = aid
    
    def login(self):
        status = "登入中"
        try:
            self.ptt_bot.login(self.id, self.password)
        except PTT.exceptions.LoginError:
            status = "登入失敗"
        except PTT.exceptions.WrongIDorPassword:
            status = "帳號或密碼錯誤"
        except PTT.exceptions.LoginTooOften:
            status = "請稍後再登入"
        except Exception : 
            status = "unknown error"
        else :
            status = "登入成功: " + self.id
            util.SaveUserJson(self.id, self.password, self.board, self.aid)
        
        self.statusSignal.emit(status)
        if status.startswith("登入成功"):
            return True
        return False
    
    def run(self):
        loginSuccess = self.login()
        if not loginSuccess:
            return

        # start to get posts
        while True :
            post_info = self.ptt_bot.get_post(self.board, post_aid=self.aid)
            self.titleSignal.emit(post_info.title)
            totalPosts = len(post_info.push_list)
            if totalPosts <= self.index:
                continue
            newPosts = post_info.push_list[self.index:]
            for push_info in post_info.push_list:
                floor = self.index + 1
                pushType = '推'
                if push_info == PTT.data_type.push_type.BOO:
                    pushType = '噓'
                elif push_info == PTT.data_type.push_type.ARROW:
                    pushType = '->'
                author = push_info.author
                content = push_info.content
                buffer = floor + 'F:  ' + pushType + ' ' + author + '\n  ' + content
                self.postSignal.emit(buffer)
                self.index = floor
            time.sleep(3) # load new posts every 3 seconds



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())