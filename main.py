from PyQt5 import QtWidgets
from PyQt5 import QtCore
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
import logging


class MainWindow(QMainWindow, ui.Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resized.connect(self.resizeScrollArea)
        self.setWindowTitle("PTT推文顯示器")
        # self.setFixedSize(960, 840)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar) 
        self.msgBox = QMessageBox()
        self.setUserInfo()
        self.labelBuffer = []
        self.dataThread = DataThread()
        self.bottonLoadPosts.clicked.connect(self.getPosts)
        # set scroll area
        self.scrollPost.setWidgetResizable(True)
        self.postWidget = QWidget()
        self.scrollLayout = QVBoxLayout()
        self.postWidget.setLayout(self.scrollLayout)
        self.scrollPost.setWidget(self.postWidget)
        self.scrollPost.verticalScrollBar().setStyleSheet('background: white')

    def resizeEvent(self, event):
        self.resized.emit()
        return super().resizeEvent(event)

    def setUserInfo(self):
        try:
            with open("user.json") as f:
                userInfo = json.load(f)
                self.inputPTTID.setText(userInfo.get("id",""))
                self.inputPTTPassword.setText(userInfo.get("password",""))
                self.inputPTTAID.setText(userInfo.get("aid",""))
        except:
            pass
    
    def setStatus(self, status):
        self.statusBar.showMessage(status,5000)

    def setTitle(self, title):
        self.textArticleTitle.setText(title)
    
    def addPostInfo(self, info):
        label = QLabel(info)
        label.adjustSize()
        label.setStyleSheet('color: white;font: 12pt')
        self.scrollLayout.addWidget(label)

    def addPost(self, content):
        label = QLabel("  " + content)
        label.adjustSize()
        label.setStyleSheet('color: yellow;font: 12pt')
        self.scrollLayout.addWidget(label)
        scroll_bar = self.scrollPost.verticalScrollBar()
        scroll_bar.rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))

    def getPosts(self): # trigger DataThread to get data
        self.bottonLoadPosts.clicked.disconnect()
        aid, board = util.ParseAID(self.inputPTTAID.text())
        self.dataThread.statusSignal.connect(self.setStatus)
        self.dataThread.titleSignal.connect(self.setTitle)
        self.dataThread.postSignal.connect(self.addPost)
        self.dataThread.infoSignal.connect(self.addPostInfo)
        id = self.inputPTTID.text()
        password = self.inputPTTPassword.text()
        self.dataThread.setting(id, password, board, aid)
        self.dataThread.start()
    def resizeScrollArea(self):
        # self.statusBar.showMessage("got resize event",1000)
        mainSize = self.size()
        # line
        self.lineSep.resize(10,mainSize.height())

        # layout
        # self.statusBar.showMessage(str(mainSize),1000)
        # newWeight = mainSize.width() - 320
        # newHeight = mainSize.height() - 70
        # self.scrollPost.resize(newWeight,newHeight)


class DataThread(QThread): # ref https://www.cnblogs.com/linyfeng/p/12239856.html
    statusSignal = pyqtSignal(str)
    titleSignal = pyqtSignal(str)
    postSignal = pyqtSignal(str)
    infoSignal = pyqtSignal(str)
    ptt_bot = PTT.API()

    def __init__(self):
        super().__init__()
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
        except Exception as e: 
            status = "unknown error"
            error_class = e.__class__.__name__
            logging.warning(str(e))
        else :
            status = "登入成功: " + self.id
            util.SaveUserJson(self.id, self.password, self.board, self.aid)
        
        self.statusSignal.emit(status)
        if status.startswith("登入成功"):
            return True
        return False
    
    def run(self):
        self.ptt_bot = PTT.API(log_level=PTT.log.level.INFO)
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
            if totalPosts - self.index > 30:
                self.index = totalPosts - 30
            newPosts = post_info.push_list[self.index:]
            for push_info in newPosts:
                floor = self.index + 1
                pushType = '推'
                if push_info == PTT.data_type.push_type.BOO:
                    pushType = '噓'
                elif push_info == PTT.data_type.push_type.ARROW:
                    pushType = '->'
                author = push_info.author
                content = push_info.content
                pushTime = push_info.time
                info = str(floor) + 'F:  ' + pushType + '     ' + author
                # buffer = str(floor) + 'F:  ' + pushType + ' ' + author + '\n  ' + content
                #buffer = util.SetPushFormat(floor,pushType, author, pushTime, content)
                self.index = floor
                self.infoSignal.emit(info)
                self.postSignal.emit(content)
            time.sleep(1) # load new posts every 1 second



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())