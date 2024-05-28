import sys, os, subprocess, configparser, time, webbrowser
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget, QTextEdit)
import anchecker_rc

class Ui_SiteCheck(object):
    def setupUi(self, SiteCheck):
        if not SiteCheck.objectName():
            SiteCheck.setObjectName(u"SiteCheck")
        SiteCheck.resize(923, 404)
        SiteCheck.setStyleSheet(u"background-color:rgb(16, 16, 16);\n"
"font: 9pt \"Arial\";")
        self.centralwidget = QWidget(SiteCheck)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 30, 230, 50))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(8, 8, 17);\n"
"	font: 700 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(13, 13, 29);\n"
"	font: 700 14pt \"Arial\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/C:/Users/user/Downloads/icons8-\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 110, 230, 70))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(8, 8, 17);\n"
"	font: 700 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(13, 13, 29);\n"
"	font: 700 14pt \"Arial\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/C:/Users/user/Downloads/icons8-\u043b\u0435\u0433\u043a\u043e-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.pushButton_2.setCheckable(False)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 290, 230, 70))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(8, 8, 17);\n"
"	font: 700 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(13, 13, 29);\n"
"	font: 700 14pt \"Arial\";\n"
"}")
        self.pushButton_3.setText(u" \u0421\u0430\u0439\u0442\u044b >")
        icon2 = QIcon()
        icon2.addFile(u":/icons/C:/Users/user/Downloads/icons8-\u0441\u0430\u0439\u0442-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.pushButton_3.setAutoExclusive(False)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 20, 641, 361))
        self.frame.setStyleSheet(u"background-color:rgb(21, 21, 21);\n"
"border:3px;\n"
"border-radius:10px")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(380, 290, 251, 61))
        self.label.setStyleSheet(u"font: 9pt \"Arial\";")
        self.xonebutton = QPushButton(self.frame)
        self.xonebutton.setObjectName(u"xonebutton")
        self.xonebutton.setGeometry(QRect(10, 50, 140, 40))
        self.xonebutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.midnightbutton = QPushButton(self.frame)
        self.midnightbutton.setObjectName(u"midnightbutton")
        self.midnightbutton.setGeometry(QRect(160, 50, 140, 40))
        self.midnightbutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.nixwarebutton = QPushButton(self.frame)
        self.nixwarebutton.setObjectName(u"nixwarebutton")
        self.nixwarebutton.setGeometry(QRect(310, 50, 140, 40))
        self.nixwarebutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.gmailbutton = QPushButton(self.frame)
        self.gmailbutton.setObjectName(u"gmailbutton")
        self.gmailbutton.setGeometry(QRect(160, 110, 140, 40))
        self.gmailbutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.mailbutton = QPushButton(self.frame)
        self.mailbutton.setObjectName(u"mailbutton")
        self.mailbutton.setGeometry(QRect(310, 110, 140, 40))
        self.mailbutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.oplatabutton = QPushButton(self.frame)
        self.oplatabutton.setObjectName(u"oplatabutton")
        self.oplatabutton.setGeometry(QRect(470, 110, 140, 40))
        self.oplatabutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.predatorbutton = QPushButton(self.frame)
        self.predatorbutton.setObjectName(u"predatorbutton")
        self.predatorbutton.setGeometry(QRect(10, 110, 140, 40))
        self.predatorbutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.youtubebutton = QPushButton(self.frame)
        self.youtubebutton.setObjectName(u"youtubebutton")
        self.youtubebutton.setGeometry(QRect(100, 220, 171, 51))
        self.youtubebutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.vkgroupbutton = QPushButton(self.frame)
        self.vkgroupbutton.setObjectName(u"vkgroupbutton")
        self.vkgroupbutton.setGeometry(QRect(310, 220, 171, 51))
        self.vkgroupbutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.en1gmabutton = QPushButton(self.frame)
        self.en1gmabutton.setObjectName(u"en1gmabutton")
        self.en1gmabutton.setGeometry(QRect(470, 50, 140, 40))
        self.en1gmabutton.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(28, 28, 28);\n"
