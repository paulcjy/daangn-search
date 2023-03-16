import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTableView
# from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
# from PySide6.QtCore import Signal, Slot, Qt, QModelIndex, QCoreApplication
# from PySide6.QtUiTools import loadUiType

import multiprocessing as mp
from multiprocessing import Pool
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
# import time
# from timeit import default_timer as timer
import webbrowser
# from ui import *

sys.setrecursionlimit(20000)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


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






def errorMsg(parent, message):
	msgBox = QMessageBox(parent)
	msgBox.setIcon(QMessageBox.Warning)
	msgBox.setWindowTitle('에러')
	msgBox.setText(message)
	msgBox.exec_()

def extract_num(string):
	if '원' not in string:
		return 0

	result = int(''.join([c for c in string if c.isdigit()]))
	return result

def make_urls_from_range(key_rng): #2 keyword, range
	keyword, rng = key_rng
	urls = []
	url1 = 'https://www.daangn.com/search/'
	url2 = '/more/flea_market?page='
	for i in rng:
		url = url1 + keyword + url2 + str(i+1)
		urls.append(url)
	return urls

def get_html_from_url(url: str): #3
	source = requests.get(url)
	return source.text

def thread_get_page(key_range): #1 keyword, range
	urls = make_urls_from_range(key_range)
	thread_list = []
	result = []
	with ThreadPoolExecutor(max_workers=8) as executor:
		for url in urls:
			thread_list.append(executor.submit(get_html_from_url, url))
		for execution in concurrent.futures.as_completed(thread_list):
			result.append(execution.result())
	return result

def get_soup(source): #4
	return BeautifulSoup(source, 'html.parser')

def apply_cond(item, price_cond): #6 price_cond
	if ('서울' not in item[1]) and ('하남시' not in item[1]):
		return 0
	if extract_num(item[2]) not in price_cond:
		return 0

	return 1

def get_data(soup_price): #5 soup, price_cond
	soup, price_cond = soup_price
	result = []

	titles   = list(map(lambda x: x.text, soup.select('.article-title')))
	regions  = list(map(lambda x: x.text.strip(), soup.select('.article-region-name')))
	prices   = list(map(lambda x: x.text.strip(), soup.select('.article-price')))
	contents = list(map(lambda x: x.text, soup.select('.article-content')))
	links    = list(map(lambda x: 'https://www.daangn.com' + x.attrs['href'], soup.select('.flea-market-article-link')))

	items = list(zip(titles, regions, prices, contents, links))

	for item in items:
		if apply_cond(item, price_cond):
			result.append(item)
	
	return result



class TableModel(QStandardItemModel):
	def __init__(self, parent, articles):
		QStandardItemModel.__init__(self, 0, 5)
		self.p = parent

		self.setHeaderData(0, Qt.Horizontal, '제목')
		self.setHeaderData(1, Qt.Horizontal, '지역')
		self.setHeaderData(2, Qt.Horizontal, '가격')
		self.setHeaderData(3, Qt.Horizontal, '내용')
		self.setHeaderData(4, Qt.Horizontal, '링크')

		for item in articles:
			self.appendRow(None)
			row = self.rowCount()-1

			self.setData(self.index(row, 0), item[0])
			self.setData(self.index(row, 1), item[1])
			self.setData(self.index(row, 2), item[2])
			self.setData(self.index(row, 3), item[3])
			self.setData(self.index(row, 4), item[4])

			self.item(row, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.searchBtn.clicked.connect(self.search)
		self.setWindowIcon(QIcon('carrot.png'))
		self.setWindowTitle('당근마켓 검색기')
		self.showMaximized()
		# self.time = 0

	# def search2(self):
	# 	count = 20
	# 	total_time = 0
	# 	for _ in range(count):
	# 		t = timer()
	# 		self.search()
	# 		total_time += timer()-t
	# 	# print('평균 검색 시간: ', self.time / count)
	# 	print('평균 총검색시간: ', total_time / count)

	def search(self):

		# 빈 칸
		if self.keywordEnt.text() == '':
			errorMsg(self, '검색어를 입력하세요.')
			return
		if self.minEnt.text() == '' or self.maxEnt.text() == '':
			errorMsg(self, '가격 범위를 입력하세요.')
			return
		if self.targetPageEnt.text() == '':
			errorMsg(self, '페이지 수를 입력하세요.')
			return

		# 숫자
		if not (self.minEnt.text().isdigit() and self.maxEnt.text().isdigit()):
			errorMsg(self, '가격 범위에는 숫자만 올 수 있습니다.')
			return
		if not self.targetPageEnt.text().isdigit():
			errorMsg(self, '페이지 수에는 숫자만 올 수 있습니다.')
			return

		self.targetPage = self.targetPageEnt.text()
		self.targetPage = int(self.targetPage)

		if not (0 < self.targetPage < 801):
			errorMsg(self, '페이지 수가 범위를 초과했습니다.')
			return


		self.keywordEnt.setDisabled(True)
		self.minEnt.setDisabled(True)
		self.maxEnt.setDisabled(True)
		self.targetPageEnt.setDisabled(True)
		self.searchBtn.setDisabled(True)

		QCoreApplication.processEvents()

		keyword = self.keywordEnt.text()
		min_price = int(self.minEnt.text())
		max_price = int(self.maxEnt.text())
		price_cond = range(min_price, max_price + 1) # Price Condition

		p1 = int(self.targetPage / 4)
		p2 = int(self.targetPage / 2)
		p3 = int(self.targetPage * 3 / 4)

		r1 = range(0, p1)
		r2 = range(p1, p2)
		r3 = range(p2, p3)
		r4 = range(p3, self.targetPage)

		pages = ((keyword, r1), (keyword, r2), (keyword, r3), (keyword, r4)) # Page Ranges


		# 당근마켓 검색
		# t1=timer()
		with Pool(processes=mp.cpu_count()) as pool:
			source = pool.map(thread_get_page, pages)
			source = [*source[0], *source[1], *source[2], *source[3]]

			# t2=timer()
			soups = pool.map(get_soup, source)
			soups = list(map(lambda soup: (soup, price_cond), soups))

			# t3=timer()
			results = pool.map(get_data, soups)
			data = []
			for result in results:
				data += result
			# t4=timer()

		# print('페이지 다운: ', t2-t1)
		# print('숩 생성하기: ', t3-t2)
		# print('조건별 입력: ', t4-t3)

		# 모델 설정
		self.model = TableModel(self, data)
		self.table.setModel(self.model)
		self.table.setSelectionBehavior(QTableView.SelectRows)

		for i in range(self.model.rowCount()):
			btn = QPushButton('바로가기')
			btn.clicked.connect(self.link)
			self.table.setIndexWidget(self.model.index(i, 4), btn)

		width = (500, 200, 120, 900, 100)
		for i in range(5):
			self.table.setColumnWidth(i, width[i])

		self.keywordEnt.setEnabled(True)
		self.minEnt.setEnabled(True)
		self.maxEnt.setEnabled(True)
		self.targetPageEnt.setEnabled(True)
		self.searchBtn.setEnabled(True)

		return



	def link(self):
		row = self.table.currentIndex().row()
		chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
		webbrowser.get(chrome_path).open(self.model.itemFromIndex(self.model.index(row, 4)).text())



if __name__ == "__main__":
	mp.freeze_support()
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())