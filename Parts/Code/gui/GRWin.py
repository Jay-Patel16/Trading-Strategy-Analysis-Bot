# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GRGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_GRWin(object):
    def openRSI(self):
        self.window = QtWidgets.QMainWindow()
        from RSIWin import Ui_RSIWin
        self.ui = Ui_RSIWin()
        self.ui.setupUi(self.window)
        self.window.show()
        GRWin.close()

    def openTrend(self):
        self.window = QtWidgets.QMainWindow()
        from TrendWin import Ui_TrendWin
        self.ui = Ui_TrendWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openScalping(self):
        self.window = QtWidgets.QMainWindow()
        from ScalpingWin import Ui_ScalpingWin
        self.ui = Ui_ScalpingWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openGeneral(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GRWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHome(self):
        self.window = QtWidgets.QMainWindow()
        from gui import Ui_mainWindow
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, GRWin):
        GRWin.setObjectName("GRWin")
        GRWin.resize(930, 530)
        self.centralwidget = QtWidgets.QWidget(GRWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 180, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 400, 151, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 60, 671, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 400, 113, 22))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(670, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 300, 91, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 240, 101, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(580, 240, 171, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 120, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, 440, 41, 20))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setText('Link')
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(290, 240, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(290, 300, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(382, 440, 231, 22))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        GRWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GRWin)
        self.menubar.setStyleSheet("background-color: rgb(116, 235, 213);")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuStrategies = QtWidgets.QMenu(self.menubar)
        self.menuStrategies.setStyleSheet(
            "background-color: rgb(172, 182, 229);")
        self.menuStrategies.setObjectName("menuStrategies")
        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setStyleSheet(
            "background-color: rgb(172, 182, 229);")
        self.menuOthers.setObjectName("menuOthers")
        GRWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GRWin)
        self.statusbar.setObjectName("statusbar")
        GRWin.setStatusBar(self.statusbar)
        self.actionTrend_Following = QtWidgets.QAction(GRWin)
        self.actionTrend_Following.setObjectName("actionTrend_Following")
        self.actionScalping = QtWidgets.QAction(GRWin)
        self.actionScalping.setObjectName("actionScalping")
        self.actionRSI_Indexing = QtWidgets.QAction(GRWin)
        self.actionRSI_Indexing.setObjectName("actionRSI_Indexing")
        self.actionHome = QtWidgets.QAction(GRWin)
        self.actionHome.setObjectName("actionHome")
        self.actionGeneral_Recommendation = QtWidgets.QAction(GRWin)
        self.actionGeneral_Recommendation.setObjectName(
            "actionGeneral_Recommendation")
        self.actionTrend_Following_2 = QtWidgets.QAction(GRWin)
        self.actionTrend_Following_2.setObjectName("actionTrend_Following_2")
        self.actionTrend_Following_2.triggered.connect(self.openTrend)
        self.actionTrend_Following_2.triggered.connect(GRWin.close)
        self.actionScalping_2 = QtWidgets.QAction(GRWin)
        self.actionScalping_2.setObjectName("actionScalping_2")
        self.actionScalping_2.triggered.connect(self.openScalping)
        self.actionScalping_2.triggered.connect(GRWin.close)
        self.actionRSI_Indexing_2 = QtWidgets.QAction(GRWin)
        self.actionRSI_Indexing_2.setObjectName("actionRSI_Indexing_2")
        self.actionRSI_Indexing_2.triggered.connect(self.openRSI)
        self.actionRSI_Indexing_2.triggered.connect(GRWin.close)
        self.actionHome_2 = QtWidgets.QAction(GRWin)
        self.actionHome_2.setObjectName("actionHome_2")
        self.actionHome_2.triggered.connect(self.openHome)
        self.actionHome_2.triggered.connect(GRWin.close)
        self.actionGeneral_Recommendation_2 = QtWidgets.QAction(GRWin)
        self.actionGeneral_Recommendation_2.setObjectName(
            "actionGeneral_Recommendation_2")
        self.actionGeneral_Recommendation_2.triggered.connect(self.openGeneral)
        self.actionGeneral_Recommendation_2.triggered.connect(GRWin.close)
        self.menuStrategies.addAction(self.actionTrend_Following_2)
        self.menuStrategies.addAction(self.actionScalping_2)
        self.menuStrategies.addAction(self.actionRSI_Indexing_2)
        self.menuOthers.addAction(self.actionHome_2)
        self.menuOthers.addAction(self.actionGeneral_Recommendation_2)
        self.menubar.addAction(self.menuStrategies.menuAction())
        self.menubar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(GRWin)
        QtCore.QMetaObject.connectSlotsByName(GRWin)

    def retranslateUi(self, GRWin):
        _translate = QtCore.QCoreApplication.translate
        GRWin.setWindowTitle(_translate("GRWin", "General Recommendation"))
        self.label_4.setText(_translate("GRWin", "General Recommendation"))
        self.label_3.setText(_translate("GRWin", "Recommendation"))
        self.label_5.setText(_translate("GRWin", "This will provide a general recommendation of a stock; Buy, Sell, or Hold. \n"
                                        " In addition, allow you to export Historical Data to excel."))
        self.pushButton.setText(_translate("GRWin", "Submit"))
        self.pushButton.clicked.connect(self.GROutput)
        self.label.setText(_translate("GRWin", "Stock Tag"))
        self.label_2.setText(_translate("GRWin", "Exchange"))
        self.comboBox.setItemText(0, _translate("GRWin", "AMEX"))
        self.comboBox.setItemText(1, _translate("GRWin", "NASDAQ"))
        self.comboBox.setItemText(2, _translate("GRWin", "NYSE"))
        self.comboBox.setItemText(3, _translate("GRWin", "OTC"))
        self.label_7.setText(_translate("GRWin", "End Date"))
        self.label_6.setText(_translate("GRWin", "Start Date"))
        self.checkBox.setText(_translate("GRWin", "Export to Excel"))
        self.label_8.setText(_translate(
            "GRWin", "Leave Start and End Date Blank, if not exporting to Excel"))
        self.label_9.setText(_translate('GRWin', 'Link'))
        self.menuStrategies.setTitle(_translate("GRWin", "Strategies"))
        self.menuOthers.setTitle(_translate("GRWin", "Others"))
        self.actionTrend_Following.setText(
            _translate("GRWin", "Trend Following"))
        self.actionScalping.setText(_translate("GRWin", "Scalping"))
        self.actionRSI_Indexing.setText(_translate("GRWin", "RSI Indexing"))
        self.actionHome.setText(_translate("GRWin", "Home"))
        self.actionGeneral_Recommendation.setText(
            _translate("GRWin", "General Recommendation"))
        self.actionTrend_Following_2.setText(
            _translate("GRWin", "Trend Following"))
        self.actionScalping_2.setText(_translate("GRWin", "Scalping"))
        self.actionRSI_Indexing_2.setText(_translate("GRWin", "RSI Indexing"))
        self.actionHome_2.setText(_translate("GRWin", "Home"))
        self.actionGeneral_Recommendation_2.setText(
            _translate("GRWin", "General Recommendation"))

    def GROutput(self):
        import sys
        import os
        current = os.path.dirname(os.path.realpath(__file__))
        parent = os.path.dirname(current)
        sys.path.append(parent)
        from Strategies.general import TradingViewRec, convertDate, getStockData, exportToExcelData
        stock = self.lineEdit.text()
        exchange = self.comboBox.currentText()
        startDate = self.dateEdit.text()
        endDate = self.dateEdit_2.text()
        exportExcel = self.checkBox.isChecked()

        if stock != "":
            recommendation = TradingViewRec(stock, exchange)
            self.lineEdit_3.setText(recommendation)

        stock = stock
        if exportExcel:
            startD, endD = convertDate(startDate, endDate)
            stockData = getStockData(stock, startD, endD)
            exportToExcelData(stockData, stock)
            fileExplorer = QFileDialog.getOpenFileNames()
            link = ''.join(fileExplorer[0])
            self.lineEdit_4.setText(os.path.abspath(link))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GRWin = QtWidgets.QMainWindow()
    ui = Ui_GRWin()
    ui.setupUi(GRWin)
    GRWin.show()
    sys.exit(app.exec_())
