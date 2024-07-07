# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_crypto.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_CryptoChange(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(272, 138)
        MainWindow.setStyleSheet(u"background: #2C2D2F")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(167, 20, 91, 48))
        self.comboBox.setStyleSheet(u"color: black;\n"
"background: white;\n"
"border-radius: 5px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 90, 121, 31))
        self.pushButton.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: yellow;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"color: black;\n"
"font-size: 19px;")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 142, 30))
        self.lineEdit.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 50, 142, 30))
        self.lineEdit_2.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 90, 121, 31))
        self.pushButton_2.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: blue;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"color: white;\n"
"font-size: 19px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u0430", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
    # retranslateUi

