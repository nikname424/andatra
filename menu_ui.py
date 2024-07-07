# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1257, 739)
        MainWindow.setStyleSheet(u"background: #2C2D2F;\n"
"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_13 = QAction(MainWindow)
        self.action_13.setObjectName(u"action_13")
        self.action_14 = QAction(MainWindow)
        self.action_14.setObjectName(u"action_14")
        self.action_15 = QAction(MainWindow)
        self.action_15.setObjectName(u"action_15")
        self.action_16 = QAction(MainWindow)
        self.action_16.setObjectName(u"action_16")
        self.action_17 = QAction(MainWindow)
        self.action_17.setObjectName(u"action_17")
        self.action_18 = QAction(MainWindow)
        self.action_18.setObjectName(u"action_18")
        self.action_19 = QAction(MainWindow)
        self.action_19.setObjectName(u"action_19")
        self.action_20 = QAction(MainWindow)
        self.action_20.setObjectName(u"action_20")
        self.action_PRO = QAction(MainWindow)
        self.action_PRO.setObjectName(u"action_PRO")
        self.action_API = QAction(MainWindow)
        self.action_API.setObjectName(u"action_API")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.translate_text = QLabel(self.centralwidget)
        self.translate_text.setObjectName(u"translate_text")
        self.translate_text.setGeometry(QRect(1070, -130, 262, 37))
        font = QFont()
        font.setPointSize(24)
        self.translate_text.setFont(font)
        self.change_crypto_btn = QPushButton(self.centralwidget)
        self.change_crypto_btn.setObjectName(u"change_crypto_btn")
        self.change_crypto_btn.setGeometry(QRect(770, 470, 220, 81))
        self.change_crypto_btn.setStyleSheet(u"width: 184px;\n"
"height: 37px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 48px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"background-color: white;\n"
"\n"
"    width: 220px;\n"
"    height: 75px;\n"
"    border-radius: 20px;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 742, 696))
        self.frame.setStyleSheet(u"width: 742px;\n"
"height: 696px;\n"
"background: white;\n"
"border-radius: 25px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.payments_to_investors_num = QLabel(self.frame)
        self.payments_to_investors_num.setObjectName(u"payments_to_investors_num")
        self.payments_to_investors_num.setGeometry(QRect(440, 106, 285, 75))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setBold(False)
        self.payments_to_investors_num.setFont(font1)
        self.payments_to_investors_num.setStyleSheet(u"width: 254px;\n"
"height: 80.56px;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"width: 63px;\n"
"height: 62.30px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.payments_to_investors_num.setAlignment(Qt.AlignCenter)
        self.Payments_to_investors_text = QLabel(self.frame)
        self.Payments_to_investors_text.setObjectName(u"Payments_to_investors_text")
        self.Payments_to_investors_text.setGeometry(QRect(10, 106, 424, 75))
        self.Payments_to_investors_text.setFont(font1)
        self.Payments_to_investors_text.setStyleSheet(u"width: 435px;\n"
"height: 80.56px;\n"
"left: 0px;\n"
"top: 0px;\n"
"position: absolute;\n"
"background: rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"width: 428px;\n"
"height: 62.30px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 64px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.Payments_to_investors_text.setTextFormat(Qt.AutoText)
        self.Payments_to_investors_text.setAlignment(Qt.AlignCenter)
        self.all_balance_fiat_text = QLabel(self.frame)
        self.all_balance_fiat_text.setObjectName(u"all_balance_fiat_text")
        self.all_balance_fiat_text.setGeometry(QRect(10, 192, 424, 75))
        self.all_balance_fiat_text.setFont(font1)
        self.all_balance_fiat_text.setStyleSheet(u"width: 435px;\n"
"    height: 87.47px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"    display: flex;\n"
"    justify-content: center;\n"
"    align-items: center;\n"
"width: 380px;\n"
"height: 67.64px;\n"
"color: black;\n"
"font-size: 54px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.all_balance_fiat_num = QLabel(self.frame)
        self.all_balance_fiat_num.setObjectName(u"all_balance_fiat_num")
        self.all_balance_fiat_num.setGeometry(QRect(440, 192, 285, 75))
        self.all_balance_fiat_num.setFont(font1)
        self.all_balance_fiat_num.setStyleSheet(u"width: 380px;\n"
"height: 67.64px;\n"
"color: black;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"width: 254px;\n"
"    height: 87.47px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 63px;\n"
"height: 67.64px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"")
        self.all_balance_fiat_num.setAlignment(Qt.AlignCenter)
        self.current_income_text = QLabel(self.frame)
        self.current_income_text.setObjectName(u"current_income_text")
        self.current_income_text.setGeometry(QRect(10, 20, 424, 76))
        self.current_income_text.setFont(font1)
        self.current_income_text.setStyleSheet(u"  width: 435px;\n"
"  height: 80.45px;\n"
"  position: relative;\n"
"width: 435px;\n"
"  height: 80.45px;\n"
"  position: absolute;\n"
"  left: 0px;\n"
"  top: 0px;\n"
"  background: rgba(0, 0, 0, 0.25);\n"
"  border-radius: 10px;\n"
"width: 430px;\n"
"  height: 59.16px;\n"
"  position: absolute;\n"
"  left: 0px;\n"
"  top: 10.65px;\n"
"  text-align: center;\n"
"  color: black;\n"
"  font-size: 48px;\n"
"  font-family: Inter;\n"
"  font-weight: 400;\n"
"  word-wrap: break-word;")
        self.current_income_text.setAlignment(Qt.AlignCenter)
        self.current_income_num = QLabel(self.frame)
        self.current_income_num.setObjectName(u"current_income_num")
        self.current_income_num.setGeometry(QRect(440, 20, 285, 76))
        self.current_income_num.setFont(font1)
        self.current_income_num.setStyleSheet(u"width: 254.20px; height: 81.64px; position: relative;\n"
"width: 254.20px; height: 81.64px; background: rgba(0, 0, 0, 0.25); border-radius: 10px;\n"
"width: 59.68px; height: 68.62px; text-align: center; color: black; font-size: 64px; font-family: Inter; font-weight: 400; word-wrap: break-word;\n"
"font-size: 24px;")
        self.current_income_num.setAlignment(Qt.AlignCenter)
        self.balance_crypto_text = QLabel(self.frame)
        self.balance_crypto_text.setObjectName(u"balance_crypto_text")
        self.balance_crypto_text.setGeometry(QRect(10, 278, 231, 75))
        self.balance_crypto_text.setFont(font1)
        self.balance_crypto_text.setStyleSheet(u"width: 435px;\n"
"    height: 74px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 212px;\n"
"height: 70px;\n"
"color: black;\n"
"font-size: 58px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.balance_crypto_box = QComboBox(self.frame)
        self.balance_crypto_box.addItem("")
        self.balance_crypto_box.addItem("")
        self.balance_crypto_box.addItem("")
        self.balance_crypto_box.setObjectName(u"balance_crypto_box")
        self.balance_crypto_box.setGeometry(QRect(245, 278, 189, 75))
        self.balance_crypto_box.setFont(font1)
        self.balance_crypto_box.setStyleSheet(u"width: 193px;\n"
"    height: 74px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 212px;\n"
"height: 70px;\n"
"color: red;\n"
"font-size: 58px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;")
        self.balance_crypto_num = QLabel(self.frame)
        self.balance_crypto_num.setObjectName(u"balance_crypto_num")
        self.balance_crypto_num.setGeometry(QRect(440, 278, 285, 75))
        self.balance_crypto_num.setFont(font1)
        self.balance_crypto_num.setStyleSheet(u"width: 380px;\n"
"height: 67.64px;\n"
"color: black;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"width: 254px;\n"
"    height: 87.47px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 63px;\n"
"height: 67.64px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 24px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"")
        self.balance_crypto_num.setAlignment(Qt.AlignCenter)
        self.input_text = QLabel(self.frame)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(400, 370, 121, 70))
        self.input_text.setFont(font1)
        self.input_text.setStyleSheet(u"width: 155.09px;\n"
"height: 69px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 40px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"    width: 339px;\n"
"    height: 69px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"\n"
"")
        self.comboBox_8 = QComboBox(self.frame)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(530, 370, 190, 70))
        self.comboBox_8.setStyleSheet(u"    width: 189.91px;\n"
"    height: 69px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"color: blue;")
        self.comboBox_9 = QComboBox(self.frame)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(200, 370, 190, 70))
        self.comboBox_9.setStyleSheet(u"    width: 189.91px;\n"
"    height: 69px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"color: blue;")
        self.output_text_2 = QLabel(self.frame)
        self.output_text_2.setObjectName(u"output_text_2")
        self.output_text_2.setGeometry(QRect(10, 370, 181, 70))
        self.output_text_2.setFont(font1)
        self.output_text_2.setStyleSheet(u"width: 155.09px;\n"
"height: 69px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 40px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"    width: 339px;\n"
"    height: 69px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"\n"
"")
        self.output_text_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(229, 500, 301, 40))
        self.lineEdit_3.setStyleSheet(u"    width: 301px;\n"
"    height: 39px;\n"
"    background: #D9D9D9;\n"
"    border-radius: 10px;\n"
"\n"
"width: 163px;\n"
"height: 35px;\n"
"text-align: center;\n"
"color: rgba(0, 0, 0, 0.50);\n"
"font-size: 20px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 590, 721, 91))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_translate = QPushButton(self.layoutWidget)
        self.btn_translate.setObjectName(u"btn_translate")
        self.btn_translate.setStyleSheet(u"    width: 324px;\n"
"    height: 75px;\n"
"    background: rgba(110.33, 59.50, 255, 0.70);\n"
"    border-radius: 20px;\n"
"\n"
"width: 249.68px;\n"
"height: 64px;\n"
"text-align: center;\n"
"color: white;\n"
"font-size: 48px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")

        self.horizontalLayout.addWidget(self.btn_translate)

        self.btn_translate_2 = QPushButton(self.layoutWidget)
        self.btn_translate_2.setObjectName(u"btn_translate_2")
        self.btn_translate_2.setStyleSheet(u"    width: 324px;\n"
"    height: 75px;\n"
"    background: rgba(59.50, 255, 125.97, 0.75);\n"
"    border-radius: 20px;\n"
"width: 249.68px;\n"
"height: 64px;\n"
"text-align: center;\n"
"color: white;\n"
"font-size: 64px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"opacity: 0.5;")

        self.horizontalLayout.addWidget(self.btn_translate_2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(770, 10, 474, 401))
        self.frame_2.setStyleSheet(u"    width: 473px;\n"
"    height: 464px;\n"
"    background: white;\n"
"    border-radius: 25px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.balance_card_text = QLabel(self.frame_2)
        self.balance_card_text.setObjectName(u"balance_card_text")
        self.balance_card_text.setGeometry(QRect(10, 20, 280, 76))
        self.balance_card_text.setFont(font1)
        self.balance_card_text.setStyleSheet(u"    width: 280.71px;\n"
"    height: 80.45px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"\n"
"width: 277.48px;\n"
"height: 59.16px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 48px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;")
        self.balance_card_text.setAlignment(Qt.AlignCenter)
        self.balance_card_num = QLabel(self.frame_2)
        self.balance_card_num.setObjectName(u"balance_card_num")
        self.balance_card_num.setGeometry(QRect(300, 20, 164, 76))
        self.balance_card_num.setFont(font1)
        self.balance_card_num.setStyleSheet(u"    width: 164.03px;\n"
"    height: 81.64px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 38.51px;\n"
"height: 68.62px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 64px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"font-size: 24px;")
        self.balance_card_num.setAlignment(Qt.AlignCenter)
        self.balance_card_text_2 = QLabel(self.frame_2)
        self.balance_card_text_2.setObjectName(u"balance_card_text_2")
        self.balance_card_text_2.setGeometry(QRect(10, 106, 280, 76))
        self.balance_card_text_2.setFont(font1)
        self.balance_card_text_2.setStyleSheet(u"    width: 280.71px;\n"
"    height: 80.45px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"\n"
"width: 277.48px;\n"
"height: 59.16px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 40px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"")
        self.balance_card_text_2.setAlignment(Qt.AlignCenter)
        self.turnover_SBP_num = QLabel(self.frame_2)
        self.turnover_SBP_num.setObjectName(u"turnover_SBP_num")
        self.turnover_SBP_num.setGeometry(QRect(300, 106, 164, 76))
        self.turnover_SBP_num.setFont(font1)
        self.turnover_SBP_num.setStyleSheet(u"    width: 164.03px;\n"
"    height: 81.64px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 38.51px;\n"
"height: 68.62px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 64px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"font-size: 24px;")
        self.turnover_SBP_num.setAlignment(Qt.AlignCenter)
        self.card_turnover_num = QLabel(self.frame_2)
        self.card_turnover_num.setObjectName(u"card_turnover_num")
        self.card_turnover_num.setGeometry(QRect(300, 192, 164, 76))
        self.card_turnover_num.setFont(font1)
        self.card_turnover_num.setStyleSheet(u"    width: 164.03px;\n"
"    height: 81.64px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"width: 38.51px;\n"
"height: 68.62px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 64px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"font-size: 24px;")
        self.card_turnover_num.setAlignment(Qt.AlignCenter)
        self.balance_card_text_3 = QLabel(self.frame_2)
        self.balance_card_text_3.setObjectName(u"balance_card_text_3")
        self.balance_card_text_3.setGeometry(QRect(10, 192, 280, 76))
        self.balance_card_text_3.setFont(font1)
        self.balance_card_text_3.setStyleSheet(u"    width: 280.71px;\n"
"    height: 80.45px;\n"
"    background: rgba(0, 0, 0, 0.25);\n"
"    border-radius: 10px;\n"
"\n"
"width: 277.48px;\n"
"height: 63.32px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"")
        self.balance_card_text_3.setAlignment(Qt.AlignCenter)
        self.choose_card_box = QComboBox(self.frame_2)
        self.choose_card_box.setObjectName(u"choose_card_box")
        self.choose_card_box.setGeometry(QRect(120, 310, 220, 40))
        self.choose_card_box.setStyleSheet(u"width: 220px;\n"
"height: 37px;\n"
"background: #D9D9D9;\n"
"border-radius: 10px;\n"
"color: blue;")
        self.spred_btn = QPushButton(self.centralwidget)
        self.spred_btn.setObjectName(u"spred_btn")
        self.spred_btn.setGeometry(QRect(1020, 470, 220, 81))
        self.spred_btn.setStyleSheet(u"width: 184px;\n"
"height: 37px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 44px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"background-color: white;\n"
"\n"
"    width: 220px;\n"
"    height: 75px;\n"
"    border-radius: 20px;")
        self.spred_btn_2 = QPushButton(self.centralwidget)
        self.spred_btn_2.setObjectName(u"spred_btn_2")
        self.spred_btn_2.setGeometry(QRect(1020, 580, 220, 81))
        self.spred_btn_2.setStyleSheet(u"width: 184px;\n"
"height: 37px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 40px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"background-color: white;\n"
"\n"
"    width: 220px;\n"
"    height: 75px;\n"
"    border-radius: 20px;")
        self.spred_btn_3 = QPushButton(self.centralwidget)
        self.spred_btn_3.setObjectName(u"spred_btn_3")
        self.spred_btn_3.setGeometry(QRect(770, 580, 220, 81))
        self.spred_btn_3.setStyleSheet(u"width: 184px;\n"
"height: 37px;\n"
"text-align: center;\n"
"color: black;\n"
"font-size: 50px;\n"
"font-family: Inter;\n"
"font-weight: 400;\n"
"word-wrap: break-word;\n"
"\n"
"background-color: white;\n"
"\n"
"    width: 220px;\n"
"    height: 75px;\n"
"    border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1257, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_5 = QMenu(self.menu_2)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_9)
        self.menu.addAction(self.action_API)
        self.menu.addSeparator()
        self.menu.addAction(self.action_11)
        self.menu_2.addAction(self.menu_5.menuAction())
        self.menu_2.addAction(self.action_13)
        self.menu_5.addAction(self.action_16)
        self.menu_5.addAction(self.action_17)
        self.menu_3.addAction(self.action)
        self.menu_3.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_5)
        self.menu_3.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_4.addAction(self.action_18)
        self.menu_4.addAction(self.action_19)
        self.menu_4.addAction(self.action_20)
        self.menu_4.addAction(self.action_PRO)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u0443", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0432\u0435\u0441\u0442\u043e\u0440\u0430", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u0443", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u043d\u0432\u0435\u0441\u0442\u043e\u0440\u0430", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u044e", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043e\u0440\u0434\u0435\u0440\u043e\u0432", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u043d\u0447\u0438\u0442\u044c \u0441\u0435\u0441\u0441\u0438\u044e", None))
        self.action_13.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0432\u044b\u043f\u0438\u0441\u043a\u0443 \u043f\u043e \u0432\u044b\u043f\u043b\u0430\u0442\u0430\u043c \u0438\u043d\u0432\u0435\u0442\u043e\u0440\u0430\u043c", None))
        self.action_14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0432\u044b\u043f\u0438\u0441\u043a\u0443 \u0434\u043b\u044f \u043d\u0430\u043b\u043e\u0433\u043e\u0432\u043e\u0439", None))
        self.action_15.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u044e \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.action_16.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u044e \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
        self.action_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044e \u043f\u043e \u043a\u0430\u0440\u0442\u0435", None))
        self.action_18.setText(QCoreApplication.translate("MainWindow", u"\u041e \u0432\u0435\u0440\u0441\u0438\u0438", None))
        self.action_19.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043d\u0430\u0441", None))
        self.action_20.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u043f\u0440\u0438\u043c\u0435\u043d\u0435\u043d\u0438\u044e", None))
        self.action_PRO.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0434\u043e PRO ", None))
        self.action_API.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u043b\u044e\u0447\u0438\u0442\u044c API", None))
#if QT_CONFIG(tooltip)
        self.translate_text.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.translate_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0421\u0434\u0435\u043b\u0430\u0442\u044c \u043f\u0435\u0440\u0435\u0432\u043e\u0434</p></body></html>", None))
        self.change_crypto_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0411\u041c\u0415\u041d", None))
        self.payments_to_investors_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Payments_to_investors_text.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043b\u0430\u0442\u044b", None))
        self.all_balance_fiat_text.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441 \u0444\u0438\u0430\u0442\u0430", None))
        self.all_balance_fiat_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.current_income_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0434\u043e\u0445\u043e\u0434", None))
        self.current_income_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.balance_crypto_text.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.balance_crypto_box.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC", None))
        self.balance_crypto_box.setItemText(1, QCoreApplication.translate("MainWindow", u"ETH", None))
        self.balance_crypto_box.setItemText(2, QCoreApplication.translate("MainWindow", u"USDT", None))

        self.balance_crypto_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input_text.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0434\u0430", None))
        self.output_text_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0443\u0434\u0430", None))
        self.lineEdit_3.setText("")
        self.btn_translate.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0415\u0420\u0415\u0412\u0415\u0421\u0422\u0418", None))
        self.btn_translate_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0422", None))
        self.balance_card_text.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043d\u0441", None))
        self.balance_card_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.balance_card_text_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0440\u043e\u0442 \u0421\u0411\u041f", None))
        self.turnover_SBP_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.card_turnover_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.balance_card_text_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043e\u0440\u043e\u0442 (\u041e\u0431\u0449\u0438\u0439)", None))
        self.spred_btn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410\u041d\u041d\u042b\u0415", None))
        self.spred_btn_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0410\u0411\u041b\u0418\u0426\u042b", None))
        self.spred_btn_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0410\u0420\u0421\u0415\u0420", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u0438\u0441\u043a\u0430", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c \u0438\u0441\u0442\u043e\u0440\u0438\u044e \u043e\u0440\u0434\u0435\u0440\u043e\u0432", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c/\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

