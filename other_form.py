from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QCoreApplication
from other_orders_ui import Ui_Other_Order

import sys

class OtherOrder(QMainWindow):
    def __init__(self):
        super(OtherOrder, self).__init__()
        self.ui = Ui_Other_Order()
        self.ui.setupUi(self)

        self.initialization()
    
    def initialization(self):
        try:
            with open('parsers/data/taker_maker.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                self.ui.textEdit.setText(text)
        except:
            pass
        
        try: 
            with open('parsers/data/maker_maker.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                self.ui.textEdit_2.setText(text)
        except:
            pass
        
        try: 
            with open('parsers/data/maker_taker.txt', 'r', encoding='utf-8') as file:
                text = file.read()
                self.ui.textEdit_3.setText(text)
        except: 
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OtherOrder()
    window.show()
    sys.exit(app.exec())

