# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_V2uhxhrW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import guigui_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(872, 626)
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 550, 500))
        self.widget.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(150, 123, 111, 255)\n"
"}\n"
"\n"
"QPushButton#pushButton_2{\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"	color: rgba(131,96,53,255);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	color:rgba(91, 88, 53, 255)\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(:/image/Robot Arm for Assembling scene, Gregor Kopka.jpg);\n"
"border-top-left-radius:50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 280, 430))
        self.label_2.setStyleSheet(u"background-color:rgba(0,0,0,80);\n"
"border-image: url(:/image/11fa5c88d63d2a4f703b4ac5b19080e8.jpg);\n"
"border-top-left-radius:50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 40, 141, 40))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:rgba(0,0,0,200);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 80, 121, 31))
        font2 = QFont()
        font2.setFamily(u"MS Reference Sans Serif")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 400, 81, 16))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 420, 41, 31))
        self.label_7.setStyleSheet(u"image: url(:/image/Logo_PENS.png);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 420, 41, 31))
        self.label_8.setStyleSheet(u"image: url(:/image/hima_meka-removebg-preview (1).png);")
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(280, 230, 211, 41))
        font3 = QFont()
        font3.setFamily(u"Gill Sans MT")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), 		stop:1 rgba(255, 255, 255, 255))\n"
"	border-radius:10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/image/1945759.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(30, 30))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(280, 110, 211, 41))
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4{\n"
"	qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255),     stop:1 rgba(255, 255, 255, 255)) \n"
"border-radius:50px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/2457863.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 170, 211, 41))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), 		stop:1 rgba(255, 255, 255, 255))\n"
"	border-radius:10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/image/5501999.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(30, 30))
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(280, 290, 211, 41))
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_6.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), 		stop:1 rgba(255, 255, 255, 255))\n"
"	border-radius:10px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/image/4603985.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_7 = QPushButton(self.widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(280, 350, 211, 41))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_7.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), 		stop:1 rgba(255, 255, 255, 255))\n"
"	border-radius:10px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/image/8536953.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setIconSize(QSize(30, 30))
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 872, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_7.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"GUI RTDS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Example Motion :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Property of :", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Letter X", None))
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Letter M", None))
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Tample", None))
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Plus Shape", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Rectangel", None))
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut("")
#endif // QT_CONFIG(shortcut)
    # retranslateUi

