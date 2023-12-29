import sqlite3
import config as cf
db_file = "DataAnd.db"

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_card(self, name_bank, number_card):
        with self.connection:
            try:
                self.cursor.execute("INSERT INTO `cards` (`name_bank`, `number_card`, `balance`, `turnover`, `turnover_sbp`) VALUES (?, ?, 0, 0, ?)", (name_bank, number_card, cf.limit_turnover_banks_SBP[name_bank.lower()]))
            except:
                pass

    def set_balance(self, number_card, balance, meaning):
        with self.connection:
            if meaning == 'set':
                self.cursor.execute("UPDATE `cards` SET `balance` = ? WHERE `number_card` = ?", (balance, number_card,))

            elif meaning == 'plus':
                self.cursor.execute("UPDATE `cards` SET `balance` = `balance` + ? WHERE `number_card` = ?", (balance, number_card,))

            elif meaning == 'minus':
                self.cursor.execute("UPDATE `cards` SET `balance` = `balance` - ? WHERE `number_card` = ?", (balance, number_card,))
            
            elif meaning == 'sbp':
                self.cursor.execute("UPDATE `cards` SET `turnover_sbp` = `turnover_sbp` - ? WHERE `number_card` = ?", (balance, number_card,))

            elif meaning == 'turnover':
                self.cursor.execute("UPDATE `cards` SET `turnover` = `turnover` + ? WHERE `number_card` = ?", (balance, number_card,))

    def set_crypto(self, name_crypto, quantity, meaning):
        with self.connection:
            if meaning == 'plus':
                # Проверяем, существует ли криптовалюта в таблице
                self.cursor.execute("SELECT 1 FROM `crypto` WHERE `name_crypto` = ?", (name_crypto,))
                
                exists = self.cursor.fetchone() is not None
                if exists:
                    self.cursor.execute("UPDATE `crypto` SET `quantity` = `quantity` + ? WHERE `name_crypto` = ?", (quantity, name_crypto,))

                else:
                    self.cursor.execute("INSERT INTO `crypto` (`name_crypto`, `quantity`) VALUES (?, ?)", (name_crypto, quantity,))

            elif meaning == 'minus':
                self.cursor.execute("UPDATE `crypto` SET `quantity` = `quantity` - ? WHERE `name_crypto` = ?", (quantity, name_crypto,))
            
            elif meaning == 'add':
                self.cursor.execute("INSERT OR IGNORE INTO `crypto` (`name_crypto`) VALUES (?)", (name_crypto,))

    def find_element(self, name_table, find_element, return_element):
        with self.connection:
            try:
                self.cursor.execute(f"SELECT `{return_element}` FROM `{name_table}` WHERE `{find_element[0]}` = ?", (find_element[1],))        
                result = self.cursor.fetchone()[0]
                return result
            except:
                return 0
    
    def double_element(self, name_table, first_element, second_element, return_element):
        with self.connection:
            try:
                self.cursor.execute(f"SELECT `{return_element}` FROM `{name_table}` WHERE `{first_element[0]}` = ? AND `{second_element[0]}` = ?", (first_element[1], second_element[1],))
                result = self.cursor.fetchall()
                return [item[0] for item in result]
            except:
                return []
            
    def get_all_data(self, card_name, element):
        with self.connection:
            try:
                self.cursor.execute(f"SELECT `{element}` FROM `history` WHERE `card_name` = ?", (card_name,))
                results = self.cursor.fetchall()
                sbp_list = [result[0] for result in results]
                return sbp_list
            except:
                return []
            
    def get_price_and_status(self, card_name, status):
        with self.connection:
            try:
                self.cursor.execute("SELECT `price` AND `summ_fiat` WHERE `card_name` = ? AND `status` = ?", (card_name, status,))
                result = self.cursor.fetchone()
                return result
            except Exception as ex:
                print(ex)
            
    def add_history(self, status, crypto_name, summ_fiat, price, quantity_crypto, name_bank, card_name, is_sbp, is_third_face):
        with self.connection:
            return self.cursor.execute("INSERT INTO `history` (`status`, `crypto_name`, `summ_fiat`, `price`, `quantity_crypto`, `name_bank`, `card_name`, `is_sbp`, `is_third_face`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (status, crypto_name, summ_fiat, price, quantity_crypto, name_bank, card_name, is_sbp, is_third_face))
        
    def add_investor(self, name, summ):
        with self.connection:
            self.cursor.execute("SELECT 1 FROM `investors` WHERE `name` = ?", (name,))
            exists = self.cursor.fetchone() is not None
            
            if exists:
                self.cursor.execute("UPDATE `investors` SET `summ` = `summ` + ? WHERE `name` = ?", (summ, name,))
            
            else:
                self.cursor.execute("INSERT INTO `investors` (`name`, `summ`) VALUES (?, ?)", (name, summ,))

    def get_all_elements(self, name_table, name_element):
        with self.connection:
            self.cursor.execute(f"SELECT `{name_element}` FROM `{name_table}`")
            cards_numbers = [row[0] for row in self.cursor.fetchall()]
            return cards_numbers
        
    def write_in_config(self, name_element):
        with self.connection:
            self.cursor.execute(f"UPDATE `config` SET `{name_element[0]}` = ?", (name_element[1],))

    def get_from_config(self, name_element):
        with self.connection:
            self.cursor.execute(f"SELECT `{name_element}` FROM `config`")
            res = self.cursor.fetchone()[0]
            return res
        
    def delete_all_data(self, name_table):
        with self.connection:
            self.cursor.execute(f"DELETE FROM `{name_table}`")
