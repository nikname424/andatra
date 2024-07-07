# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_crypto.ui'
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

class Ui_AddCrypto(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 132)
        MainWindow.setStyleSheet(u"background: #2C2D2F;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.crypto_buy_text = QLabel(self.centralwidget)
        self.crypto_buy_text.setObjectName(u"crypto_buy_text")
        self.crypto_buy_text.setGeometry(QRect(10, 10, 200, 60))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(False)
        self.crypto_buy_text.setFont(font)
        self.crypto_buy_text.setStyleSheet(u"width: 152px; height: 50px; opacity: 0.75; background: white; border-radius: 5px;\n"
"width: 111px;\n"
"height: 44px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 40px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"width: 197px;\n"
"height: 50px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"\n"
"")
        self.crypto_buy_text.setAlignment(Qt.AlignCenter)
        self.name_bank_edit = QLineEdit(self.centralwidget)
        self.name_bank_edit.setObjectName(u"name_bank_edit")
        self.name_bank_edit.setGeometry(QRect(220, 10, 160, 60))
        self.name_bank_edit.setStyleSheet(u"width: 162px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(210, 90, 171, 32))
        self.buttonBox.setStyleSheet(u"background: white;\n"
"color: black;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.crypto_buy_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">\u041a\u0420\u0418\u041f\u0422\u041e\u0412\u0410\u041b\u042e\u0422\u0410</span></p></body></html>", None))
        self.name_bank_edit.setText("")
    # retranslateUi

