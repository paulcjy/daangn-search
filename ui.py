# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1020)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 41, 20))
        self.keywordEnt = QLineEdit(self.centralwidget)
        self.keywordEnt.setObjectName(u"keywordEnt")
        self.keywordEnt.setGeometry(QRect(60, 20, 121, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 20, 56, 20))
        self.minEnt = QLineEdit(self.centralwidget)
        self.minEnt.setObjectName(u"minEnt")
        self.minEnt.setGeometry(QRect(260, 20, 71, 20))
        self.maxEnt = QLineEdit(self.centralwidget)
        self.maxEnt.setObjectName(u"maxEnt")
        self.maxEnt.setGeometry(QRect(347, 20, 71, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(334, 20, 16, 20))
        self.searchBtn = QPushButton(self.centralwidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(750, 19, 75, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 20, 56, 20))
        self.targetPageEnt = QLineEdit(self.centralwidget)
        self.targetPageEnt.setObjectName(u"targetPageEnt")
        self.targetPageEnt.setGeometry(QRect(500, 20, 51, 20))
        self.table = QTableView(self.centralwidget)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(20, 50, 1881, 951))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(553, 20, 191, 20))
        font = QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(830, 20, 411, 20))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1750, 30, 151, 20))
        font1 = QFont()
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9\uc5b4", None))
        self.keywordEnt.setText(QCoreApplication.translate("MainWindow", u"\ub0c9\uc7a5\uace0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9 \ubc94\uc704", None))
        self.minEnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.maxEnt.setText(QCoreApplication.translate("MainWindow", u"100000000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.searchBtn.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ud398\uc774\uc9c0 \uc218", None))
        self.targetPageEnt.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"(\ud398\uc774\uc9c0 \ub2f9 12\uac1c, \uac00\ub2a5 \ubc94\uc704: 1~800)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"* \uac80\uc0c9\ud558\ub294 \ub370 \uc2dc\uac04\uc774 \uac78\ub9b4 \uc218 \uc788\uc2b5\ub2c8\ub2e4. \uacb0\uacfc\uac00 \ub098\uc62c \ub54c\uae4c\uc9c0 \uac00\ub9cc\ud788 \uae30\ub2e4\ub824\uc8fc\uc138\uc694.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ver.1.0  Made By CJY", None))
    # retranslateUi

