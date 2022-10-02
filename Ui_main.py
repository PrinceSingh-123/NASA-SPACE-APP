# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 437)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 0, 331, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 40, 801, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 80, 41, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 61, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 230, 61, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 300, 71, 31))
        self.bf1 = QLineEdit(self.centralwidget)
        self.bf1.setObjectName(u"bf1")
        self.bf1.setGeometry(QRect(160, 80, 151, 31))
        self.ampl1_i = QLineEdit(self.centralwidget)
        self.ampl1_i.setObjectName(u"ampl1_i")
        self.ampl1_i.setGeometry(QRect(160, 150, 151, 31))
        self.bgse = QLineEdit(self.centralwidget)
        self.bgse.setObjectName(u"bgse")
        self.bgse.setGeometry(QRect(160, 220, 151, 31))
        self.time_pb5 = QLineEdit(self.centralwidget)
        self.time_pb5.setObjectName(u"time_pb5")
        self.time_pb5.setGeometry(QRect(160, 290, 151, 31))
        self.predict = QPushButton(self.centralwidget)
        self.predict.setObjectName(u"predict")
        self.predict.setGeometry(QRect(530, 360, 131, 41))
        self.predict.setStyleSheet(u"border-radius:12px;\n"
"background-color: rgb(112, 122, 126);")
        self.clear = QPushButton(self.centralwidget)
        self.clear.setObjectName(u"clear")
        self.clear.setGeometry(QRect(350, 360, 131, 41))
        self.clear.setStyleSheet(u"border-radius:14px;\n"
"background-color: rgb(183, 65, 204);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 70, 131, 41))
        self.result = QLabel(self.centralwidget)
        self.result.setObjectName(u"result")
        self.result.setGeometry(QRect(600, 70, 131, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Save the Earth from Another Carrington Event!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BF1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"AMPL1_I", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"BGSE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Time_PB5", None))
        self.bf1.setText("")
        self.ampl1_i.setText("")
        self.bgse.setText("")
        self.time_pb5.setText("")
        self.predict.setText(QCoreApplication.translate("MainWindow", u"predict", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Predication Result", None))
        self.result.setText("")
    # retranslateUi

