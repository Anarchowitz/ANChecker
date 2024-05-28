# ANCHECKER V2
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
    QSizePolicy, QWidget, QTextEdit, QPlainTextEdit)
from maininfo import Ui_MainWindow
from easycheck import Ui_EasyCheck
from hardcheck import Ui_HardCheck
from sitecheck import Ui_SiteCheck


class MainInfo(QMainWindow):
    def __init__(self):
        super(MainInfo, self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.open_easycheck)
        self.ui.pushButton_3.clicked.connect(self.open_sitecheck)
        self.ui.pushButton_4.clicked.connect(self.open_hardcheck)
    def open_easycheck(self):
        self.close()
        self.easycheck = EasyCheck()
        self.easycheck.show()
    def open_hardcheck(self):
        self.close()
        self.easycheck = HardCheck()
        self.easycheck.show()
    def open_sitecheck(self):
        self.close()
        self.easycheck = SiteCheck()
        self.easycheck.show()

class EasyCheck(QMainWindow):
    def __init__(self):
        super(EasyCheck, self).__init__()
        self.ui= Ui_EasyCheck()
        self.ui.setupUi(self)
        self.ui.information.clicked.connect(self.open_info)
        self.ui.HardCheck.clicked.connect(self.open_hardcheck)
        self.ui.sites.clicked.connect(self.open_sitecheck)
        #--programs
        self.ui.LastActivityView.clicked.connect(self.ui.open_LastActivityView)
        self.ui.Shellbags.clicked.connect(self.ui.open_Shellbags)
        self.ui.UserAsstisView.clicked.connect(self.ui.open_UserAssistView)
        self.ui.UsbDeview.clicked.connect(self.ui.open_UsbDeview)
        self.ui.JumpListView.clicked.connect(self.ui.open_JumpListView)
        self.ui.OpenFolders.clicked.connect(self.ui.open_OpenFolders)
        self.ui.ProcessHacker.clicked.connect(self.ui.open_ProcessHacker)
    def open_info(self):
        self.close()
        self.easycheck = MainInfo()
        self.easycheck.show()
    def open_hardcheck(self):
        self.close()
        self.easycheck = HardCheck()
        self.easycheck.show()
    def open_sitecheck(self):
        self.close()
        self.easycheck = SiteCheck()
        self.easycheck.show()

class HardCheck(QMainWindow):
    def __init__(self):
        super(HardCheck, self).__init__()
        self.ui= Ui_HardCheck()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.open_easycheck)
        self.ui.pushButton_3.clicked.connect(self.open_sitecheck)
        self.ui.pushButton.clicked.connect(self.open_info)
        #--programs
        self.ui.hxd.clicked.connect(self.ui.open_HxD)
        self.ui.sac.clicked.connect(self.ui.open_SAC)
        self.ui.regscanner.clicked.connect(self.ui.open_RegScanner)
        self.ui.downloadview.clicked.connect(self.ui.open_DownloadView)
        self.ui.openedfilesview.clicked.connect(self.ui.open_OpenedFilesView)
        self.ui.everything.clicked.connect(self.ui.open_Everything)
        self.ui.MUICacheView.clicked.connect(self.ui.open_MUICacheView)
    def open_easycheck(self):
        self.close()
        self.easycheck = EasyCheck()
        self.easycheck.show()
    def open_info(self):
        self.close()
        self.easycheck = MainInfo()
        self.easycheck.show()
    def open_sitecheck(self):
        self.close()
        self.easycheck = SiteCheck()
        self.easycheck.show()

class SiteCheck(QMainWindow):
    def __init__(self):
        super(SiteCheck, self).__init__()
        self.ui= Ui_SiteCheck()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.open_easycheck)
        self.ui.pushButton_4.clicked.connect(self.open_hardcheck)
        self.ui.pushButton.clicked.connect(self.open_info)
        #--sites
        self.ui.xonebutton.clicked.connect(self.ui.open_xone)
        self.ui.midnightbutton.clicked.connect(self.ui.open_midnight)
        self.ui.nixwarebutton.clicked.connect(self.ui.open_nixware)
        self.ui.en1gmabutton.clicked.connect(self.ui.open_en1gma)
        self.ui.predatorbutton.clicked.connect(self.ui.open_predator)
        self.ui.gmailbutton.clicked.connect(self.ui.open_gmail)
        self.ui.mailbutton.clicked.connect(self.ui.open_mail)
        self.ui.oplatabutton.clicked.connect(self.ui.open_oplata)
        self.ui.youtubebutton.clicked.connect(self.ui.open_ytstudio)
        self.ui.vkgroupbutton.clicked.connect(self.ui.open_vkgroup)
    def open_easycheck(self):
        self.close()
        self.easycheck = EasyCheck()
        self.easycheck.show()
    def open_info(self):
        self.close()
        self.easycheck = MainInfo()
        self.easycheck.show()
    def open_hardcheck(self):
        self.close()
        self.easycheck = HardCheck()
        self.easycheck.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainInfo()
    window.show()
    sys.exit(app.exec())
