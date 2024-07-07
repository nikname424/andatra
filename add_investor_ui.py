# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_investor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QWidget)

class Ui_AddInvestor(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(373, 229)
        MainWindow.setStyleSheet(u"background: #2C2D2F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 152, 50))
        self.label_2.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 152, 50))
        self.label.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 10, 196, 50))
        self.lineEdit_2.setStyleSheet(u"width: 196px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-size: 18px;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 70, 196, 50))
        self.lineEdit.setStyleSheet(u"width: 196px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-size: 18px;")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 190, 171, 31))
        self.buttonBox.setStyleSheet(u"background: white;\n"
"color: black;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 130, 152, 50))
        self.label_3.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 130, 196, 50))
        self.lineEdit_3.setStyleSheet(u"width: 196px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font-size: 18px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">\u0421\u0443\u043c\u043c\u0430</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">\u0424\u0418\u041e</span></p></body></html>", None))
        self.lineEdit_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">\u0414\u043e\u0445\u043e\u0434 %</span></p></body></html>", None))
    # retranslateUi

