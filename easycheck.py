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

class Ui_EasyCheck(object):
    def setupUi(self, EasyCheck):
        if not EasyCheck.objectName():
            EasyCheck.setObjectName(u"EasyCheck")
        EasyCheck.resize(923, 404)
        EasyCheck.setStyleSheet(u"background-color:rgb(16, 16, 16)")
        self.centralwidget = QWidget(EasyCheck)
        self.centralwidget.setObjectName(u"centralwidget")
        self.information = QPushButton(self.centralwidget)
        self.information.setObjectName(u"information")
        self.information.setGeometry(QRect(0, 30, 230, 50))
        self.information.setStyleSheet(u"QPushButton{\n"
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
        self.information.setIcon(icon)
        self.information.setIconSize(QSize(20, 20))
        self.information.setCheckable(False)
        self.information.setChecked(False)
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
        self.sites = QPushButton(self.centralwidget)
        self.sites.setObjectName(u"sites")
        self.sites.setGeometry(QRect(0, 290, 230, 70))
        self.sites.setStyleSheet(u"QPushButton{\n"
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
        self.sites.setText(u" \u0421\u0430\u0439\u0442\u044b")
        icon2 = QIcon()
        icon2.addFile(u":/icons/C:/Users/user/Downloads/icons8-\u0441\u0430\u0439\u0442-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sites.setIcon(icon2)
        self.sites.setIconSize(QSize(20, 20))
        self.sites.setAutoExclusive(False)
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
        self.LastActivityView = QPushButton(self.frame)
        self.LastActivityView.setObjectName(u"LastActivityView")
        self.LastActivityView.setGeometry(QRect(10, 60, 161, 41))
        self.LastActivityView.setStyleSheet(u"QPushButton{\n"
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
        self.Shellbags = QPushButton(self.frame)
        self.Shellbags.setObjectName(u"Shellbags")
        self.Shellbags.setGeometry(QRect(10, 120, 161, 41))
        self.Shellbags.setStyleSheet(u"QPushButton{\n"
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
        self.UserAsstisView = QPushButton(self.frame)
        self.UserAsstisView.setObjectName(u"UserAsstisView")
        self.UserAsstisView.setGeometry(QRect(10, 190, 161, 41))
        self.UserAsstisView.setStyleSheet(u"QPushButton{\n"
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
        self.ProcessHacker = QPushButton(self.frame)
        self.ProcessHacker.setObjectName(u"ProcessHacker")
        self.ProcessHacker.setGeometry(QRect(430, 20, 161, 41))
        self.ProcessHacker.setStyleSheet(u"QPushButton{\n"
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
        self.UsbDeview = QPushButton(self.frame)
        self.UsbDeview.setObjectName(u"UsbDeview")
        self.UsbDeview.setGeometry(QRect(200, 60, 161, 41))
        self.UsbDeview.setStyleSheet(u"QPushButton{\n"
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
        self.JumpListView = QPushButton(self.frame)
        self.JumpListView.setObjectName(u"JumpListView")
        self.JumpListView.setGeometry(QRect(200, 120, 161, 41))
        self.JumpListView.setStyleSheet(u"QPushButton{\n"
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
        self.OpenFolders = QPushButton(self.frame)
        self.OpenFolders.setObjectName(u"OpenFolders")
        self.OpenFolders.setGeometry(QRect(200, 190, 161, 41))
        self.OpenFolders.setStyleSheet(u"QPushButton{\n"
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 30, 5, 221))
        self.label_2.setStyleSheet(u"background:rgb(28, 28, 28);")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(410, 70, 221, 181))
        self.HardCheck = QPushButton(self.centralwidget)
        self.HardCheck.setObjectName(u"HardCheck")
        self.HardCheck.setGeometry(QRect(0, 200, 230, 70))
        self.HardCheck.setStyleSheet(u"QPushButton{\n"
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
        self.HardCheck.setIcon(icon3)
        self.HardCheck.setIconSize(QSize(20, 20))
        EasyCheck.setCentralWidget(self.centralwidget)

        self.retranslateUi(EasyCheck)

        QMetaObject.connectSlotsByName(EasyCheck)
    # setupUi
    def open_LastActivityView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'LastactivityView/LastactivityView.exe')
        os.startfile(program_path)
    def open_Shellbags(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'Shellbags/Shellbags.exe')
        os.startfile(program_path)
    def open_UserAssistView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'UserAssistView/UserAssistView.exe')
        os.startfile(program_path)
    def open_UsbDeview(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'UsbDeview/UsbDeview.exe')
        os.startfile(program_path)
    def open_JumpListView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'JumpListView/JumpListView.exe')
        os.startfile(program_path)
    def open_OpenFolders(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'OpenFolder.bat')
        os.startfile(program_path)
    def open_ProcessHacker(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'ProcessHacker/ProcessHacker.exe')
        os.startfile(program_path)

    def retranslateUi(self, EasyCheck):
        EasyCheck.setWindowTitle(QCoreApplication.translate("EasyCheck", u"ANCHECKER", None))
        self.information.setText(QCoreApplication.translate("EasyCheck", u" \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("EasyCheck", u" EasyCheck >", None))
        self.label.setText(QCoreApplication.translate("EasyCheck", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Credits:</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">anarchowitz</span><span style=\" font-size:7pt;\"> (creator)</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">yooma.su</span><span style=\" font-size:7pt;\"> (design/colors)</span></p></body></html>", None))
        self.LastActivityView.setText(QCoreApplication.translate("EasyCheck", u"LastActivityView", None))
        self.Shellbags.setText(QCoreApplication.translate("EasyCheck", u"ShellBags", None))
        self.UserAsstisView.setText(QCoreApplication.translate("EasyCheck", u"UserAssistView", None))
        self.ProcessHacker.setText(QCoreApplication.translate("EasyCheck", u"Process Hacker 2", None))
        self.UsbDeview.setText(QCoreApplication.translate("EasyCheck", u"UsbDeview", None))
        self.JumpListView.setText(QCoreApplication.translate("EasyCheck", u"JumpListView", None))
        self.OpenFolders.setText(QCoreApplication.translate("EasyCheck", u"Appdata/Others", None))
        self.label_2.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("EasyCheck", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<br />Aimbot<br />Exloader<br />Fecurity<br />Tkazer</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aimstar</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">XONE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Midnight</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">triggerbot</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cheat</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wallhack</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nixwar"
                        "e</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Aimware</p></body></html>", None))
        self.HardCheck.setText(QCoreApplication.translate("EasyCheck", u" HardCheck", None))
    # retranslateUi

