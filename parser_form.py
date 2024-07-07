from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QCoreApplication
from parser_ui import Ui_Parser
from parsers.p2p import P2PTrade1
from parsers.advertises_config import bybit_data
import subprocess
import json
import os
import sys

class ParserForm(QMainWindow): 
    def __init__(self): 
        super(ParserForm, self).__init__()
        self.ui = Ui_Parser()
        self.ui.setupUi(self)

        self.initialization()
        self.connectionButtons()

        self.pos = 'taker_maker'
        self.set_best_orders()

    def initialization(self):
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()

        self.ui.label_6.setText('') 
        self.ui.label_9.setText('') 
        self.ui.label_13.setText('')
        self.ui.label_16.setText('')
        self.ui.label_19.setText('')
        self.ui.label_7.setText('') 
        self.ui.label_10.setText('')
        self.ui.label_12.setText('')
        self.ui.label_17.setText('')
        self.ui.label_20.setText('')
        self.ui.label_29.setText('')
        self.ui.label_30.setText('')
        self.ui.label_31.setText('')
        self.ui.label_32.setText('')
        self.ui.label_33.setText('') 
        
        if self.ui.comboBox.currentText() == 'BYBIT':
            list_crypto_bybit = bybit_data['bybit']['crypto']
            list_bank_bybit = bybit_data['bybit']['bank']
            list_list_bank_bybit = []
            
            for key, value in list_bank_bybit.items():
                list_list_bank_bybit.append(key) 
            
            self.ui.comboBox_2.addItems(list_crypto_bybit)
            self.ui.comboBox_3.addItems(list_list_bank_bybit)

        elif self.ui.comboBox.currentText() == "HUOBI":
            pass
        
        else: 
            pass

    def connectionButtons(self):
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.initialization())
        self.ui.pushButton_6.clicked.connect(lambda: self.update_order(self.ui.comboBox.currentText()))
        self.ui.pushButton_7.clicked.connect(lambda: self.change_button())
        self.ui.pushButton_2.clicked.connect(lambda: subprocess.Popen(["py", "other_form.py"]))
        #self.ui.pushButton_2.clicked.connect(lambda: OtherOrder().show)
        self.ui.pushButton.clicked.connect(lambda: subprocess.Popen(["py", os.path.join('parsers', 'find_best_price.py')]))
        self.ui.pushButton_3.clicked.connect(lambda: self.set_pos('maker_taker'))
        self.ui.pushButton_4.clicked.connect(lambda: self.set_pos('taker_maker'))
        self.ui.pushButton_5.clicked.connect(lambda: self.set_pos('maker_maker'))

    def change_button(self):
        if self.ui.pushButton_7.text() == 'ПОКУПКА':
            self.ui.pushButton_7.setStyleSheet(u"color: white;\n"
    "background: red;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u041e\u0414\u0410\u0416\u0410", None))
        elif self.ui.pushButton_7.text() == 'ПРОДАЖА':
            self.ui.pushButton_7.setStyleSheet(u"color: white;\n"
    "background: lime;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e\u041a\u0423\u041f\u041a\u0410", None))

    def set_pos(self, pos):
        self.pos = pos
        if pos == 'maker_taker':
            self.ui.pushButton_3.setStyleSheet(u"color: white;\n"
    "background: #00F0FF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_4.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_5.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
        elif pos == 'taker_maker':
            self.ui.pushButton_3.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_4.setStyleSheet(u"color: white;\n"
    "background: #00F0FF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_5.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
        elif pos == 'maker_maker':
            self.ui.pushButton_3.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_4.setStyleSheet(u"color: white;\n"
    "background: #000AFF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")
            self.ui.pushButton_5.setStyleSheet(u"color: white;\n"
    "background: #00F0FF;\n"
    "border-radius: 10px;\n"
    "font-size: 28px;")

        self.set_best_orders()

    def set_best_orders(self):
        with open(f'parsers/data/{self.pos}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        try:
            buy_crypto = data['buy_crypto']
            buy_price = data['buy_price']
            buy_order = data['buy_order']

            sell_crypto = data['sell_crypto']
            sell_price = data['sell_price']
            sell_order = data['sell_order']

            percent = data['percent']

            self.ui.label_23.setText(str(buy_crypto))
            self.ui.label_25.setText(str(buy_price))
            self.ui.label_26.setText(str(buy_order))

            self.ui.label_24.setText(str(sell_crypto))
            self.ui.label_27.setText(str(sell_price))
            self.ui.label_28.setText(str(sell_order))

            self.ui.label_35.setText(str(percent) + '%')

        except Exception as ex:
           self.ui.label_23.setText(str())
           self.ui.label_25.setText("Обнови курсы!")
           self.ui.label_26.setText(str())

           self.ui.label_24.setText(str())
           self.ui.label_27.setText("Обнови курсы!")
           self.ui.label_28.setText(str())

           self.ui.label_35.setText('0%')
           print(ex)

    def update_order(self, exchange):
        crypto = self.ui.comboBox_2.currentText()
        side = 'buy' if self.ui.pushButton_7.text() == 'ПОКУПКА' else 'sell'
        payments = bybit_data[exchange.lower()]['bank'][self.ui.comboBox_3.currentText()]

        cl = P2PTrade1(fiat='RUB', crypto=crypto, side=side, payments=payments)
        if exchange == 'BYBIT': 
            try:
                data = cl.bybitP2P()
                items = data['result']['items']

                try:
                    self.ui.label_6.setText(str(items[0]['price']))
                except (IndexError, KeyError, TypeError):
                    self.ui.label_6.setText('')

                try:
                    self.ui.label_9.setText(str(items[1]['price']))
                except (IndexError, KeyError, TypeError):
                    self.ui.label_9.setText('')

                try:
                    self.ui.label_13.setText(str(items[2]['price']))
                except (IndexError, KeyError, TypeError):
                    self.ui.label_13.setText('')

                try:
                    self.ui.label_16.setText(str(items[3]['price']))
                except (IndexError, KeyError, TypeError):
                    self.ui.label_16.setText('')

                try:
                    self.ui.label_19.setText(str(items[4]['price']))
                except (IndexError, KeyError, TypeError):
                    self.ui.label_19.setText('')

                try:
                    self.ui.label_7.setText(f'https://www.bybit.com/fiat/trade/otc/profile/{items[0]["userId"]}/{crypto}/RUB/item')
                except Exception as ex:
                    self.ui.label_7.setText('')
                    print('Ошибка 1', ex)

                try:
                    self.ui.label_10.setText(f'https://www.bybit.com/fiat/trade/otc/profile/{items[1]["userId"]}/{crypto}/RUB/item')
                except (IndexError, KeyError, TypeError):
                    self.ui.label_10.setText('')

                try:
                    self.ui.label_12.setText(f'https://www.bybit.com/fiat/trade/otc/profile/{items[2]["userId"]}/{crypto}/RUB/item')
                except (IndexError, KeyError, TypeError):
                    self.ui.label_12.setText('')

                try:
                    self.ui.label_17.setText(f'https://www.bybit.com/fiat/trade/otc/profile/{items[3]["userId"]}/{crypto}/RUB/item')
                except (IndexError, KeyError, TypeError):
                    self.ui.label_17.setText('')

                try:
                    self.ui.label_20.setText(f'https://www.bybit.com/fiat/trade/otc/profile/{items[4]["userId"]}/{crypto}/RUB/item')
                except (IndexError, KeyError, TypeError):
                    self.ui.label_20.setText('')

                try:
                    self.ui.label_29.setText(items[0]['nickName'])
                except Exception as ex:
                    self.ui.label_29.setText('')
                    print('Ошибка 2', ex)

                try:
                    self.ui.label_30.setText(items[1]['nickName'])
                except (IndexError, KeyError, TypeError):
                    self.ui.label_30.setText('')

                try:
                    self.ui.label_31.setText(items[2]['nickName'])
                except (IndexError, KeyError, TypeError):
                    self.ui.label_31.setText('')

                try:
                    self.ui.label_32.setText(items[3]['nickName'])
                except (IndexError, KeyError, TypeError):
                    self.ui.label_32.setText('')

                try:
                    self.ui.label_33.setText(items[4]['nickName'])
                except (IndexError, KeyError, TypeError):
                    self.ui.label_33.setText('')
            except Exception as ex:
                print(ex)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParserForm()
    window.show()
    sys.exit(app.exec())