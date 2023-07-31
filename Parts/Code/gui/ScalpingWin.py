# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScalpingGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScalpingWin(object):
    def openRSI(self):
        self.window = QtWidgets.QMainWindow()
        from RSIWin import Ui_RSIWin
        self.ui = Ui_RSIWin()
        self.ui.setupUi(self.window)
        self.window.show()

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
        from GRWin import Ui_GRWin
        self.ui = Ui_GRWin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openHome(self):
        self.window = QtWidgets.QMainWindow()
        from gui import Ui_mainWindow
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, ScalpingWin):
        ScalpingWin.setObjectName("ScalpingWin")
        ScalpingWin.resize(900, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("scalping.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ScalpingWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ScalpingWin)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 230, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 340, 81, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(320, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 170, 111, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 170, 111, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 340, 113, 22))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(460, 230, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 80, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(460, 170, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 230, 101, 16))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 170, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 170, 121, 21))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(750, 170, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 227, 93, 28))
        self.pushButton.setObjectName("pushButton")
        ScalpingWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ScalpingWin)
        self.menubar.setStyleSheet(
            "background-color: rgb(116, 235, 213);")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuScalping = QtWidgets.QMenu(self.menubar)
        self.menuScalping.setStyleSheet(
            "background-color: rgb(172, 182, 229);")
        self.menuScalping.setObjectName("menuScalping")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setStyleSheet(
            "background-color: rgb(172, 182, 229);")
        self.menuHome.setObjectName("menuHome")
        ScalpingWin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ScalpingWin)
        self.statusbar.setObjectName("statusbar")
        ScalpingWin.setStatusBar(self.statusbar)
        self.actionTrend_Following = QtWidgets.QAction(ScalpingWin)
        self.actionTrend_Following.setObjectName("actionTrend_Following")
        self.actionTrend_Following.triggered.connect(self.openTrend)
        self.actionTrend_Following.triggered.connect(ScalpingWin.close)
        self.actionRSI_Indexing = QtWidgets.QAction(ScalpingWin)
        self.actionRSI_Indexing.setObjectName("actionRSI_Indexing")
        self.actionRSI_Indexing.triggered.connect(self.openRSI)
        self.actionRSI_Indexing.triggered.connect(ScalpingWin.close)
        self.actionGeneral_Recommendation = QtWidgets.QAction(ScalpingWin)
        self.actionGeneral_Recommendation.setObjectName(
            "actionGeneral_Recommendation")
        self.actionGeneral_Recommendation.triggered.connect(self.openGeneral)
        self.actionGeneral_Recommendation.triggered.connect(ScalpingWin.close)
        self.actionHome = QtWidgets.QAction(ScalpingWin)
        self.actionHome.setObjectName("actionHome")
        self.actionHome.triggered.connect(self.openHome)
        self.actionHome.triggered.connect(ScalpingWin.close)
        self.actionScalping = QtWidgets.QAction(ScalpingWin)
        self.actionScalping.setObjectName("actionScalping")
        self.actionScalping.triggered.connect(self.openScalping)
        self.actionScalping.triggered.connect(ScalpingWin.close)
        self.actionGeneral_Recommendation_2 = QtWidgets.QAction(ScalpingWin)
        self.actionGeneral_Recommendation_2.setObjectName(
            "actionGeneral_Recommendation_2")
        self.actionGeneral_Recommendation_2.triggered.connect(self.openGeneral)
        self.actionGeneral_Recommendation_2.triggered.connect(
            ScalpingWin.close)
        self.menuScalping.addAction(self.actionTrend_Following)
        self.menuScalping.addAction(self.actionRSI_Indexing)
        self.menuScalping.addAction(self.actionScalping)
        self.menuHome.addAction(self.actionHome)
        self.menuHome.addAction(self.actionGeneral_Recommendation_2)
        self.menubar.addAction(self.menuScalping.menuAction())
        self.menubar.addAction(self.menuHome.menuAction())

        self.retranslateUi(ScalpingWin)
        QtCore.QMetaObject.connectSlotsByName(ScalpingWin)

    def retranslateUi(self, ScalpingWin):
        _translate = QtCore.QCoreApplication.translate
        ScalpingWin.setWindowTitle(_translate("ScalpingWin", "Scalping"))
        self.lineEdit_2.setPlaceholderText(_translate("ScalpingWin", "0"))
        self.label_3.setText(_translate("ScalpingWin", "Win Rate"))
        self.label_4.setText(_translate("ScalpingWin", "Scalping"))
        self.label_7.setText(_translate("ScalpingWin", "Start Date"))
        self.label.setText(_translate("ScalpingWin", "Stock Tag"))
        self.lineEdit_3.setPlaceholderText(_translate("ScalpingWin", "0"))
        self.label_2.setText(_translate("ScalpingWin", "Buy/Sell \n"
                                        "Percentage"))
        self.label_5.setText(_translate("ScalpingWin", "Scalping is the idea of buy when the market dips below a certain percentage \n"
                                        "and selling once the price has gone above a certain percentage"))
        self.label_8.setText(_translate("ScalpingWin", "End Date"))
        self.label_6.setText(_translate("ScalpingWin", "Days Timeout"))
        self.lineEdit_4.setPlaceholderText(_translate("ScalpingWin", "5"))
        self.pushButton.setText(_translate("ScalpingWin", "Submit"))
        self.pushButton.clicked.connect(self.ScalpingOutput)
        self.menuScalping.setTitle(_translate("ScalpingWin", "Strategies"))
        self.menuHome.setTitle(_translate("ScalpingWin", "Others"))
        self.actionTrend_Following.setText(
            _translate("ScalpingWin", "Trend Following"))
        self.actionRSI_Indexing.setText(
            _translate("ScalpingWin", "RSI Indexing"))
        self.actionGeneral_Recommendation.setText(
            _translate("ScalpingWin", "General Recommendation"))
        self.actionHome.setText(_translate("ScalpingWin", "Home"))
        self.actionScalping.setText(_translate("ScalpingWin", "Scalping"))
        self.actionGeneral_Recommendation_2.setText(
            _translate("ScalpingWin", "General Recommendation"))

    def ScalpingOutput(self):
        import sys
        import os
        current = os.path.dirname(os.path.realpath(__file__))
        parent = os.path.dirname(current)
        sys.path.append(parent)
        from Strategies.general import convertDate, getWinRate, profits
        from Strategies.Scalping import scalping, displayEntryExit, graphScalping
        stock = self.lineEdit.text()
        buyPSellP = self.lineEdit_2.text()
        startDate = self.dateEdit_2.text()
        endDate = self.dateEdit.text()
        timeout = self.lineEdit_4.text()
        startD, endD = convertDate(startDate, endDate)
        data, signals = scalping(stock, startD, endD, timeout, buyPSellP)
        buy, sell = displayEntryExit(data)
        profitsScalping = profits(buy, sell, data)
        winRate = getWinRate(profitsScalping)
        self.lineEdit_3.setText(str(winRate) + "%")
        graphScalping(data, buy, sell)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScalpingWin = QtWidgets.QMainWindow()
    ui = Ui_ScalpingWin()
    ui.setupUi(ScalpingWin)
    ScalpingWin.show()
    sys.exit(app.exec_())
