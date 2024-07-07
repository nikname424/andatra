# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login_Form(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(272, 212)
        MainWindow.setStyleSheet(u"background: #2C2D2F")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 160, 115, 41))
        self.pushButton.setStyleSheet(u"width: 229px;\n"
"  height: 69px;\n"
"  background: #DF00F2;\n"
"  border-radius: 10px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"color: white;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 80, 192, 30))
        self.lineEdit.setStyleSheet(u"  width: 387px;\n"
"  height: 61px;\n"
"  position: relative;\n"
"  background: white;\n"
"  border-radius: 10px;\n"
"color: black;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(40, 40, 192, 30))
        self.lineEdit_2.setStyleSheet(u"  width: 387px;\n"
"  height: 61px;\n"
"  position: relative;\n"
"  background: white;\n"
"  border-radius: 10px;\n"
"color: black;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(42, 46, 67, 17))
        self.label.setStyleSheet(u"background: white;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(42, 84, 67, 20))
        self.label_2.setStyleSheet(u"background: white;")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(40, 120, 192, 30))
        self.lineEdit_3.setStyleSheet(u"  width: 387px;\n"
"  height: 61px;\n"
"  position: relative;\n"
"  background: white;\n"
"  border-radius: 10px;\n"
"color: black;\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(42, 126, 51, 20))
        self.label_3.setStyleSheet(u"background: white;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 10, 151, 25))
        self.label_4.setStyleSheet(u"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">\u0410\u0412\u0422\u041e\u0420\u0418\u0417\u0410\u0426\u0418\u042f</span></p></body></html>", None))
    # retranslateUi

