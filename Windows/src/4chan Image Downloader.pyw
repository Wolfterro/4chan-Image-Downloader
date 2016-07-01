# -*- coding: utf-8 -*-

'''
The MIT License (MIT)

Copyright (c) 2016 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#===================================
# Criado por: Wolfterro
# Versão: 1.0 - Python 2.x - Windows
# Data: 26/06/2016
#===================================

from PyQt4 import QtCore, QtGui
from os.path import expanduser

import os
import sys
import json
import urllib2
import subprocess

version = "1.0"
home_dir = expanduser("~")

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
        MainWindow.resize(460, 480)
        MainWindow.setMaximumSize(QtCore.QSize(460, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.clicked.connect(self.selectOutputDir)
        self.gridLayout.addWidget(self.toolButton, 2, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.getUserValues)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 3)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "4chan Image Downloader - v%s" % (version), None))
        self.label_2.setText(_translate("MainWindow", "Board do Tópico Escolhido:", None))
        self.comboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Escolha uma board</p></body></html>", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "/3/ - 3DCG", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "/a/ - Anime & Manga", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "/aco/ - Adult Cartoons", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "/adv/ - Advice", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "/an/ - Animals & Nature", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "/asp/ - Alternative Sports", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "/b/ - Random", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "/biz/ - Business & Finance", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "/c/ - Anime/Cute", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "/cgl/ - Cosplay & EGL", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "/ck/ - Food & Cooking", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "/cm/ - Cute/Male", None))
        self.comboBox.setItemText(12, _translate("MainWindow", "/co/ - Comics & Cartoons", None))
        self.comboBox.setItemText(13, _translate("MainWindow", "/d/ - Hentai/Alternative", None))
        self.comboBox.setItemText(14, _translate("MainWindow", "/diy/ - Do It Yourself", None))
        self.comboBox.setItemText(15, _translate("MainWindow", "/e/ - Ecchi", None))
        self.comboBox.setItemText(16, _translate("MainWindow", "/f/ - Flash", None))
        self.comboBox.setItemText(17, _translate("MainWindow", "/fa/ - Fashion", None))
        self.comboBox.setItemText(18, _translate("MainWindow", "/fit/ - Fitness", None))
        self.comboBox.setItemText(19, _translate("MainWindow", "/g/ - Technology", None))
        self.comboBox.setItemText(20, _translate("MainWindow", "/gd/ - Graphic Design", None))
        self.comboBox.setItemText(21, _translate("MainWindow", "/gif/ - Adult GIF", None))
        self.comboBox.setItemText(22, _translate("MainWindow", "/h/ - Hentai", None))
        self.comboBox.setItemText(23, _translate("MainWindow", "/hc/ - Hardcore", None))
        self.comboBox.setItemText(24, _translate("MainWindow", "/his/ - History & Humanities", None))
        self.comboBox.setItemText(25, _translate("MainWindow", "/hm/ - Handsome Men", None))
        self.comboBox.setItemText(26, _translate("MainWindow", "/hr/ - High Resolution", None))
        self.comboBox.setItemText(27, _translate("MainWindow", "/i/ - Oekaki", None))
        self.comboBox.setItemText(28, _translate("MainWindow", "/ic/ - Artwork/Critique", None))
        self.comboBox.setItemText(29, _translate("MainWindow", "/int/ - International", None))
        self.comboBox.setItemText(30, _translate("MainWindow", "/jp/ - Otaku Culture", None))
        self.comboBox.setItemText(31, _translate("MainWindow", "/k/ - Weapons", None))
        self.comboBox.setItemText(32, _translate("MainWindow", "/lgbt/ - LGBT", None))
        self.comboBox.setItemText(33, _translate("MainWindow", "/lit/ - Literature", None))
        self.comboBox.setItemText(34, _translate("MainWindow", "/m/ - Mecha", None))
        self.comboBox.setItemText(35, _translate("MainWindow", "/mlp/ - Pony", None))
        self.comboBox.setItemText(36, _translate("MainWindow", "/mu/ - Music", None))
        self.comboBox.setItemText(37, _translate("MainWindow", "/n/ - Transportation", None))
        self.comboBox.setItemText(38, _translate("MainWindow", "/news/ - Current News", None))
        self.comboBox.setItemText(39, _translate("MainWindow", "/o/ - Auto", None))
        self.comboBox.setItemText(40, _translate("MainWindow", "/out/ - Outdoors", None))
        self.comboBox.setItemText(41, _translate("MainWindow", "/p/ - Photo", None))
        self.comboBox.setItemText(42, _translate("MainWindow", "/po/ - Papercraft & Origami", None))
        self.comboBox.setItemText(43, _translate("MainWindow", "/pol/ - Politically Incorrect", None))
        self.comboBox.setItemText(44, _translate("MainWindow", "/qst/ - Quests", None))
        self.comboBox.setItemText(45, _translate("MainWindow", "/r/ - Adult Requests", None))
        self.comboBox.setItemText(46, _translate("MainWindow", "/r9k/ - ROBOT9001", None))
        self.comboBox.setItemText(47, _translate("MainWindow", "/s/ - Sexy Beautiful Women", None))
        self.comboBox.setItemText(48, _translate("MainWindow", "/s4s/ - Shit 4chan Says", None))
        self.comboBox.setItemText(49, _translate("MainWindow", "/sci/ - Science & Math", None))
        self.comboBox.setItemText(50, _translate("MainWindow", "/soc/ - Cams & Meetups", None))
        self.comboBox.setItemText(51, _translate("MainWindow", "/sp/ - Sports", None))
        self.comboBox.setItemText(52, _translate("MainWindow", "/t/ - Torrents", None))
        self.comboBox.setItemText(53, _translate("MainWindow", "/tg/ - Traditional Games", None))
        self.comboBox.setItemText(54, _translate("MainWindow", "/toy/ - Toys", None))
        self.comboBox.setItemText(55, _translate("MainWindow", "/trash/ - Off-Topic", None))
        self.comboBox.setItemText(56, _translate("MainWindow", "/trv/ - Travel", None))
        self.comboBox.setItemText(57, _translate("MainWindow", "/tv/ - Television & Film", None))
        self.comboBox.setItemText(58, _translate("MainWindow", "/u/ - Yuri", None))
        self.comboBox.setItemText(59, _translate("MainWindow", "/v/ - Video Games", None))
        self.comboBox.setItemText(60, _translate("MainWindow", "/vg/ - Video Game Generals", None))
        self.comboBox.setItemText(61, _translate("MainWindow", "/vp/ - Pokémon", None))
        self.comboBox.setItemText(62, _translate("MainWindow", "/vr/ - Retro Games", None))
        self.comboBox.setItemText(63, _translate("MainWindow", "/w/ - Anime/Wallpapers", None))
        self.comboBox.setItemText(64, _translate("MainWindow", "/wg/ - Wallpapers/General", None))
        self.comboBox.setItemText(65, _translate("MainWindow", "/wsr/ - Worksafe Requests", None))
        self.comboBox.setItemText(66, _translate("MainWindow", "/x/ - Paranormal", None))
        self.comboBox.setItemText(67, _translate("MainWindow", "/y/ - Yaoi", None))
        self.label.setText(_translate("MainWindow", "Insira a ID do Tópico:", None))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Insira APENAS a ID do tópico</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "Pasta de Destino:", None))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>Selecione a pasta de destino das imagens</p></body></html>", None))
        self.lineEdit_2.setText(_translate("MainWindow", "%s\\4chan" % (home_dir), None))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Selecionar pasta...</p></body></html>", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Iniciar o download das imagens</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))

    #==========================================================================
    # Métodos de Download: Procedimento de Download das Imagens
    #==========================================================================

    def selectOutputDir(self):
        self.chosenDir = QtGui.QFileDialog.getExistingDirectory(MainWindow, 'Selecione a pasta de destino:', home_dir, QtGui.QFileDialog.ShowDirsOnly)
        self.lineEdit_2.setText(self.chosenDir.replace("/", "\\"))
        return

    def checkOutputDir(self, getOutputDir):
        if os.path.exists(str(self.getOutputDir)):
            os.chdir(str(self.getOutputDir))
        else:
            os.makedirs(str(self.getOutputDir))
            os.chdir(str(self.getOutputDir))
        return

    def getJson(self, url):
        try:
            self.response = urllib2.urlopen(self.url)
            self.data = json.loads(self.response.read())
        except Exception:
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar .json para %s!" % (self.url))
            return {}
        return self.data

    def downloadWithoutProgress(self, imageUrl, filename):
        self.imageResponse = urllib2.urlopen(self.imageUrl)
        with open(str(self.filename), 'wb') as self.file:
            while True:
                self.imageData = self.imageResponse.read()
                if not self.imageData:
                    break
                self.file.write(self.imageData)

    def getPosts(self, getBoardValue, getThreadNumber):
        self.url = "https://a.4cdn.org/%s/thread/%s.json" % (self.getBoardValue, self.getThreadNumber)
        self.data = self.getJson(self.url)
        try:
            return self.data['posts']
        except:
            self.textEdit.append(u"[Downloader] ERRO! Erro ao recuperar posts do tópico %s em /%s/!" % (self.getThreadNumber, self.getBoardValue))
            QtGui.QApplication.processEvents()
            return []

    def getImagesFromPosts(self, posts):
        return ['%s%s' % (self.p['tim'], self.p['ext']) for self.p in self.posts if 'tim' in self.p and 'ext' in self.p]

    def downloadImage(self, getBoardValue, image):
        self.imageUrl = "http://i.4cdn.org/%s/%s" % (self.getBoardValue, str(self.image))
        self.filename = os.path.join(str(self.image))
        self.downloadWithoutProgress(self.imageUrl, self.filename)

    def processThread(self, getBoardValue, getThreadNumber):
        self.textEdit.append(u"[Downloader] Fazendo download em /%s/ do tópico %s" % (self.getBoardValue, self.getThreadNumber))
        QtGui.QApplication.processEvents()

        self.posts = self.getPosts(self.getBoardValue, self.getThreadNumber)
        self.images = self.getImagesFromPosts(self.posts)

        self.textEdit.append(u"[Downloader] Encontrada %d imagens em %d posts" % (len(self.images), len(self.posts)))
        self.textEdit.append("\n=================================================\n")
        QtGui.QApplication.processEvents()

        self.downloaded = 0

        for self.image in self.images:
            self.checkImagesInDir = os.path.isfile(str(self.image))
            if self.checkImagesInDir == True:
                self.downloaded += 1
                self.textEdit.append(u"Imagem '%s' %d/%d em /%s/ do tópico %s já existe! Pulando ..." % (
                    str(self.image), self.downloaded, len(self.images), self.getBoardValue, self.getThreadNumber))
                QtGui.QApplication.processEvents()
            else:
                self.downloaded += 1
                self.textEdit.append(u"Baixando %s - Imagem %d/%d em /%s/ do tópico %s ..." % (
                    str(self.image), self.downloaded, len(self.images), self.getBoardValue, self.getThreadNumber))
                QtGui.QApplication.processEvents()
                self.downloadImage(self.getBoardValue, self.image)
        return

    def getUserValues(self):
        self.getBoardValue = str(self.comboBox.currentText()).split(" - ", 1)[0].replace("/", "")
        self.getThreadNumber = str(self.lineEdit.text())
        self.getOutputDir = str(self.lineEdit_2.text())

        if self.getThreadNumber == "":
            self.textEdit.append(u"[Downloader] Erro! Falta a ID do Tópico!!")
            return
        elif self.getOutputDir == "":
            self.textEdit.append(u"[Downloader] Erro! Falta o caminho para a pasta de destino!!")
            return
        else:
            self.pushButton.setEnabled(False)
            self.pushButton.setText(_translate("MainWindow", "Downloading...", None))
            self.pushButton.repaint()
            QtGui.QApplication.processEvents()

            self.checkOutputDir(self.getOutputDir)

            self.textEdit.clear()
            self.textEdit.append(u"[Downloader] Iniciando Download das Imagens ...")
            QtGui.QApplication.processEvents()

            self.processThread(self.getBoardValue, self.getThreadNumber)

            self.pushButton.setEnabled(True)
            self.pushButton.setText(_translate("MainWindow", "Download", None))
            self.pushButton.repaint()
            QtGui.QApplication.processEvents()

            self.textEdit.append(u"[Downloader] Concluído!!")
            QtGui.QApplication.processEvents()

            subprocess.Popen("explorer %s" % (self.getOutputDir))

            return

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

