# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_card.ui'
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

class Ui_ChangeCard(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(220, 250)
        MainWindow.setStyleSheet(u"background: #2C2D2F")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 10, 48, 48))
        self.comboBox.setStyleSheet(u"color: black;\n"
"background: white;\n"
"border-radius: 5px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 210, 121, 31))
        self.pushButton.setStyleSheet(u" background: yellow;\n"
" border-radius: 20px;\n"
"color: black;\n"
"font-size: 18px;")
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
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 130, 142, 30))
        self.lineEdit_4.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 170, 142, 30))
        self.lineEdit_5.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 90, 142, 30))
        self.lineEdit_3.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043d\u043a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0440\u043e\u0442", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0440\u043e\u0442 \u043f\u043e \u0421\u0411\u041f", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
    # retranslateUi

