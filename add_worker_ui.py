# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_worker.ui'
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

class Ui_Add_Worker(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(322, 254)
        MainWindow.setStyleSheet(u"background: #2C2D2F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(160, 10, 152, 30))
        self.name_input.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border-radius: 20px;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 142, 30))
        self.label.setStyleSheet(u"  padding-left: 20px;\n"
"  padding-right: 20px;\n"
"  padding-top: 5px;\n"
"  padding-bottom: 5px;\n"
"  background: white;\n"
"  border-radius: 50px;")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 142, 30))
        self.label_2.setStyleSheet(u"  width: 283px;\n"
"  height: 61px;\n"
"  padding-left: 20px;\n"
"  padding-right: 20px;\n"
"  padding-top: 5px;\n"
"  padding-bottom: 5px;\n"
"  background: white;\n"
"  border-radius: 50px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 142, 30))
        self.label_3.setStyleSheet(u"  width: 283px;\n"
"  height: 61px;\n"
"  padding-left: 20px;\n"
"  padding-right: 20px;\n"
"  padding-top: 5px;\n"
"  padding-bottom: 5px;\n"
"  background: white;\n"
"  border-radius: 50px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 142, 30))
        self.label_4.setStyleSheet(u"  width: 283px;\n"
"  height: 61px;\n"
"  padding-left: 20px;\n"
"  padding-right: 20px;\n"
"  padding-top: 5px;\n"
"  padding-bottom: 5px;\n"
"  background: white;\n"
"  border-radius: 50px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 142, 30))
        self.label_5.setStyleSheet(u"  width: 283px;\n"
"  height: 61px;\n"
"  padding-left: 20px;\n"
"  padding-right: 20px;\n"
"  padding-top: 5px;\n"
"  padding-bottom: 5px;\n"
"  background: white;\n"
"  border-radius: 50px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;")
        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(180, 210, 114, 35))
        self.add_btn.setStyleSheet(u"width: 229px;\n"
"  height: 69px;\n"
"  background: #24FF00;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;")
        self.name_input_2 = QLineEdit(self.centralwidget)
        self.name_input_2.setObjectName(u"name_input_2")
        self.name_input_2.setGeometry(QRect(160, 50, 152, 30))
        self.name_input_2.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border-radius: 20px;")
        self.name_input_4 = QLineEdit(self.centralwidget)
        self.name_input_4.setObjectName(u"name_input_4")
        self.name_input_4.setGeometry(QRect(160, 130, 152, 30))
        self.name_input_4.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border-radius: 20px;")
        self.name_input_5 = QLineEdit(self.centralwidget)
        self.name_input_5.setObjectName(u"name_input_5")
        self.name_input_5.setGeometry(QRect(160, 170, 152, 30))
        self.name_input_5.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border-radius: 20px;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 90, 151, 31))
        self.comboBox.setStyleSheet(u"background: white;\n"
"color: black;\n"
"border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041f\u0430\u0441\u043f\u043e\u0440\u0442</p></body></html>", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"ROLE_MEMBER", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"ROLE_ADMIN", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ROLE_OWNER", None))

    # retranslateUi

