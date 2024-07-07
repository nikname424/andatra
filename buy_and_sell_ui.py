# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buy_and_sell.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_Buy_and_Sell(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 403)
        MainWindow.setStyleSheet(u"background: #2C2D2F;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 551, 384))
        self.frame_2.setStyleSheet(u"width: 542px;\n"
"height: 383px;\n"
"background: white;\n"
"border-radius: 10px;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.crypto_buy_text = QLabel(self.frame_2)
        self.crypto_buy_text.setObjectName(u"crypto_buy_text")
        self.crypto_buy_text.setGeometry(QRect(10, 10, 356, 50))
        font = QFont()
        self.crypto_buy_text.setFont(font)
        self.crypto_buy_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.crypto_buy_text.setAlignment(Qt.AlignCenter)
        self.crypto_buy_box = QComboBox(self.frame_2)
        self.crypto_buy_box.addItem("")
        self.crypto_buy_box.setObjectName(u"crypto_buy_box")
        self.crypto_buy_box.setGeometry(QRect(370, 10, 172, 50))
        self.crypto_buy_box.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.50);\n"
"border-radius: 5px;\n"
"font-size: 42px;\n"
"color: red;")
        self.enter_price_on_buy = QLineEdit(self.frame_2)
        self.enter_price_on_buy.setObjectName(u"enter_price_on_buy")
        self.enter_price_on_buy.setGeometry(QRect(370, 70, 172, 50))
        self.enter_price_on_buy.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"color: black;")
        self.price_on_buy_text = QLabel(self.frame_2)
        self.price_on_buy_text.setObjectName(u"price_on_buy_text")
        self.price_on_buy_text.setGeometry(QRect(10, 70, 356, 50))
        self.price_on_buy_text.setFont(font)
        self.price_on_buy_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.price_on_buy_text.setAlignment(Qt.AlignCenter)
        self.summ_on_buy_enter = QLineEdit(self.frame_2)
        self.summ_on_buy_enter.setObjectName(u"summ_on_buy_enter")
        self.summ_on_buy_enter.setGeometry(QRect(280, 130, 264, 50))
        self.summ_on_buy_enter.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"color: black;")
        self.summ_on_buy_text = QLabel(self.frame_2)
        self.summ_on_buy_text.setObjectName(u"summ_on_buy_text")
        self.summ_on_buy_text.setGeometry(QRect(10, 130, 264, 50))
        self.summ_on_buy_text.setFont(font)
        self.summ_on_buy_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.summ_on_buy_text.setAlignment(Qt.AlignCenter)
        self.card_for_buy_text = QLabel(self.frame_2)
        self.card_for_buy_text.setObjectName(u"card_for_buy_text")
        self.card_for_buy_text.setGeometry(QRect(10, 190, 264, 50))
        self.card_for_buy_text.setFont(font)
        self.card_for_buy_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.card_for_buy_box = QComboBox(self.frame_2)
        self.card_for_buy_box.addItem("")
        self.card_for_buy_box.setObjectName(u"card_for_buy_box")
        self.card_for_buy_box.setGeometry(QRect(280, 190, 264, 50))
        self.card_for_buy_box.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.50);\n"
"border-radius: 5px;\n"
"font-size: 24px;\n"
"color: blue;")
        self.btn_buy = QPushButton(self.frame_2)
        self.btn_buy.setObjectName(u"btn_buy")
        self.btn_buy.setGeometry(QRect(300, 290, 222, 50))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(False)
        self.btn_buy.setFont(font1)
        self.btn_buy.setStyleSheet(u"width: 222px;\n"
"height: 55px;\n"
"background: rgba(60, 255, 126, 0.75);\n"
"border-radius: 10px;\n"
"color: white;\n"
"width: 221.83px;\n"
"height: 47.19px;\n"
"text-align: center;\n"
"color: white;\n"
"font-size: 36px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.use_SBP_buy_check = QCheckBox(self.frame_2)
        self.use_SBP_buy_check.setObjectName(u"use_SBP_buy_check")
        self.use_SBP_buy_check.setGeometry(QRect(40, 260, 200, 50))
        font2 = QFont()
        font2.setPointSize(14)
        self.use_SBP_buy_check.setFont(font2)
        self.use_SBP_buy_check.setStyleSheet(u"background: gray;")
        self.third_party_check = QCheckBox(self.frame_2)
        self.third_party_check.setObjectName(u"third_party_check")
        self.third_party_check.setGeometry(QRect(40, 320, 200, 50))
        self.third_party_check.setFont(font2)
        self.third_party_check.setStyleSheet(u"background: gray;")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(570, 10, 551, 384))
        self.frame_3.setStyleSheet(u"width: 542px;\n"
"height: 383px;\n"
"background: white;\n"
"border-radius: 10px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.crypto_sell_text = QLabel(self.frame_3)
        self.crypto_sell_text.setObjectName(u"crypto_sell_text")
        self.crypto_sell_text.setGeometry(QRect(10, 10, 356, 50))
        self.crypto_sell_text.setFont(font)
        self.crypto_sell_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.crypto_sell_text.setAlignment(Qt.AlignCenter)
        self.crypto_sell_box = QComboBox(self.frame_3)
        self.crypto_sell_box.addItem("")
        self.crypto_sell_box.addItem("")
        self.crypto_sell_box.addItem("")
        self.crypto_sell_box.setObjectName(u"crypto_sell_box")
        self.crypto_sell_box.setGeometry(QRect(370, 10, 172, 50))
        self.crypto_sell_box.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.50);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: red;")
        self.price_on_sell_text = QLabel(self.frame_3)
        self.price_on_sell_text.setObjectName(u"price_on_sell_text")
        self.price_on_sell_text.setGeometry(QRect(10, 70, 356, 50))
        self.price_on_sell_text.setFont(font)
        self.price_on_sell_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 44px;\n"
