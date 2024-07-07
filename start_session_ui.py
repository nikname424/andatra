# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_session.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_Start_Session_Window(object):
    def setupUi(self, Start_Session_Window):
        if not Start_Session_Window.objectName():
            Start_Session_Window.setObjectName(u"Start_Session_Window")
        Start_Session_Window.resize(553, 253)
        Start_Session_Window.setStyleSheet(u"background: #2C2D2F;\n"
"")
        self.centralwidget = QWidget(Start_Session_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(300, 200, 171, 31))
        self.buttonBox.setStyleSheet(u"background: white;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.choose_card_box = QComboBox(self.centralwidget)
        self.choose_card_box.setObjectName(u"choose_card_box")
        self.choose_card_box.setGeometry(QRect(280, 130, 264, 50))
        self.choose_card_box.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.50);\n"
"border-radius: 5px;\n"
"font-size: 22px;\n"
"color: white;")
        self.name_bank = QLabel(self.centralwidget)
        self.name_bank.setObjectName(u"name_bank")
        self.name_bank.setGeometry(QRect(10, 130, 264, 50))
        self.name_bank.setStyleSheet(u"width: 264px;\n"
"height: 50px;\n"
"background: rgba(255, 255, 255, 0.75);\n"
"border-radius: 5px;\n"
"")
        self.write_balance_card_btn = QPushButton(self.centralwidget)
        self.write_balance_card_btn.setObjectName(u"write_balance_card_btn")
        self.write_balance_card_btn.setGeometry(QRect(20, 190, 236, 50))
        self.write_balance_card_btn.setStyleSheet(u"width: 236.18px;\n"
"height: 51.29px;\n"
"background: rgba(93, 36, 255, 0.70);\n"
"border-radius: 10px;\n"
"font-size: 48px;\n"
"color: white;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 264, 50))
        self.label.setStyleSheet(u"width: 264px;\n"
"height: 50px;\n"
"background: rgba(255, 255, 255, 0.75);\n"
"border-radius: 5px;\n"
"")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 10, 264, 50))
        font = QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"width: 264px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 70, 264, 50))
        self.label_3.setStyleSheet(u"width: 264px;\n"
"height: 50px;\n"
"background: rgba(255, 255, 255, 0.75);\n"
"border-radius: 5px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 70, 264, 50))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"width: 264px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        Start_Session_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Start_Session_Window)

        QMetaObject.connectSlotsByName(Start_Session_Window)
    # setupUi

    def retranslateUi(self, Start_Session_Window):
        Start_Session_Window.setWindowTitle(QCoreApplication.translate("Start_Session_Window", u"MainWindow", None))
        self.name_bank.setText(QCoreApplication.translate("Start_Session_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">\u0411\u0430\u043d\u043a</span></p></body></html>", None))
        self.write_balance_card_btn.setText(QCoreApplication.translate("Start_Session_Window", u"\u0417\u0410\u041f\u0418\u0421\u042c", None))
        self.label.setText(QCoreApplication.translate("Start_Session_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0439 \u0431\u0430\u043b\u0430\u043d\u0441</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Start_Session_Window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u0411\u0430\u043b\u0430\u043d\u0441 \u043d\u0430 \u043a\u0430\u0440\u0442\u0435</span></p></body></html>", None))
    # retranslateUi
