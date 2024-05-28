import sys, os, subprocess, configparser, time
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget, QTextEdit, QPlainTextEdit)
import anchecker_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 404)
        MainWindow.setStyleSheet(u"background-color:rgb(16, 16, 16);\n"
"font: 9pt \"Arial\";")
        self.centralwidget = QWidget(MainWindow)
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
        self.pushButton_3.setText(u" \u0421\u0430\u0439\u0442\u044b")
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 641, 281))
        self.label_2.setStyleSheet(u"font: 9pt \"Arial\";")
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ANCHECKER", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f >", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" EasyCheck", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Credits:</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">anarchowitz</span><span style=\" font-size:7pt;\"> (creator)</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">yooma.su</span><span style=\" font-size:7pt;\"> (design/colors)</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">ANChecker</span><span style=\" font-size:10pt; font-weight:700;\"> - \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u043d\u0430 \u0447\u0438\u0442\u044b \u0438\u0433\u0440\u043e\u043a\u043e\u0432.<br/><br/></span><span style=\" font-size:10pt;\">\u0412 \u043d\u0430\u0448\u0435\u0439 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 - \u0435\u0441\u0442\u044c \u0442\u0430\u043a\u0438\u0435 \u043c\u043d\u043e\u0433\u043e\u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043a\u0430\u043a:<br/></span><span style=\" font-size:10pt; font-weight:700;\"><br/>SAC<br/>BrowserDownloadView<br/>LastActivityView<br/>Shellbag Analyzer<br/>RegScanner<br/>UsbDeview<br/>UserAssistView<br/>OpenedFilesView<br/>HxD<br/>Appdata/Others</span></p><p><span style=\" font-size:10pt;\">\u041f\u043e"
                        "\u0434\u0445\u043e\u0434\u0438\u0442 \u043a\u0430\u043a \u0434\u043b\u044f HardCheck, \u043a\u0430\u043a \u0438 EasyCheck</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" HardCheck", None))
    # retranslateUi

