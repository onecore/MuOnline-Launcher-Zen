# -*- coding: utf-8 -*-

## CoreSECURITY Software Development Group
## Mark Anthony Pequeras
## Licensed Under GPLv2
## The Power of Python
## InvictuzMU Online Launcher

from PyQt4 import QtCore, QtGui
from subprocess import Popen
from Settings import mainSettings
import urllib, urllib2


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(906, 480)
        Form.setMinimumSize(QtCore.QSize(906, 480))
        Form.setMaximumSize(QtCore.QSize(906, 480))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setStyleSheet(_fromUtf8("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #333751);"))

        self.OrangeBar = QtGui.QPlainTextEdit(Form)
        self.OrangeBar.setEnabled(False)
        self.OrangeBar.setGeometry(QtCore.QRect(70, 20, 641, 311))
        self.OrangeBar.setStyleSheet(_fromUtf8("border-radius: 15px 33px 22px 33px;\n"
"border: 3px outset #333751;\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #26293B);"))
        self.OrangeBar.setObjectName(_fromUtf8("OrangeBar"))
        self.SMScredit = QtGui.QLabel(Form)
        self.SMScredit.setGeometry(QtCore.QRect(720, 210, 141, 91))
        self.SMScredit.setStyleSheet(_fromUtf8("background: transparent;\n"
""))
        self.SMScredit.setText(_fromUtf8(""))
        self.SMScredit.setPixmap(QtGui.QPixmap(_fromUtf8("CSImages/smscreds.jpg")))
        self.SMScredit.setObjectName(_fromUtf8("SMScredit"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(720, 310, 131, 51))
        self.label_3.setStyleSheet(_fromUtf8("background: transparent;"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("CSImages/webshop.jpg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.MuLogoTop = QtGui.QLabel(Form)
        self.MuLogoTop.setGeometry(QtCore.QRect(350, 0, 201, 71))
        self.MuLogoTop.setStyleSheet(_fromUtf8("background: transparent;"))
        self.MuLogoTop.setText(_fromUtf8(""))
        self.MuLogoTop.setPixmap(QtGui.QPixmap(_fromUtf8("CSImages/reg_logo.png")))
        self.MuLogoTop.setObjectName(_fromUtf8("MuLogoTop"))
        self.redplus = QtGui.QLabel(Form)
        self.redplus.setGeometry(QtCore.QRect(680, 30, 16, 16))
        self.redplus.setStyleSheet(_fromUtf8("background: transparent;"))
        self.redplus.setText(_fromUtf8(""))
        self.redplus.setPixmap(QtGui.QPixmap(_fromUtf8("CSImages/arrow.gif")))
        self.redplus.setObjectName(_fromUtf8("redplus"))

        self.WebshopButton = QtGui.QPushButton(Form)
        self.WebshopButton.setGeometry(QtCore.QRect(720, 310, 131, 51))
        self.WebshopButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.WebshopButton.setStyleSheet(_fromUtf8("border-image: url(CSImages/round.gif);\n"
"background: transparent;"))
        self.WebshopButton.setText(_fromUtf8(""))
        self.WebshopButton.setObjectName(_fromUtf8("WebshopButton"))
        self.SMSCreditsButtons = QtGui.QPushButton(Form)
        self.SMSCreditsButtons.setGeometry(QtCore.QRect(720, 220, 141, 71))
        self.SMSCreditsButtons.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.SMSCreditsButtons.setStyleSheet(_fromUtf8("border-image: url(CSImages/round.gif);\n"
"background: transparent;"))
        self.SMSCreditsButtons.setText(_fromUtf8(""))
        self.SMSCreditsButtons.setObjectName(_fromUtf8("SMSCreditsButtons"))
        self.VoteButton = QtGui.QPushButton(Form)
        self.VoteButton.setGeometry(QtCore.QRect(720, 140, 151, 61))
        self.VoteButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.VoteButton.setStyleSheet(_fromUtf8("\n"
"background: transparent;\n"
"border-image: url(CSImages/votebanner.jpg);"))
        self.VoteButton.setText(_fromUtf8(""))
        self.VoteButton.setObjectName(_fromUtf8("VoteButton"))
        openslide = open('Settings/News/Slider.py', 'r+')
        rslide = openslide.read()
        eslide = eval(str(rslide))

        opennews = open('Settings/News/News.py', 'r+')
        rnews = opennews.read()
        enews = eval(str(rnews))



        self.WebViewScrollingImages = QtWebKit.QWebView(Form)
        self.WebViewScrollingImages.setGeometry(QtCore.QRect(190, 70, 251, 251))
        self.WebViewScrollingImages.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.WebViewScrollingImages.setStyleSheet(_fromUtf8("background: transparent;\n"
""))
        self.WebViewScrollingImages.setUrl(QtCore.QUrl(_fromUtf8(str(eslide))))
        self.WebViewScrollingImages.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.WebViewScrollingImages.setObjectName(_fromUtf8("WebViewScrollingImages"))
        self.WebViewNewsEvents = QtWebKit.QWebView(Form)
        self.WebViewNewsEvents.setGeometry(QtCore.QRect(450, 70, 251, 251))
        self.WebViewNewsEvents.setUrl(QtCore.QUrl(_fromUtf8(str(enews))))
        self.WebViewNewsEvents.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.NonCosmeticDefaultPen|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.WebViewNewsEvents.setObjectName(_fromUtf8("WebViewNewsEvents"))
        self.LatestVersionName = QtGui.QLabel(Form)
        self.LatestVersionName.setGeometry(QtCore.QRect(720, 380, 81, 16))
        self.LatestVersionName.setStyleSheet(_fromUtf8("color: rgb(145, 145, 145);"))
        self.LatestVersionName.setObjectName(_fromUtf8("LatestVersionName"))
        self.YourVersionName = QtGui.QLabel(Form)
        self.YourVersionName.setGeometry(QtCore.QRect(720, 400, 81, 16))
        self.YourVersionName.setStyleSheet(_fromUtf8("color: rgb(145, 145, 145);"))
        self.YourVersionName.setObjectName(_fromUtf8("YourVersionName"))
        self.StatusName = QtGui.QLabel(Form)
        self.StatusName.setGeometry(QtCore.QRect(720, 420, 61, 20))
        self.StatusName.setStyleSheet(_fromUtf8("color: rgb(145, 145, 145);"))
        self.StatusName.setObjectName(_fromUtf8("StatusName"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(780, 420, 81, 16))
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(188, 188, 188);"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.NotificationBox = QtGui.QPlainTextEdit(Form)
        self.NotificationBox.setGeometry(QtCore.QRect(320, 330, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.NotificationBox.setFont(font)
        self.NotificationBox.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);\n"
"background: transparent;"
"border: none;"))
        self.NotificationBox.insertPlainText(_fromUtf8(""))
        self.NotificationBox.setObjectName(_fromUtf8("NotificationBox"))
        self.NotificationBox.setDisabled(1)


        self.NotificationBox2 = QtGui.QPlainTextEdit(Form)
        self.NotificationBox2.setGeometry(QtCore.QRect(320, 330, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.NotificationBox2.setFont(font)
        self.NotificationBox2.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);\n"
"background: transparent;"
"border: none;"))
        self.NotificationBox2.insertPlainText(_fromUtf8(""))
        self.NotificationBox2.setObjectName(_fromUtf8("NotificationBox2"))
        self.NotificationBox2.setDisabled(1)


        self.ServerName = QtGui.QLabel(Form)
        self.ServerName.setGeometry(QtCore.QRect(100, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monotype Corsiva"))
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.ServerName.setFont(font)
        self.ServerName.setStyleSheet(_fromUtf8("background: none;\n"
"\n"
"\n"
"\n"
"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));"))
        self.ServerName.setObjectName(_fromUtf8("ServerName"))

        self.CurrentVersionLabel = QtGui.QLabel(Form)
        self.CurrentVersionLabel.setGeometry(QtCore.QRect(800, 400, 61, 16))
        self.CurrentVersionLabel.setStyleSheet(_fromUtf8("color: rgb(145, 145, 145);"))
        self.CurrentVersionLabel.setObjectName(_fromUtf8("CurrentVersionLabel"))
        self.LatestVersionLabel = QtGui.QLabel(Form)
        self.LatestVersionLabel.setGeometry(QtCore.QRect(800, 380, 61, 16))
        self.LatestVersionLabel.setStyleSheet(_fromUtf8("color: rgb(145, 145, 145);"))
        self.LatestVersionLabel.setObjectName(_fromUtf8("LatestVersionLabel"))
        self.ServerStatusLabel = QtGui.QLabel(Form)
        self.ServerStatusLabel.setGeometry(QtCore.QRect(100, 80, 71, 16))
        self.ServerStatusLabel.setStyleSheet(_fromUtf8("color: rgb(129, 129, 129);\n"
"background: none;"))
        self.ServerStatusLabel.setObjectName(_fromUtf8("ServerStatusLabel"))
        self.OnlineLabel = QtGui.QLabel(Form)
        self.OnlineLabel.setGeometry(QtCore.QRect(80, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OnlineLabel.setFont(font)
        self.OnlineLabel.setStyleSheet(_fromUtf8("color: rgb(91, 170, 0);"))
        self.OnlineLabel.setObjectName(_fromUtf8("OnlineLabel"))
        self.HorizontalLine = QtGui.QFrame(Form)
        self.HorizontalLine.setGeometry(QtCore.QRect(80, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.HorizontalLine.setFont(font)
        self.HorizontalLine.setStyleSheet(_fromUtf8("background: none;"))
        self.HorizontalLine.setFrameShape(QtGui.QFrame.HLine)
        self.HorizontalLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.HorizontalLine.setObjectName(_fromUtf8("HorizontalLine"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(720, 50, 161, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet(_fromUtf8("border-image: url(CSImages/left_main_snsImg100408.jpg);"))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Closebutton = QtGui.QPushButton(Form)
        self.Closebutton.setGeometry(QtCore.QRect(20, 20, 40, 40))
        self.Closebutton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.Closebutton.setStyleSheet(_fromUtf8("QPushButton{border-image: url(CSImages/closetekster.png);\n"
"\n"
"\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-image: url(CSImages/hover.png);\n"
"}"))
        self.Closebutton.setText(_fromUtf8(""))
        self.Closebutton.setObjectName(_fromUtf8("Closebutton"))
        self.MinimizeButton = QtGui.QPushButton(Form)
        self.MinimizeButton.setGeometry(QtCore.QRect(20, 60, 25, 29))
        self.MinimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.MinimizeButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton{border-image:  url(CSImages/minimizetekster.png);\n"
"\n"
"\n"
"background: transparent;}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"border-image: url(CSImages/MinHoverTekster.png);\n"
"}"))
        self.MinimizeButton.setText(_fromUtf8(""))
        self.MinimizeButton.setObjectName(_fromUtf8("MinimizeButton"))
        self.Wizard = QtGui.QLabel(Form)
        self.Wizard.setGeometry(QtCore.QRect(0, 110, 291, 341))
        self.Wizard.setStyleSheet(_fromUtf8("background: transparent;"))
        self.Wizard.setText(_fromUtf8(""))
        self.Wizard.setPixmap(QtGui.QPixmap(_fromUtf8("Invictuz.png")))
        self.Wizard.setScaledContents(True)
        self.Wizard.setObjectName(_fromUtf8("Wizard"))
        self.CheckForUpdateButton = QtGui.QPushButton(Form)
        self.CheckForUpdateButton.setGeometry(QtCore.QRect(190, 400, 111, 41))
        self.CheckForUpdateButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.CheckForUpdateButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9);\n"
"color: #ffffff;\n"
"border: 2px outset #333751;\n"
"border-radius: 5px 5px 5px 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.CheckForUpdateButton.setObjectName(_fromUtf8("CheckForUpdateButton"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(310, 350, 391, 111))
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::tab-bar {\n"
"background: none;\n"
"border: transparent;\n"
"border-color: transparent;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #26293B , stop: 1 #26293B);\n"
"  color: white;\n"
"border: none;\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: orange;\n"
"border: none;\n"
" }\n"
"\n"
"\n"
"QTabWidget::pane { border: 0; }"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.PlayNow = QtGui.QWidget()
        self.PlayNow.setObjectName(_fromUtf8("PlayNow"))
        self.StartGameButton_5 = QtGui.QPushButton(self.PlayNow)
        self.StartGameButton_5.setGeometry(QtCore.QRect(210, 20, 161, 41))
        self.StartGameButton_5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.StartGameButton_5.setStyleSheet(_fromUtf8("border-image: url(CSImages/bt_gamestart.gif);"))
        self.StartGameButton_5.setText(_fromUtf8(""))
        self.StartGameButton_5.setObjectName(_fromUtf8("StartGameButton_5"))
        self.NewsInStartGame_5 = QtGui.QLabel(self.PlayNow)
        self.NewsInStartGame_5.setGeometry(QtCore.QRect(10, 0, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.NewsInStartGame_5.setFont(font)
        self.NewsInStartGame_5.setStyleSheet(_fromUtf8("background: none;\n"
"color: #ffffff;"))
        self.NewsInStartGame_5.setObjectName(_fromUtf8("NewsInStartGame_5"))
        self.OrangeLetterC_5 = QtGui.QLabel(self.PlayNow)
        self.OrangeLetterC_5.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.OrangeLetterC_5.setText(_fromUtf8(""))
        self.OrangeLetterC_5.setPixmap(QtGui.QPixmap(_fromUtf8("CSImages/icon_wcoinc.gif")))
        self.OrangeLetterC_5.setObjectName(_fromUtf8("OrangeLetterC_5"))
        self.tabWidget.addTab(self.PlayNow, _fromUtf8(""))
        self.SettingsTab = QtGui.QWidget()
        self.SettingsTab.setObjectName(_fromUtf8("SettingsTab"))
        self.SaveUsernameButton_5 = QtGui.QPushButton(self.SettingsTab)
        self.SaveUsernameButton_5.setGeometry(QtCore.QRect(250, 10, 131, 51))
        self.SaveUsernameButton_5.setStyleSheet(_fromUtf8("QPushButton{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffcc00, stop: 1 #b87f2b);\n"
"color: #ffffff;\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2980b9, stop: 1 #3498db);\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
""))
        self.SaveUsernameButton_5.setObjectName(_fromUtf8("SaveUsernameButton_5"))
        self.label_33 = QtGui.QLabel(self.SettingsTab)
        self.label_33.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_33.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.SettingsTab)
        self.label_34.setGeometry(QtCore.QRect(140, 40, 91, 16))
        self.label_34.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.WindowsOnorFullSlider = QtGui.QSlider(self.SettingsTab)
        self.WindowsOnorFullSlider.setGeometry(QtCore.QRect(90, 40, 41, 19))
        self.WindowsOnorFullSlider.setStyleSheet(_fromUtf8("background: none;"))
        self.WindowsOnorFullSlider.setMaximum(2)
        self.WindowsOnorFullSlider.setValue(1)
        self.WindowsOnorFullSlider.setOrientation(QtCore.Qt.Horizontal)
        self.WindowsOnorFullSlider.setObjectName(_fromUtf8("WindowsOnorFullSlider"))
        self.WindowsOnorFullSlider.setDisabled(1)
        self.comboBox_5 = QtGui.QComboBox(self.SettingsTab)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 10, 171, 22))
        self.comboBox_5.setStyleSheet(_fromUtf8("QComboBox { \n"
"\n"
"     border-radius: 8px 8px 8px 8px; \n"
"\n"
"     padding: 1px 1px 1px 1px; \n"
"     min-width: 6em; \n"
"     color: rgb(220, 220, 220); \n"
"     background-color: #ffffff; \n"
"     margin: 0 0 0 0; \n"
" } \n"
"  \n"
" QComboBox:editable { \n"
"     background: rgb(80, 80, 80); \n"
" } \n"
"  \n"
" QComboBox:!editable { \n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
" } \n"
"  \n"
" QComboBox::drop-down:editable {background: #ffffff \n"
" } \n"
"  \n"
" QComboBox:!editable:on { \n"
" } \n"
"  \n"
" QComboBox::drop-down:editable:on { \n"
" } \n"
"  \n"
" QComboBox:on { /* shift the text when the popup opens */ \n"
"     padding-top: 3px; \n"
"     padding-left: 4px; \n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
" } \n"
"  \n"
" QComboBox::drop-down { \n"
"     subcontrol-origin: padding; \n"
"     subcontrol-position: center right; \n"
"     width: 15px;  \n"
"     right:3px; \n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */ \n"
"     border-bottom-right-radius: 3px; \n"
"     background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3498db, stop: 1 #2980b9); \n"
" } \n"
"  \n"
" QComboBox::down-arrow { \n"
"     image: url(TeskterImages/closetekster.png); \n"
"     height: 10px; \n"
" } \n"
"  \n"
" QComboBox::down-arrow:on { /* shift the arrow when popup is open */ \n"
"     top: 1px; \n"
"     left: 1px; \n"
" } \n"
"  \n"
" QListView#comboListView { \n"
"     background: rgb(80, 80, 80); \n"
"     color: rgb(220, 220, 220); \n"
"     min-height: 90px; \n"
"     margin: 0 0 0 0; \n"
" } \n"
"  \n"
" QListView#comboListView::item { \n"
"     background-color: rgb(80, 80, 80); \n"
" } \n"
"  \n"
" QListView#comboListView::item:hover { \n"
"     background-color: rgb(95, 95, 95); }"))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.SettingsTab)
        self.label.setGeometry(QtCore.QRect(30, 60, 51, 16))
        self.label.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.SettingsTab)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.SoundsOnandOffSlider = QtGui.QSlider(self.SettingsTab)
        self.SoundsOnandOffSlider.setGeometry(QtCore.QRect(90, 60, 41, 19))
        self.SoundsOnandOffSlider.setStyleSheet(_fromUtf8("color: #ffffff;\n"
"background: none;"))
        self.SoundsOnandOffSlider.setMaximum(2)
        self.SoundsOnandOffSlider.setValue(1)
        self.SoundsOnandOffSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SoundsOnandOffSlider.setObjectName(_fromUtf8("SoundsOnandOffSlider"))
        self.tabWidget.addTab(self.SettingsTab, _fromUtf8(""))
        self.ContactTab = QtGui.QWidget()
        self.ContactTab.setObjectName(_fromUtf8("ContactTab"))
        self.label_36 = QtGui.QLabel(self.ContactTab)
        self.label_36.setGeometry(QtCore.QRect(10, 10, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(_fromUtf8("color: rgb(166, 166, 166);\n"
"background: none;"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.tabWidget.addTab(self.ContactTab, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.WebshopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.WebshopWebFunction)
        QtCore.QObject.connect(self.SMSCreditsButtons, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SMSwebFunction)
        QtCore.QObject.connect(self.VoteButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.VoteButtonFunction)
        QtCore.QObject.connect(self.CheckForUpdateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CheckforUpdatesTrigger)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SocialsBarFunction)
        QtCore.QObject.connect(self.Closebutton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close)
        QtCore.QObject.connect(self.MinimizeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showMinimized)
        QtCore.QObject.connect(self.StartGameButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.StartGameFunction)
        QtCore.QObject.connect(self.SaveUsernameButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.SaveWindowsandSoundsFunction)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        import urllib
        Form.setWindowTitle(_translate("Form", "Launcher", None))
        self.LatestVersionName.setText(_translate("Form", "  Latest Version:", None))
        self.YourVersionName.setText(_translate("Form", "  Your Version:  ", None))
        self.StatusName.setText(_translate("Form", "  Status: ", None))
        readup = mainSettings.Updater
        lwebversion = urllib.urlopen(str(readup)+'/csupdater/LatestVersion.txt')
        readwebver = lwebversion.read()    #Read Version Web
        openverss = open('Version.py', 'r+')
        for xxxx in openverss:
            spxx = xxxx.split(',')
            readxxx = spxx[-1]

        #self.label_11.setText(_translate("Form", "          Check for Update!", None))

        if float(readwebver) > float(readxxx):
            self.label_11.setText('Please Update!')
        else:
            self.label_11.setText('Updated!')
            pass



        self.ServerName.setText(_translate("Form", mainSettings.Server, None))
        self.CheckForUpdateButton.setText(_translate("Form", "Check for Updates", None))
        openver = open('Version.py', 'r+')
        for ov in openver:
            ovc = ov.split(',')
            versx = ovc[-1]
        self.CurrentVersionLabel.setText(_translate("Form", "              " + str(versx), None))
        openver.close()
        readup = mainSettings.Updater
        lwebversion = urllib.urlopen(str(readup)+'/csupdater/LatestVersion.txt')
        readwebver = lwebversion.read()
        self.LatestVersionLabel.setText(_translate("Form", "              " + str(readwebver), None))
        self.ServerStatusLabel.setText(_translate("Form", "Server Status", None))
        self.OnlineLabel.setText(_translate("Form", "       ONLINE", None))
        self.NewsInStartGame_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#949494;\">You might want to take a check</span></p><p><span style=\" color:#949494;\">first at the Settings tab before</span></p><p><span style=\" color:#949494;\">Starting the Game?</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PlayNow), _translate("Form", "Play Now", None))
        self.SaveUsernameButton_5.setText(_translate("Form", "Save Settings", None))
        self.label_33.setText(_translate("Form", "Windows Mode", None))
        self.label_34.setText(_translate("Form", "Full Screen Mode", None))
        self.comboBox_5.setCurrentIndex(3)
        self.comboBox_5.setItemText(0, _translate("Form", "     800x600  Window Screen", None))
        self.comboBox_5.setItemText(1, _translate("Form", "     1024x768  Window Screen", None))
        self.comboBox_5.setItemText(2, _translate("Form", "     1280x1024  Window Screen", None))
        self.comboBox_5.setItemText(3, _translate("Form", "     Select Window Size", None))
        self.comboBox_5.setItemText(4, _translate("Form", "     800x600  Full Screen", None))
        self.comboBox_5.setItemText(5, _translate("Form", "     1024x768 Full Screen", None))
        self.comboBox_5.setItemText(6, _translate("Form", "     1280x1024 Full Screen", None))
        self.label.setText(_translate("Form", "Sounds On", None))
        self.label_2.setText(_translate("Form", "Sounds Off", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SettingsTab), _translate("Form", "Settings", None))
        self.label_36.setText(_translate("Form", "<html><head/><body><p><b>This Software is brought to you by CoreSEC Software Development </p></b><p>Contact Us for more infromations at     <u>http://coresec.sf.net/</u></p><br/><br/></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ContactTab), _translate("Form", "Contact Us", None))



    def WebshopWebFunction(self):
        file = open('Settings/Buttons/WebshopLink.py', 'r+')
        rfile = file.read()
        strfile = eval(str(rfile))
        rightnews = self.WebViewNewsEvents
        rightnews.setUrl(QtCore.QUrl(_fromUtf8(str(strfile))))
        rightnews.setGeometry(QtCore.QRect(190, 70, 500, 251))

    def SMSwebFunction(self):
        file = open('Settings/Buttons/SmsLink.py', 'r+')
        rfile = file.read()
        strfile = eval(str(rfile))
        rightnewsc = self.WebViewNewsEvents
        rightnewsc.setUrl(QtCore.QUrl(_fromUtf8(str(strfile))))
        rightnewsc.setGeometry(QtCore.QRect(190, 70, 500, 251))


    def VoteButtonFunction(self):
        file = open('Settings/Buttons/VoteLink.py', 'r+')
        rfile = file.read()
        strfile = eval(str(rfile))
        rightnewsx = self.WebViewNewsEvents
        rightnewsx.setUrl(QtCore.QUrl(_fromUtf8(str(strfile))))
        rightnewsx.setGeometry(QtCore.QRect(190, 70, 500, 251))


    def CheckforUpdatesTrigger(self):
        self.timer = QtCore.QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.CheckforUpdatesFunction)
        self.timer.start(1000)


    def CheckforUpdatesFunction(self):
        Getupdater = mainSettings.Updater
        req = urllib2.Request(str(Getupdater)+'/csupdater/LatestVersion.txt')
        fileFolders = urllib2.Request(str(Getupdater)+'/csupdater/Versions/')
        req.add_header('Referer', 'http://www.python.org/')
        resp = urllib2.urlopen(req)
        GetLatest = resp.read()   # Get Web Version / Latest
        reopenLatest = open('Version.py','r+')

        for last in reopenLatest:
            splitLast = last.split(',')
            getFinalLast = splitLast[-1]
        floatLast = float(getFinalLast) # Client Version
        floatWeb = float(GetLatest) # Web Version

        reopenLatest.close()
        if float(floatWeb) > float(floatLast):
            Form.close(),Popen('Updater.exe')
        else:
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText('You are using the Latest Version, Your Client is Up to Date!')
            pass


    def StartGameFunction(self):
        import os as cs
        import time
        from subprocess import Popen
        Getupdater = mainSettings.Updater
        req = urllib2.Request(str(Getupdater)+'/csupdater/LatestVersion.txt')
        fileFolders = urllib2.Request(str(Getupdater)+'/csupdater/Versions/')
        req.add_header('Referer', 'http://www.python.org/')
        resp = urllib2.urlopen(req)
        GetLatest = resp.read()   # Get Web Version / Latest
        reopenLatest = open('Version.py','r+')

        for last in reopenLatest:
            splitLast = last.split(',')
            getFinalLast = splitLast[-1]
        floatLast = float(getFinalLast) # Client Version
        floatWeb = float(GetLatest) # Web Version

        reopenLatest.close()
        if float(floatWeb) > float(floatLast):
            Form.close(),Popen('Updater.exe') # Runs if There is a New Version
        else:
            Form.close(),Popen(str(mainSettings.Start))  # Runs Game if no Latest Version
        #self.comboBox_5.get
        #funcrun = self.CheckforUpdatesFunction
        #funcrun






    def SaveUsernameFunction(self):
        """  Unused Function """
        pass # hahaha lucky you





    def SaveWindowsandSoundsFunction(self):
        import time
        """  RESOLUTION FUNCTION   """
        from subprocess import Popen as run
        getResolutions = self.comboBox_5.currentText()  #Get Resolution
        setWindSlider = self.WindowsOnorFullSlider
        getSounds = self.SoundsOnandOffSlider.value()
        ######## WS START ############
        if "Select Window Size" in str(getResolutions):
            setWindSlider.setValue(0)

            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: Default Selected')
            pass

        if "800x600  Window Screen" in str(getResolutions):
            setWindSlider.setValue(0)
            run('w86.bat', shell=True)  #window 8x6
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 800x600 Window-Mode Selected [PRESS YES]')
        if "1024x768  Window Screen" in str(getResolutions):
            setWindSlider.setValue(0)
            run('w17.bat', shell=True)  #window 1x7
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 1024x768 Window-Mode Selected [PRESS YES]')
        if "1280x1024  Window Screen" in str(getResolutions):
            setWindSlider.setValue(0)
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 1280x1024 Window-Mode Selected [PRESS YES]')
            run('w121.bat', shell=True) #window 121


        ############## FS START #######
        if "800x600  Full Screen" in str(getResolutions):
            setWindSlider.setValue(2)
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 800x600 Full-Screen Mode Selected [PRESS YES]')
            run('f86.bat', shell=True) #window 8x6

        if "1024x768 Full Screen" in str(getResolutions):
            setWindSlider.setValue(2)
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 1024x768 Full-Screen Mode Selected [PRESS YES]')
            run('f17.bat', shell=True) #window 8x6

        if "1280x1024 Full Screen" in str(getResolutions):
            setWindSlider.setValue(2)
            self.NotificationBox.clear(), self.NotificationBox2.clear(),self.NotificationBox2.insertPlainText(str(mainSettings.Server)+' Launcher: 1280x1024 Full-Screen Mode Selected [PRESS YES]')
            run('f121.bat', shell=True) #window 8x6
        ##############################################

        def CheckSoundsNow(object):
            getsSounds = getSounds
            if getsSounds == 1:
                pass # Next Update
            if getsSounds == 2:
                pass # Next Update
            if getsSounds == 0:
                pass # Next Update
        CheckSoundsNow(object)



    def SocialsBarFunction(self):
        file = open('Settings/Buttons/SocialLink.py', 'r+')
        rfile = file.read()
        strfile = eval(str(rfile))
        rightnewsq = self.WebViewNewsEvents
        rightnewsq.setUrl(QtCore.QUrl(_fromUtf8(str(strfile))))
        rightnewsq.setGeometry(QtCore.QRect(190, 70, 500, 251))

    def close(self):
        Form.close()
    def showMinimized(self):
        Form.showMinimized()


from PyQt4 import QtWebKit


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    uiFrame = mainSettings.Frameless
    uiBorder = mainSettings.Borderless
    if uiFrame == 0:
        pass
    if uiFrame == 1:
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    if uiBorder == 0:
        pass
    if uiBorder == 1:
        Form.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

    else:
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

