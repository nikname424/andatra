# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_card.ui'
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

class Ui_Add_card(object):
    def setupUi(self, Add_card):
        if not Add_card.objectName():
            Add_card.setObjectName(u"Add_card")
        Add_card.resize(384, 187)
        Add_card.setStyleSheet(u"width: 372px;\n"
"height: 152px;\n"
"background: #2C2D2F;\n"
"")
        self.centralwidget = QWidget(Add_card)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(200, 150, 171, 32))
        self.buttonBox.setStyleSheet(u"background: white;\n"
"color: black;")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.crypto_buy_text = QLabel(self.centralwidget)
        self.crypto_buy_text.setObjectName(u"crypto_buy_text")
        self.crypto_buy_text.setGeometry(QRect(10, 10, 152, 60))
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
"")
        self.crypto_buy_text.setAlignment(Qt.AlignCenter)
        self.name_bank_edit = QLineEdit(self.centralwidget)
        self.name_bank_edit.setObjectName(u"name_bank_edit")
        self.name_bank_edit.setGeometry(QRect(170, 10, 200, 60))
        self.name_bank_edit.setStyleSheet(u"width: 196px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"")
        self.crypto_buy_text_2 = QLabel(self.centralwidget)
        self.crypto_buy_text_2.setObjectName(u"crypto_buy_text_2")
        self.crypto_buy_text_2.setGeometry(QRect(10, 80, 152, 60))
        self.crypto_buy_text_2.setFont(font)
        self.crypto_buy_text_2.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"width: 111px;\n"
"height: 44px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.crypto_buy_text_2.setAlignment(Qt.AlignCenter)
        self.number_card_edit = QLineEdit(self.centralwidget)
        self.number_card_edit.setObjectName(u"number_card_edit")
        self.number_card_edit.setGeometry(QRect(170, 80, 200, 60))
        self.number_card_edit.setStyleSheet(u"width: 196px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"color: black;")
        Add_card.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_card)

        QMetaObject.connectSlotsByName(Add_card)
    # setupUi

    def retranslateUi(self, Add_card):
        Add_card.setWindowTitle(QCoreApplication.translate("Add_card", u"MainWindow", None))
        self.crypto_buy_text.setText(QCoreApplication.translate("Add_card", u"<html><head/><body><p>\u0411\u0410\u041d\u041a</p></body></html>", None))
        self.crypto_buy_text_2.setText(QCoreApplication.translate("Add_card", u"<html><head/><body><p>\u041d\u041e\u041c\u0415\u0420</p></body></html>", None))
    # retranslateUi

