# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import threading

import res_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog, QMainWindow, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal
import time
from pysondb import db


class MyThread(QThread):
    def __init__(self, sleep):
        super().__init__()
        self.sleepBar = sleep
        self.exit_event = threading.Event()

    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 1000:
            cnt += 1
            time.sleep(self.sleepBar)
            self.change_value.emit(cnt)
            if self.exit_event.is_set():
                break

    def stop(self):
        self.exit_event.set()


class Ui_Dialog(QDialog):
    @staticmethod
    def getItems():
        a = db.getDb("db_config.json")
        items = [i["name"] for i in a.getByQuery({"type": "unit"})]
        return items

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(587, 407)
        Dialog.setMinimumSize(QtCore.QSize(587, 407))
        Dialog.setMaximumSize(QtCore.QSize(587, 407))
        Dialog.setStyleSheet("#centralwidget {\n"
                             "    background-color: rgb(240,255,255);\n"
                             "}")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 587, 407))
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 340, 120, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 21px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(155, 340, 120, 46))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 21px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 551, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QScrollBar:vertical {\n"
                                      "    background: white;\n"
                                      "    width: 12px;               \n"
                                      "    margin: 0px 0px 0px 0px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    background: rgb(1, 74, 88);\n"
                                      "    min-height: 0px;\n"
                                      "}\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "    background: rgb(1, 74, 88);\n"
                                      "    height: 0px;\n"
                                      "    subcontrol-position: bottom;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "    background: rgb(1, 74, 88);\n"
                                      "    height: 0 px;\n"
                                      "    subcontrol-position: top;\n"
                                      "    subcontrol-origin: margin;\n"
                                      "}\n"
                                      "QListWidget::item:selected {\n"
                                      "    background: #cce7ff;\n"
                                      "    color: black;\n"
                                      "}")
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.addItems(self.getItems())
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(312, 290, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setHidden(True)
        self.pushButton_6.setGeometry(QtCore.QRect(406, 290, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setHidden(True)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 290, 35, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}\n"
                                        "QPushButton:disabled {\n"
                                        "background-color: rgba(1, 74, 88, 150);\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setHidden(True)
        self.pushButton_8.setGeometry(QtCore.QRect(536, 290, 35, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 10px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}\n"
                                        "QPushButton:disabled {\n"
                                        "background-color: rgba(1, 74, 88, 150);\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background: transparent;\n"
                                 "font: 75 12pt \"Arial\";\n"
                                 "color: rgb(0, 59, 70);")
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 290, 285, 30))
        self.lineEdit.setStyleSheet("border-style: outset;\n"
                                    "border-width: 2px;\n"
                                    "border-radius: 8px;\n"
                                    "border-color: rgb(0, 0, 0);\n"
                                    "background: transparent;\n"
                                    "font-size: 18px;")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.checkActions()
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Обновление конфигурации"))
        self.label.setText(_translate("Dialog", "Данные отображаются по следующим персонажам:"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "APIИмя:ПользовательскоеИмя"))
        self.pushButton_5.setText(_translate("Dialog", "Добавить"))
        self.pushButton_6.setText(_translate("Dialog", "Удалить"))
        self.pushButton_7.setText(_translate("Dialog", "▲"))
        self.pushButton_8.setText(_translate("Dialog", "▼"))
        self.pushButton_3.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_4.setText(_translate("Dialog", "Отмена"))

    def checkActions(self):
        self.pushButton_3.clicked.connect(self.saveConfig)
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.addItemInList)
        self.pushButton_6.clicked.connect(self.removeItemFromList)
        self.pushButton_7.clicked.connect(self.changeRowSelectItemUp)
        self.pushButton_8.clicked.connect(self.changeRowSelectItemDown)
        self.lineEdit.textChanged.connect(self.removeSelectList)
        self.listWidget.currentRowChanged.connect(self.setVisibleMenuButtons)

    def saveConfig(self):
        a = db.getDb("db_config.json")
        a.deleteAll()

        items = []
        for i in range(self.listWidget.count()):
            items.append({"name": self.listWidget.item(i).text(), "type": "unit"})

        a.addMany(items)
        self.close()

    def removeSelectList(self):
        self.listWidget.setCurrentRow(-1)

    def addItemInList(self):
        item = self.lineEdit.text()
        if item:
            self.listWidget.addItem(item)
            self.listWidget.scrollToItem(self.listWidget.item(self.listWidget.count() - 1))
            self.lineEdit.setText('')
        self.removeSelectList()

    def setHiddenMenuButtons(self, flag: bool):
        self.pushButton_6.setHidden(flag)
        self.pushButton_7.setHidden(flag)
        self.pushButton_8.setHidden(flag)
        if not flag:
            self.pushButton_7.setDisabled(False)
            self.pushButton_8.setDisabled(False)

    def setVisibleMenuButtons(self):
        row = self.listWidget.currentRow()
        if row != -1:
            self.setHiddenMenuButtons(False)
            if row == 0:
                self.pushButton_7.setDisabled(True)
            if row == self.listWidget.count() - 1:
                self.pushButton_8.setDisabled(True)
        else:
            self.setHiddenMenuButtons(True)

    def removeItemFromList(self):
        item = self.listWidget.currentRow()
        if item != -1:
            self.listWidget.takeItem(item)
            self.removeSelectList()

    def changeRowSelectItemUp(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.currentItem()
        self.listWidget.takeItem(row)
        self.listWidget.insertItem(row - 1, item)
        self.listWidget.setCurrentRow(row - 1)

    def changeRowSelectItemDown(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.currentItem()
        self.listWidget.takeItem(row)
        self.listWidget.insertItem(row + 1, item)
        self.listWidget.setCurrentRow(row + 1)


class PopupException(QDialog):
    def __init__(self, labelText, error=True, id=None):
        super().__init__()
        self.flagError = error
        self.text = labelText
        self.id = id

    def setupUi(self, Form):
        Form.setObjectName("Error")
        Form.resize(430, 140)
        Form.setStyleSheet("background-color: rgb(240,255,255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(275, 90, 130, 30))
        self.pushButton.setStyleSheet("background: autoFill;\n"
                                      "background-color: rgb(1, 74, 88);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"Arial\";\n"
                                      "border-style: outset;\n"
                                      "border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 391, 41))
        self.label.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                 "background: transparent;\n"
                                 "color: rgb(1, 74, 88);")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        if self.flagError:
            Form.setWindowTitle(_translate("Form", "Ошибка"))
        else:
            Form.setWindowTitle(_translate("Form", "Успешно"))
        self.pushButton.setText(_translate("Form", "Принято"))
        if self.id:
            self.label.setText(_translate("Form", self.text + self.id))
        else:
            self.label.setText(_translate("Form", self.text))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton.clicked.connect(self.close)


class Ui_MainWindow(QMainWindow):
    class MyLineEdit(QLineEdit):
        def __init__(self, parent=None):
            QLineEdit.__init__(self, parent=parent)
            self.setPlaceholderText('000-000-000')
            self.setMaxLength(11)

        def setCursorPos(self):
            count = 0
            for i in self.displayText()[::-1]:
                if i in '123456789':
                    break
                count += 1

            if count == 4 or count == 8:
                count -= 1

            if count:
                self.setCursorPosition(len(self.displayText()) - count)
            else:
                self.setCursorPosition(0)

        def focusInEvent(self, event):
            if self.text() == "":
                self.setInputMask('999-999-999')
                self.setText('000-000-000')
            self.setCursorPos()

        def focusOutEvent(self, event):
            if self.text().replace('0', '') == "--":
                self.setInputMask('')
                self.setText('')

        def mousePressEvent(self, event):
            self.setCursorPos()

    def setupUi(self, MainWindow):
        a = db.getDb("db_url.json")

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 500)
        MainWindow.setMinimumSize(QtCore.QSize(685, 500))
        MainWindow.setMaximumSize(QtCore.QSize(685, 500))
        MainWindow.setStyleSheet("#centralwidget {\n"
                                 "    background-image: url(:/resources/image/background.png);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 305, 130, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "background: autoFill;\n"
                                      "background-color: rgb(1, 74, 88);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 18px;\n"
                                      "}\n"
                                      "QPushButton::pressed {\n"
                                      "    background-color: rgb(97, 164, 173);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 305, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 18px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 305, 150, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 18px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 159, 88, 33))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "background: autoFill;\n"
                                        "background-color: rgb(1, 74, 88);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 9px;\n"
                                        "}\n"
                                        "QPushButton::pressed {\n"
                                        "    background-color: rgb(97, 164, 173);\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")

        self.lineEdit = self.MyLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(355, 111, 300, 30))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setStyleSheet("QLineEdit {    \n"
                                    "    border-style: outset;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 8px;\n"
                                    "    border-color: rgb(0, 0, 0);\n"
                                    "    background: transparent;\n"
                                    "    font-size: 20px;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(235, 113, 101, 23))
        self.label.setStyleSheet("background: transparent;\n"
                                 "font: 75 12pt \"Arial\";\n"
                                 "color: rgb(0, 59, 70);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(235, 208, 101, 23))
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 59, 70);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(422, 208, 131, 24))
        self.label_3.setStyleSheet("QLabel {\n"
                                   "background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 59, 70);\n"
                                   "}\n"
                                   "QToolTip {\n"
                                   "background-color: rgb(248,253,253);\n"
                                   "color: #003b46;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(235, 252, 111, 23))
        self.label_4.setStyleSheet("font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 61, 74);\n"
                                   "background: transparent;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(275, 20, 381, 41))
        self.label_5.setStyleSheet("font: 75 26pt \"Arial\";\n"
                                   "color: rgb(235, 242, 244);\n"
                                   "background:transparent;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(235, 163, 101, 23))
        self.label_6.setStyleSheet("background: transparent;\n"
                                   "font: 75 12pt \"Arial\";\n"
                                   "color: rgb(0, 59, 70);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(355, 250, 300, 30))
        self.lineEdit_2.setStyleSheet("border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 8px;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "background: transparent;\n"
                                      "font-size: 20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(355, 160, 211, 30))
        self.lineEdit_3.setStyleSheet("border-style: outset;\n"
                                      "border-width: 2px;\n"
                                      "border-radius: 8px;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "background: transparent;\n"
                                      "font-size: 20px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText(a.getByQuery({"name": "api"})[0]["url"])
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(355, 195, 57, 50))
        self.checkBox.setStyleSheet("QCheckBox::indicator {\n"
                                    "    width: 50px;\n"
                                    "    height: 50px;\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator::checked {\n"
                                    "    image: url(:/resources/image/switch-on.png);\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox::indicator::unchecked {\n"
                                    "    image: url(:/resources/image/switch-off.png);\n"
                                    "}")
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(610, 430, 57, 51))
        self.checkBox_2.setStyleSheet("QCheckBox::indicator {\n"
                                      "    width: 50px;\n"
                                      "    height: 50px;\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator::checked {\n"
                                      "    \n"
                                      "    image: url(:/resources/image/robot2.png);\n"
                                      "}\n"
                                      "\n"
                                      "QCheckBox::indicator::unchecked {\n"
                                      "    image: url(:/resources/image/robot.png);\n"
                                      "}")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.checkActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setTabOrder(self.pushButton, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.checkBox_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GH"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))
        self.pushButton_2.setText(_translate("MainWindow", "Сохранить как..."))
        self.pushButton_3.setText(_translate("MainWindow", "Конфигурация"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Код игрока"))
        self.label_2.setText(_translate("MainWindow", "Один игрок"))
        self.label_3.setToolTip(_translate("MainWindow",
                                           "<span style=\'font-size: 13px;\'>Переключатель в режиме \"Вся гильдия\" предоставляет информацию о всех участниках гильдии, в которой состоит игрок.</span>"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p>Вся гильдия <span style=\" vertical-align:super;\">ⓘ</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Директория"))
        self.label_5.setText(_translate("MainWindow", "Игровой ассистент"))
        self.label_6.setText(_translate("MainWindow", "Адрес API"))
        self.lineEdit_2.setText(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop').replace('\\', '/'))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "http://"))

    def checkActions(self):
        self.pushButton_2.clicked.connect(self.changeDirectory)
        self.pushButton_3.clicked.connect(self.updateConfig)
        self.pushButton_4.clicked.connect(self.saveUrlAPItoConfig)
        # self.connect(self.progressBar.value==100, self.show_popup_success)

    def changeDirectory(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        fname = dialog.getExistingDirectory(self, 'Выбор директории для сохранения',
                                            os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        if fname:
            self.lineEdit_2.setText(fname)

    def saveUrlAPItoConfig(self):
        a = db.getDb("db_url.json")
        url = self.lineEdit_3.text()
        if not url == "" and url[-1] != '/':
            url += '/'
        a.updateByQuery({"name": "api"}, {"url": url})

    def updateConfig(self):
        dialog = Ui_Dialog()
        dialog.setupUi(dialog)
        dialog.exec_()

    def changeValueOfRobot(self):
        self.checkBox_2.setChecked(not self.checkBox_2.isChecked())

    def show_popup(self):
        msg = PopupException("Не удалось найти игрока с кодом: ", id=self.lineEdit.text())
        msg.setupUi(msg)
        msg.exec_()

    def show_popup_ex(self):
        msg = PopupException("Произошла непредвиденная ошибка")
        msg.setupUi(msg)
        msg.exec_()

    def show_popup_success(self):
        msg = PopupException("Статистика была успешно получена", False)
        msg.setupUi(msg)
        msg.exec_()


if __name__ == "__main__":
    import sys
    import ctypes

    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('ico.ico'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