"	font: 700 12pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(33, 33, 33);\n"
"	font: 700 12pt \"Arial\";\n"
"}")
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 200, 230, 70))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border:3px;\n"
"	border-radius:10px;\n"
"	background:rgb(8, 8, 17);\n"
"	font: 700 14pt \"Arial\";\n"
"}\n"
"QPushButton:hover{\n"
"	border:1px;\n"
"	border-radius:5px;\n"
"	background:rgb(13, 13, 29);\n"
"	font: 700 14pt \"Arial\";\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/C:/Users/user/Downloads/icons8-\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0439-\u0442\u0440\u0443\u0434-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 20))
        SiteCheck.setCentralWidget(self.centralwidget)

        self.retranslateUi(SiteCheck)

        QMetaObject.connectSlotsByName(SiteCheck)
    # setupUi
    # self.ui.midnightbutton.clicked.connect(self.ui.open_midnight)
        # self.ui.nixwarebutton.clicked.connect(self.ui.open_nixware)
        # self.ui.en1gmabutton.clicked.connect(self.ui.open_en1gma)
        # self.ui.predatorbutton.clicked.connect(self.ui.open_predator)
        # self.ui.gmailbutton.clicked.connect(self.ui.open_gmail)
        # self.ui.mailbutton.clicked.connect(self.ui.open_mail)
        # self.ui.oplatabutton.clicked.connect(self.ui.open_oplata)
        # self.ui.youtubebutton.clicked.connect(self.ui.open_ytstudio)
        # self.ui.vkgroupbutton.clicked.connect(self.ui.open_vkgroup)
    def open_xone(self):
        webbrowser.open('https://xone.fun/login')
    def open_midnight(self):
        webbrowser.open('https://midnight.im/usercp/')
    def open_nixware(self):
        webbrowser.open('https://nixware.cc/user-panel/subscriptions')
    def open_en1gma(self):
        webbrowser.open('https://en1gma.tech/forums/')
    def open_predator(self):
        webbrowser.open('https://predator.systems/panel/subscriptions')
    def open_gmail(self):
        webbrowser.open('https://gmail.com')
    def open_mail(self):
        webbrowser.open('https://mail.ru')
    def open_oplata(self):
        webbrowser.open('https://oplata.info')
    def open_ytstudio(self):
        webbrowser.open('https://studio.youtube.com')
    def open_vkgroup(self):
        webbrowser.open('https://vk.com/groups')
    
    def retranslateUi(self, SiteCheck):
        SiteCheck.setWindowTitle(QCoreApplication.translate("SiteCheck", u"ANCHECKER", None))
        self.pushButton.setText(QCoreApplication.translate("SiteCheck", u" \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("SiteCheck", u" EasyCheck", None))
        self.label.setText(QCoreApplication.translate("SiteCheck", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Credits:</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">anarchowitz</span><span style=\" font-size:7pt;\"> (creator)</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">yooma.su</span><span style=\" font-size:7pt;\"> (design/colors)</span></p></body></html>", None))
        self.xonebutton.setText(QCoreApplication.translate("SiteCheck", u"1. XONE", None))
        self.midnightbutton.setText(QCoreApplication.translate("SiteCheck", u"2. MIDNIGHT", None))
        self.nixwarebutton.setText(QCoreApplication.translate("SiteCheck", u"3. NIXWARE", None))
        self.gmailbutton.setText(QCoreApplication.translate("SiteCheck", u"5. GMAIL", None))
        self.mailbutton.setText(QCoreApplication.translate("SiteCheck", u"6. MAIL.RU", None))
        self.oplatabutton.setText(QCoreApplication.translate("SiteCheck", u"7. OPLATA.INFO", None))
        self.predatorbutton.setText(QCoreApplication.translate("SiteCheck", u"5. PREDATOR", None))
        self.youtubebutton.setText(QCoreApplication.translate("SiteCheck", u"8. YOUTUBE Studio", None))
        self.vkgroupbutton.setText(QCoreApplication.translate("SiteCheck", u"9.  VK Group", None))
        self.en1gmabutton.setText(QCoreApplication.translate("SiteCheck", u"4. EN1GMA", None))
        self.pushButton_4.setText(QCoreApplication.translate("SiteCheck", u" HardCheck", None))
    # retranslateUi

