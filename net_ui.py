# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'net_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import os

class Ui_Net(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1257, 768)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Устанавливаем фон через QLabel
        self.background_label = QLabel(self.centralwidget)
        self.background_label.setObjectName(u"background_label")
        self.background_label.setGeometry(MainWindow.rect())
        self.background_label.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), 'images/net.jpg')))
        self.background_label.setScaledContents(True)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 80, 1051, 551))
        self.label_2.setStyleSheet(u"background: white;\nborder-radius: 30px;")

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 550, 160, 50))
        self.pushButton.setStyleSheet(u"background: red;\ncolor: white;\nfont-size: 24px;\nborder-radius: 10px;")

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(700, 550, 160, 50))
        self.pushButton_2.setStyleSheet(u"background: lime;\ncolor: white;\nborder-radius: 10px;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">\u041c\u0438\u043d\u0438\u0441\u0442\u0435\u0440\u0441\u0442\u0432\u043e \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u044f \u0421\u0442\u0430\u0432\u0440\u043e\u043f\u043e\u043b\u044c\u0441\u043a\u043e\u0433\u043e \u041a\u0440\u0430\u044f</span></p><p align=\"center\"><span style=\" font-size:20pt;\">\u0413\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0431\u044e\u0434\u0436\u0435\u0442\u043d\u043e\u0435 \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u043e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0435 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u0435</span></p><p align=\"center\"><span style=\" font-size:20pt;\">&quot;\u041d\u0435\u0432\u0438\u043d\u043d\u043e\u043c\u044b\u0441\u0441\u043a\u0438\u0439 \u042d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 "
                        "\u0422\u0435\u0445\u043d\u0438\u043a\u0443\u043c&quot;</span></p><p align=\"center\"><span style=\" font-size:20pt;\">\u0414\u0438\u043f\u043b\u043e\u043c\u043d\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442 \u0410\u0418\u0421 &quot;\u041a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u0430&quot;</span></p><p align=\"center\"><span style=\" font-size:20pt;\">\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b \u0441\u0442\u0443\u0434\u0435\u043d\u0442 410 \u0433\u0440\u0443\u043f\u043f\u044b:</span></p><p align=\"center\"><span style=\" font-size:20pt;\">\u0421\u0430\u0432\u0447\u0435\u043d\u043a\u043e \u041d\u0438\u043a\u0438\u0442\u0430 \u0414\u043c\u0438\u0442\u0440\u0438\u0435\u0432\u0438\u0447</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \"\u041f\u0440\u0438\u0432\u0435\u0442\"", None))
    # retranslateUi