"color: black;")
        self.price_on_sell_text.setAlignment(Qt.AlignCenter)
        self.enter_price_on_sell = QLineEdit(self.frame_3)
        self.enter_price_on_sell.setObjectName(u"enter_price_on_sell")
        self.enter_price_on_sell.setGeometry(QRect(370, 70, 172, 50))
        self.enter_price_on_sell.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"color: black;")
        self.summ_on_sell_text = QLabel(self.frame_3)
        self.summ_on_sell_text.setObjectName(u"summ_on_sell_text")
        self.summ_on_sell_text.setGeometry(QRect(10, 130, 264, 50))
        self.summ_on_sell_text.setFont(font)
        self.summ_on_sell_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 24px;\n"
"color: black;")
        self.summ_on_sell_text.setAlignment(Qt.AlignCenter)
        self.summ_on_sell_enter = QLineEdit(self.frame_3)
        self.summ_on_sell_enter.setObjectName(u"summ_on_sell_enter")
        self.summ_on_sell_enter.setGeometry(QRect(280, 130, 264, 50))
        self.summ_on_sell_enter.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"color: black;")
        self.card_for_sell_text = QLabel(self.frame_3)
        self.card_for_sell_text.setObjectName(u"card_for_sell_text")
        self.card_for_sell_text.setGeometry(QRect(10, 190, 261, 53))
        self.card_for_sell_text.setFont(font)
        self.card_for_sell_text.setStyleSheet(u"width: 356px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 5px;\n"
"font-size: 32px;\n"
"color: black;")
        self.card_for_sell_text.setAlignment(Qt.AlignCenter)
        self.card_for_sell_box = QComboBox(self.frame_3)
        self.card_for_sell_box.setObjectName(u"card_for_sell_box")
        self.card_for_sell_box.setGeometry(QRect(280, 190, 264, 50))
        self.card_for_sell_box.setStyleSheet(u"width: 172px;\n"
"height: 50px;\n"
"background: rgba(0, 0, 0, 0.50);\n"
"border-radius: 5px;\n"
"font-size: 24px;\n"
"color: blue;")
        self.btn_sell = QPushButton(self.frame_3)
        self.btn_sell.setObjectName(u"btn_sell")
        self.btn_sell.setGeometry(QRect(30, 290, 222, 50))
        self.btn_sell.setFont(font1)
        self.btn_sell.setStyleSheet(u"width: 222px;\n"
"height: 55px;\n"
"background: rgba(250, 0, 0, 0.75);\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 28px;\n"
"width: 221.83px;\n"
"height: 47.19px;\n"
"text-align: center;\n"
"color: white;\n"
"font-size: 36px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.fresh_btn = QPushButton(self.frame_3)
        self.fresh_btn.setObjectName(u"fresh_btn")
        self.fresh_btn.setGeometry(QRect(310, 320, 235, 55))
        self.fresh_btn.setStyleSheet(u"width: 235px;\n"
"height: 55px;\n"
"background: rgba(110, 59, 255, 0.70);\n"
"border-radius: 10px;\n"
"color: white;\n"
"width: 221.83px;\n"
"height: 47.19px;\n"
"text-align: center;\n"
"color: white;\n"
"font-size: 36px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 250, 96, 60))
        font3 = QFont()
        font3.setPointSize(20)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"width: 97px;\n"
"height: 63px;\n"
"background: rgba(0, 0, 0, 0.05);\n"
"border-radius: 5px;\n"
"color: black;\n"
"")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(410, 260, 131, 41))
        self.label.setStyleSheet(u"width: 138px;\n"
"height: 46px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 34px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.crypto_buy_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0443\u043f\u0430\u0435\u043c", None))
        self.crypto_buy_box.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC", None))

        self.price_on_buy_text.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438", None))
        self.summ_on_buy_enter.setText("")
        self.summ_on_buy_text.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.card_for_buy_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">\u041a\u0430\u0440\u0442\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438</span></p></body></html>", None))
        self.card_for_buy_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

        self.btn_buy.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u041a\u0423\u041f\u041a\u0410", None))
        self.use_SBP_buy_check.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u0442\u0435 \u0421\u0411\u041f?", None))
        self.third_party_check.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442 3-\u0438\u0445 \u043b\u0438\u0446", None))
        self.crypto_sell_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u0430\u0451\u043c", None))
        self.crypto_sell_box.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC", None))
        self.crypto_sell_box.setItemText(1, QCoreApplication.translate("MainWindow", u"USDT", None))
        self.crypto_sell_box.setItemText(2, QCoreApplication.translate("MainWindow", u"ETH", None))

        self.price_on_sell_text.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.summ_on_sell_text.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u044b", None))
        self.summ_on_sell_enter.setText("")
        self.card_for_sell_text.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438", None))
        self.btn_sell.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u041e\u0414\u0410\u0416\u0410", None))
        self.fresh_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041d\u041e\u0412\u0418\u0422\u042c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">0%</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430 \u043a\u0440\u0443\u0433", None))
    # retranslateUi

