# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tables.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QWidget)

class Ui_TableForm(object):
    def setupUi(self, Add_card):
        if not Add_card.objectName():
            Add_card.setObjectName(u"Add_card")
        Add_card.resize(1240, 741)
        Add_card.setStyleSheet(u"width: 372px;\n"
"height: 152px;\n"
"background: #2C2D2F;\n"
"")
        self.centralwidget = QWidget(Add_card)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 1210, 731))
        self.tabWidget.setStyleSheet(u"color: white;")
        self.cards = QWidget()
        self.cards.setObjectName(u"cards")
        self.tableView = QTableView(self.cards)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 10, 1210, 610))
        self.tableView.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.pushButton_10 = QPushButton(self.cards)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(280, 630, 228, 70))
        self.pushButton_10.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #24FF00;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_11 = QPushButton(self.cards)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(540, 630, 228, 70))
        self.pushButton_11.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: orange;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 26px;\n"
"color: white;")
        self.pushButton_12 = QPushButton(self.cards)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(800, 630, 228, 70))
        self.pushButton_12.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #FF0000;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.tabWidget.addTab(self.cards, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableView_2 = QTableView(self.tab_3)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(10, 10, 1210, 610))
        self.tableView_2.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.pushButton_7 = QPushButton(self.tab_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(800, 630, 228, 70))
        self.pushButton_7.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #FF0000;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_8 = QPushButton(self.tab_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(280, 630, 228, 70))
        self.pushButton_8.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #24FF00;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_9 = QPushButton(self.tab_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(540, 630, 228, 70))
        self.pushButton_9.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: orange;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 26px;\n"
"color: white;")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableView_3 = QTableView(self.tab_2)
        self.tableView_3.setObjectName(u"tableView_3")
        self.tableView_3.setGeometry(QRect(10, 10, 1210, 610))
        self.tableView_3.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(800, 630, 228, 70))
        self.pushButton_4.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #FF0000;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_5 = QPushButton(self.tab_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 630, 228, 70))
        self.pushButton_5.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #24FF00;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_6 = QPushButton(self.tab_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(540, 630, 228, 70))
        self.pushButton_6.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: orange;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 26px;\n"
"color: white;")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableView_4 = QTableView(self.tab)
        self.tableView_4.setObjectName(u"tableView_4")
        self.tableView_4.setGeometry(QRect(10, 10, 1210, 610))
        self.tableView_4.setStyleSheet(u"background: white;\n"
"border-radius: 10px;")
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 630, 228, 70))
        self.pushButton.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #24FF00;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(540, 630, 228, 70))
        self.pushButton_3.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: orange;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 26px;\n"
"color: white;")
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(800, 630, 228, 70))
        self.pushButton_2.setStyleSheet(u"  width: 229px;\n"
"  height: 69px;\n"
"  background: #FF0000;\n"
"  border-radius: 20px;\n"
"  overflow: hidden;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  display: inline-flex;\n"
"font-size: 36px;\n"
"color: white;")
        self.tabWidget.addTab(self.tab, "")
        Add_card.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_card)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Add_card)
    # setupUi

    def retranslateUi(self, Add_card):
        Add_card.setWindowTitle(QCoreApplication.translate("Add_card", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("Add_card", u"<html><head/><body><p>test</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.cards.setToolTip(QCoreApplication.translate("Add_card", u"<html><head/><body><p align=\"center\">\u041a\u0430\u0440\u0442\u044b</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText(QCoreApplication.translate("Add_card", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c", None))
        self.pushButton_11.setText(QCoreApplication.translate("Add_card", u"\u0420\u0415\u0414\u0410\u041a\u0422\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.pushButton_12.setText(QCoreApplication.translate("Add_card", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cards), QCoreApplication.translate("Add_card", u"\u041a\u0430\u0440\u0442\u044b", None))
        self.pushButton_7.setText(QCoreApplication.translate("Add_card", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_8.setText(QCoreApplication.translate("Add_card", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c", None))
        self.pushButton_9.setText(QCoreApplication.translate("Add_card", u"\u0420\u0415\u0414\u0410\u041a\u0422\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Add_card", u"\u041a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u044b", None))
        self.pushButton_4.setText(QCoreApplication.translate("Add_card", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Add_card", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c", None))
        self.pushButton_6.setText(QCoreApplication.translate("Add_card", u"\u0420\u0415\u0414\u0410\u041a\u0422\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Add_card", u"\u0418\u043d\u0432\u0435\u0441\u0442\u043e\u0440\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Add_card", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Add_card", u"\u0420\u0415\u0414\u0410\u041a\u0422\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Add_card", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Add_card", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
    # retranslateUi

