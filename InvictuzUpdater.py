# -*- coding: utf-8 -*-



from PyQt4 import QtCore, QtGui
import urllib
import urllib2
import time
import sys
import os
from subprocess import Popen
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(679, 160)
        MainWindow.setStyleSheet(_fromUtf8("background: rgb(93, 93, 93);"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 481, 71))
        self.progressBar.setStyleSheet(_fromUtf8(" QProgressBar {\n"
"     border: 2px solid grey;\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
" }\n"
"\n"
" QProgressBar:chunk {\n"
"     background-color: #05B8CC;\n"
"     width: 20px;\n"
" }"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setFormat(_fromUtf8("%p%         from Mu Int Online"))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.nowUpdating = QtGui.QTextEdit(self.centralwidget)
        self.nowUpdating.setGeometry(QtCore.QRect(10, 120, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.nowUpdating.setFont(font)
        self.nowUpdating.setStyleSheet(_fromUtf8("color: white;background: transparent;border: none;"))
        self.nowUpdating.setObjectName(_fromUtf8("nowUpdating"))
        self.nowUpdating.setDisabled(1)
        self.ionlinename = QtGui.QLabel(self.centralwidget)
        self.ionlinename.setGeometry(QtCore.QRect(10, 10, 241, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.ionlinename.setFont(font)
        self.ionlinename.setStyleSheet(_fromUtf8("\n"
"color: rgb(180, 180, 180);"))
        self.ionlinename.setObjectName(_fromUtf8("ionlinename"))
        self.nowUpdating_2 = QtGui.QLabel(self.centralwidget)
        self.nowUpdating_2.setGeometry(QtCore.QRect(560, 120, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.nowUpdating_2.setFont(font)
        self.nowUpdating_2.setStyleSheet(_fromUtf8("color: rgb(130, 130, 130);"))
        self.nowUpdating_2.setObjectName(_fromUtf8("nowUpdating_2"))
        self.minimizeme = QtGui.QPushButton(MainWindow)
        self.minimizeme.setGeometry(QtCore.QRect(630, 0, 25, 29))
        self.minimizeme.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.minimizeme.setStyleSheet(_fromUtf8("\n"
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
        self.minimizeme.setText(_fromUtf8(""))
        self.minimizeme.setObjectName(_fromUtf8("minimizeme"))

        self.ionlinename_2 = QtGui.QLabel(self.centralwidget)
        self.ionlinename_2.setGeometry(QtCore.QRect(120, 10, 241, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.ionlinename_2.setFont(font)
        self.ionlinename_2.setStyleSheet(_fromUtf8("background: none;\n"
"color:rgb(255, 210, 46);"))
        self.ionlinename_2.setObjectName(_fromUtf8("ionlinename_2"))
        self.INFORMATION = QtGui.QLabel(self.centralwidget)
        self.INFORMATION.setGeometry(QtCore.QRect(220, 120, 311, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.INFORMATION.setFont(font)
        self.INFORMATION.setStyleSheet(_fromUtf8("background: none;\n"
"color:rgb(130, 130, 130);"))
        self.INFORMATION.setObjectName(_fromUtf8("INFORMATION"))
        self.StartUpdate = QtGui.QPushButton(self.centralwidget)
        self.StartUpdate.setGeometry(QtCore.QRect(500, 40, 171, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.StartUpdate.setFont(font)
        self.StartUpdate.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.StartUpdate.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #3498db;\n"
"  border-radius: 28px;\n"
"  font-family: Arial;\n"
"  color: #ffffff;\n"
"  font-size: 20px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background: #3cb0fd;\n"
"  text-decoration: none;\n"
"}"))
        self.StartUpdate.setObjectName(_fromUtf8("StartUpdate"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.StartUpdate, QtCore.SIGNAL(_fromUtf8("clicked()")), self.startupdateTrigger)
        QtCore.QObject.connect(self.minimizeme, QtCore.SIGNAL(_fromUtf8("clicked()")), self.minimizemet)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Invictuz Online Updater", None))
        self.nowUpdating.setText(_translate("MainWindow", "Please Click the \"Update Now\"", None))
        self.ionlinename.setText(_translate("MainWindow", "      Mu Int", None))
        self.nowUpdating_2.setText(_translate("MainWindow", "Copyright (c) Sheily 2014", None))
        self.ionlinename_2.setText(_translate("MainWindow", "Online", None))
        self.INFORMATION.setText(_translate("MainWindow", "More Update Information? visit:  http://sheily.com/", None))
        self.StartUpdate.setText(_translate("MainWindow", "UPDATE NOW", None))



    def startupdateTrigger(self):
        """
        main updater function
        """

        # IMPORTANT VARIABLES START
        from Settings import mainSettings
        iProgress = self.progressBar
        nowUpdating = self.nowUpdating
        nowUpdating.clear(),nowUpdating.insertHtml('<b><font color=\'orange\'>Now Updating, Do not Interrupt!</font></b>')
        version = open('Settings/Version.py', 'r+')
        updater = open('Settings/Updater.py', 'r+')
        rversion = version.read()         # Get Client Version
        Getupdater = updater.read()    # Get Updater URL
        req = urllib2.Request(str(Getupdater)+'/csupdater/LatestVersion.txt')
        fileFolders = urllib2.Request(str(Getupdater)+'/csupdater/Versions/')
        req.add_header('Referer', 'http://www.python.org/')
        resp = urllib2.urlopen(req)
        GetLatest = resp.read()   # Get Web Version / Latest
        Getversion = eval(str(rversion))
        evalVersion = eval(str(rversion))
        evalLatest = eval(str(GetLatest))
        msgBox = QtGui.QMessageBox()
        msgBox.setText('Finished Updating! Start Game Now!')
        msgBox.setWindowTitle('Invictuz Online Updater')
        toStart2 = mainSettings.Start
        openvers = open('Version.py','r+')  # Open Version File NEW
        for version in openvers:
            x = version.split(',')
            getLast = x[-1]
            floatLast = float(getLast)
        # IMPORTANLE VARIABLES END
        decVersion = float(floatLast) + 0.1

        if float(evalLatest) > float(floatLast):
            pass
        else:
            MainWindow.close(),Popen(str(toStart2)),Popen('run.bat', shell=True)
            return 0 # <-- not needed LOL
        openvers.close()

        webFolder = str(Getupdater)+'csupdater/Versions/'+str(decVersion)+'/'+str(decVersion)+'.zip'
        url = webFolder
        file_name = url.split('/')[-1]
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])


        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%3.2f % % " % (file_size_dl * 100. / file_size) #Lets do Squaroootinssss
            #statuss = status + chr(8)*(len(status)+1)
            x=status.replace('%','')
            floatingX = float(x)
            iProgress.setValue(float(floatingX))

        if iProgress.value() == 100:
            nowUpdating.clear(),nowUpdating.insertHtml('<b><font color=\'orange\'>Finished Updating to version {v}</font></b>'.format(v=decVersion))
        openVerfile = open('Version.py','r+')
        w = open('Version.py','a')

        for version in openVerfile:
            x = version.split(',')

        w.write(','+ str(decVersion))
        w.close()
        f.close()
        ## MAKE FILE FOR UNZIPPER MARK :)
        reopenLatest = open('Version.py','r+')
        for last in reopenLatest:
            splitLast = last.split(',')
            getFinalLast = splitLast[-1]
        verzip = open('verzip.py','w')
        verzip.write(str(getFinalLast))
        reopenLatest.close()
        self.StartUpdate.setText('Start Game')
        letStart = mainSettings.Start
        MainWindow.close(),Popen(str(letStart)),Popen('run.bat', shell=True)



    def minimizemet(self):
        MainWindow.showMinimized()
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

