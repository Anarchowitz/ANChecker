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

class Ui_HardCheck(object):
    def setupUi(self, HardCheck):
        if not HardCheck.objectName():
            HardCheck.setObjectName(u"HardCheck")
        HardCheck.resize(923, 404)
        HardCheck.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        HardCheck.setStyleSheet(u"background-color:rgb(16, 16, 16);\n"
"font: 9pt \"Arial\";")
        self.centralwidget = QWidget(HardCheck)
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
        self.hxd = QPushButton(self.frame)
        self.hxd.setObjectName(u"hxd")
        self.hxd.setGeometry(QRect(10, 50, 160, 40))
        self.hxd.setStyleSheet(u"QPushButton{\n"
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
        self.regscanner = QPushButton(self.frame)
        self.regscanner.setObjectName(u"regscanner")
        self.regscanner.setGeometry(QRect(210, 50, 160, 40))
        self.regscanner.setStyleSheet(u"QPushButton{\n"
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
        self.downloadview = QPushButton(self.frame)
        self.downloadview.setObjectName(u"downloadview")
        self.downloadview.setGeometry(QRect(410, 50, 160, 40))
        self.downloadview.setStyleSheet(u"QPushButton{\n"
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
        self.sac = QPushButton(self.frame)
        self.sac.setObjectName(u"sac")
        self.sac.setGeometry(QRect(10, 110, 160, 40))
        self.sac.setStyleSheet(u"QPushButton{\n"
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
        self.everything = QPushButton(self.frame)
        self.everything.setObjectName(u"everything")
        self.everything.setGeometry(QRect(210, 190, 160, 40))
        self.everything.setStyleSheet(u"QPushButton{\n"
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
        self.openedfilesview = QPushButton(self.frame)
        self.openedfilesview.setObjectName(u"openedfilesview")
        self.openedfilesview.setGeometry(QRect(410, 110, 160, 40))
        self.openedfilesview.setStyleSheet(u"QPushButton{\n"
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
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(210, 240, 171, 101))
        self.MUICacheView = QPushButton(self.frame)
        self.MUICacheView.setObjectName(u"MUICacheView")
        self.MUICacheView.setGeometry(QRect(210, 110, 160, 40))
        self.MUICacheView.setStyleSheet(u"QPushButton{\n"
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
        HardCheck.setCentralWidget(self.centralwidget)


        self.retranslateUi(HardCheck)

        QMetaObject.connectSlotsByName(HardCheck)
    # setupUi
    def open_HxD(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'HxD/HxD.exe')
        os.startfile(program_path)
    def open_SAC(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'SAC.bat')
        os.startfile(program_path)
    def open_RegScanner(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'RegScanner/RegScanner.exe')
        os.startfile(program_path)
    def open_OpenedFilesView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'Openedfilesview/OpenedFilesView.exe')
        os.startfile(program_path)
    def open_DownloadView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'BrowserDownloadsView/BrowserDownloadsView.exe')
        os.startfile(program_path)
    def open_Everything(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'Everything/Everything.exe')
        os.startfile(program_path)
    def open_MUICacheView(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        program_path = os.path.join(script_dir, 'assets', 'MUICacheView/MUICacheView.exe')
        os.startfile(program_path)    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ANCHECKER", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" \u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" EasyCheck", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:7pt;\">Credits:</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">anarchowitz</span><span style=\" font-size:7pt;\"> (creator)</span></p><p align=\"right\"><span style=\" font-size:7pt; font-weight:700;\">yooma.su</span><span style=\" font-size:7pt;\"> (design/colors)</span></p></body></html>", None))
        self.hxd.setText(QCoreApplication.translate("MainWindow", u"HxD", None))
        self.regscanner.setText(QCoreApplication.translate("MainWindow", u"RegScanner", None))
        self.downloadview.setText(QCoreApplication.translate("MainWindow", u"DownloadView", None))
        self.sac.setText(QCoreApplication.translate("MainWindow", u"SAC", None))
        self.everything.setText(QCoreApplication.translate("MainWindow", u"Everything", None))
        self.openedfilesview.setText(QCoreApplication.translate("MainWindow", u"OpenedFilesView", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"R3D | Xone | Midnight | MUTINY | Yeahnot | LeagueMode | Unreal | VRedux | FURIOS | otcv | Avira | Neverlose | ESPdX | BoBerHook | Legendware | EGHack | nixware.cc | HAUNTEDPROJECT| externalcrack | RAGER9 | RAGER8 | .ahk | WinX | PhoenixHack | OBR | OneByteRadar | Skinchanger | NAIM | EZinjector | Reborn | OneByteWall*Hack | Keter | Annihilation | Sapphire | f0rg0tten | Osiris | Multihack | Breakthrough | REKTWARE | D3m | ExtrimHack | EZfrags | Shark | RHcheats | FREEQN | Aqua | Boomwtf | Pphud | INDIGO | FRUX0 | hack | cheat | \u0447\u0438\u0442 | KlarWare | Aimware | Skeet | gamesense | Aurora | SpirtHack | Fatality | OneTap | ev0lve | Eternity | Z0rhack | Stickrpg | Demonside.us | Bhop | BunnyHop | AviraSAMOWARE | ExLoader | .amc | R8 | freeqn | imgui.ini", None))
        self.MUICacheView.setText(QCoreApplication.translate("MainWindow", u"MUICacheView", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" HardCheck >", None))
    # retranslateUi

