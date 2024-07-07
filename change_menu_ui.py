# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_ChangeMenu(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 189)
        MainWindow.setStyleSheet(u"background: #2C2D2F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 40, 168, 50))
        self.lineEdit.setStyleSheet(u"width: 168px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 130, 152, 50))
        self.pushButton.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"background: rgba(255, 244.80, 0, 0.75);\n"
"border-radius: 10px;\n"
"width: 122px;\n"
"height: 44px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 36px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.to_crypto = QComboBox(self.centralwidget)
        self.to_crypto.setObjectName(u"to_crypto")
        self.to_crypto.setGeometry(QRect(10, 70, 150, 50))
        self.to_crypto.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.from_crypto = QComboBox(self.centralwidget)
        self.from_crypto.setObjectName(u"from_crypto")
        self.from_crypto.setGeometry(QRect(10, 10, 150, 50))
        self.from_crypto.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 130, 168, 50))
        self.label.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"width: 141px;\n"
"height: 44px;\n"
"text-align: center;\n"
"color: rgba(3.19, 3.19, 3.19, 0.25);\n"
"font-size: 36px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"color: black\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041c\u0415\u041d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">STATUS</p></body></html>", None))
    # retranslateUi

