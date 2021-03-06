# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './QT/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1138, 897)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(-1, 200, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.labelPTTID = QtWidgets.QLabel(self.centralwidget)
        self.labelPTTID.setObjectName("labelPTTID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelPTTID)
        self.inputPTTID = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPTTID.sizePolicy().hasHeightForWidth())
        self.inputPTTID.setSizePolicy(sizePolicy)
        self.inputPTTID.setMaximumSize(QtCore.QSize(200, 100))
        self.inputPTTID.setText("")
        self.inputPTTID.setObjectName("inputPTTID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputPTTID)
        self.labelPTTPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPTTPassword.setObjectName("labelPTTPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPTTPassword)
        self.inputPTTPassword = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPTTPassword.sizePolicy().hasHeightForWidth())
        self.inputPTTPassword.setSizePolicy(sizePolicy)
        self.inputPTTPassword.setMaximumSize(QtCore.QSize(200, 100))
        self.inputPTTPassword.setText("")
        self.inputPTTPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputPTTPassword.setObjectName("inputPTTPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputPTTPassword)
        self.labelAID = QtWidgets.QLabel(self.centralwidget)
        self.labelAID.setObjectName("labelAID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelAID)
        self.inputPTTAID = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputPTTAID.sizePolicy().hasHeightForWidth())
        self.inputPTTAID.setSizePolicy(sizePolicy)
        self.inputPTTAID.setMaximumSize(QtCore.QSize(200, 100))
        self.inputPTTAID.setText("")
        self.inputPTTAID.setObjectName("inputPTTAID")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputPTTAID)
        self.bottonLoadPosts = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottonLoadPosts.sizePolicy().hasHeightForWidth())
        self.bottonLoadPosts.setSizePolicy(sizePolicy)
        self.bottonLoadPosts.setMaximumSize(QtCore.QSize(200, 100))
        self.bottonLoadPosts.setObjectName("bottonLoadPosts")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bottonLoadPosts)
        self.horizontalLayout.addLayout(self.formLayout)
        self.lineSep = QtWidgets.QFrame(self.centralwidget)
        self.lineSep.setFrameShape(QtWidgets.QFrame.VLine)
        self.lineSep.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSep.setObjectName("lineSep")
        self.horizontalLayout.addWidget(self.lineSep)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textArticleTitle = QtWidgets.QTextBrowser(self.centralwidget)
        self.textArticleTitle.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textArticleTitle.setFont(font)
        self.textArticleTitle.setObjectName("textArticleTitle")
        self.verticalLayout_3.addWidget(self.textArticleTitle)
        self.scrollPost = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollPost.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scrollPost.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollPost.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollPost.setWidgetResizable(True)
        self.scrollPost.setObjectName("scrollPost")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 532, 794))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollPost.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollPost)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelPTTID.setText(_translate("MainWindow", "輸入PTT ID :"))
        self.inputPTTID.setPlaceholderText(_translate("MainWindow", "PTT ID"))
        self.labelPTTPassword.setText(_translate("MainWindow", "輸入PTT 密碼 :"))
        self.inputPTTPassword.setPlaceholderText(_translate("MainWindow", "PTT 密碼"))
        self.labelAID.setText(_translate("MainWindow", "輸入文章代碼 :"))
        self.inputPTTAID.setPlaceholderText(_translate("MainWindow", "#1VyG2jpG (C_Chat)"))
        self.bottonLoadPosts.setText(_translate("MainWindow", "載入推文"))
        self.textArticleTitle.setPlaceholderText(_translate("MainWindow", "文章標題"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
