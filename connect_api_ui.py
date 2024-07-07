# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect_api.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialogButtonBox,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QWidget)

class Ui_connect_api(object):
    def setupUi(self, connect_api):
        if not connect_api.objectName():
            connect_api.setObjectName(u"connect_api")
        connect_api.resize(389, 177)
        connect_api.setStyleSheet(u"background: #2C2D2F")
        self.centralwidget = QWidget(connect_api)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 130, 151, 31))
        self.checkBox.setStyleSheet(u"width: 210px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(190, 130, 169, 31))
        self.buttonBox.setStyleSheet(u"background: white;")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 10, 210, 50))
        self.lineEdit.setStyleSheet(u"width: 209px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 152, 50))
        self.label.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 152, 50))
        self.label_2.setStyleSheet(u"width: 152px;\n"
"height: 50px;\n"
"text-align: center;\n"
"color: #030303;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"width: 152px;\n"
"height: 50px;\n"
"opacity: 0.75;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 70, 210, 50))
        self.lineEdit_2.setStyleSheet(u"width: 209px;\n"
"height: 50px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        connect_api.setCentralWidget(self.centralwidget)

        self.retranslateUi(connect_api)

        QMetaObject.connectSlotsByName(connect_api)
    # setupUi

    def retranslateUi(self, connect_api):
        connect_api.setWindowTitle(QCoreApplication.translate("connect_api", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.checkBox.setToolTip(QCoreApplication.translate("connect_api", u"<html><head/><body><p><span style=\" font-size:20pt;\">\u041f\u043e\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox.setText(QCoreApplication.translate("connect_api", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("connect_api", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">API KEY</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("connect_api", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">API SECRET</span></p></body></html>", None))
        self.lineEdit_2.setText("")
    # retranslateUi

