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
        
    def add_investor(self, name, summ, income):
        with self.connection:
            self.cursor.execute("SELECT 1 FROM `investors` WHERE `name` = ?", (name,))
            exists = self.cursor.fetchone() is not None
            
            if exists:
                self.cursor.execute("UPDATE `investors` SET `summ` = ? AND `income` = ? WHERE `name` = ?", (summ, income, name,))
            
            else:
                self.cursor.execute("INSERT INTO `investors` (`name`, `summ`, `income`) VALUES (?, ?, ?)", (name, summ, income,))

    def delete_investor(self, name):
        with self.connection:
            try:
                self.cursor.execute("DELETE FROM investors WHERE name = ?", (name,))
                return 'OK'
            except Exception as ex:
                return ex

    def get_investors(self):
        with self.connection:
            self.cursor.execute("SELECT name FROM investors")
            data = self.cursor.fetchall()
            return [item[0] for item in data]
        
    def delete_card(self, card):
        with self.connection:
            try:
                self.cursor.execute("DELETE FROM cards WHERE number_card = ?", (card,))
                return 'OK'
            except Exception as ex:
                return ex
            
    def delete_crypto(self, crypto):
        with self.connection:
            try:
                self.cursor.execute("DELETE FROM crypto WHERE name_crypto = ?", (crypto,))
                return 'OK'
            except Exception as ex:
                return ex

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

    def get_table(self, name_table):
        with self.connection:
            self.cursor.execute(f"SELECT * FROM {name_table}")
            data = self.cursor.fetchall()
            self.cursor.execute(f"PRAGMA table_info({name_table});")
            columns = self.cursor.fetchall()
            return_colums = []
            for i in columns:
                return_colums.append(i[1])
        
        return data, return_colums
    
    ###работа над add worker и delete worker

    def get_data_worker(self, worker_id):
        with self.connection:
            self.cursor.execute(f"SELECT * FROM workers WHERE id = ?", (worker_id,))
            return_data = [row[0] for row in self.cursor.fetchall()]
        
        return return_data
    
    def add_worker(self, username, subname, job_title, salary, pasport, secret_key):
        with self.connection:
            self.cursor.execute(f"INSERT INTO workers (username, subname, job_title, salary, pasport, isWork, secret_key) VALUES (?, ?, ?, ?, ?, 0, ?)", (username, subname, job_title, salary, pasport, secret_key,))

    def remove_worker(self, worker_id):
        with self.connection:
            self.cursor.execute(f"DELETE FROM workers WHERE id = ?", (worker_id,))

    def set_work(self, pasport, meaning):
        with self.connection:
            if meaning:
                self.cursor.execute(f"UPDATE workers SET isWork = 1 WHERE pasport = ?", (pasport,))
            else:
                self.cursor.execute(f"UPDATE workers SET isWork = 0")

    def get_element_worker_id(self, id, element):
        with self.connection:
            self.cursor.execute(f"SELECT {element} FROM workers WHERE id = ?", (id,))
            return self.cursor.fetchone()[0]
        
    def get_secret_key(self, name, pasport):
        with self.connection:
            self.cursor.execute(f"SELECT secret_key FROM workers WHERE username = ? AND pasport = ?", (name, pasport,))
            return self.cursor.fetchone()[0]
        
    def get_bot_token(self):
        with self.connection:
            self.cursor.execute(f"SELECT bot_token FROM config")
            return self.cursor.fetchone()[0]
    
    def delete_worker_id(self, id_worker):
        with self.connection:
            self.cursor.execute(f"DELETE FROM workers WHERE id = ?", (id_worker))


    ##работа с формой логина и пароля

    def check_login_and_password(self, username, pasport):
        with self.connection:
            self.cursor.execute(f"""
                SELECT username, pasport, user_id
                FROM workers
                WHERE username = ? AND pasport = ?
            """, (username, pasport))

            row = self.cursor.fetchone()
            if row and all(row):
                print(row[0])  # username
                print(row[1])  # pasport
                print(row[2])  # user_id
                return True
            else:
                return False
            
    def get_user_id(self, pasport):
        with self.connection:
            self.cursor.execute(f"SELECT user_id FROM workers WHERE pasport = ?", (pasport,))
            return self.cursor.fetchone()[0]
        
    ##работа с проверкой ролей

    def get_role(self):
        with self.connection:
            self.cursor.execute(f"SELECT job_title FROM workers WHERE isWork = 1")
            return self.cursor.fetchone()[0]
    
    #запросы на обновления

    def update_worker(self, id, name, surname, job_title, salary, pasport, secret_key, user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE `workers` SET username = ?, subname = ?, job_title = ?, salary = ?, pasport = ?, secret_key = ?, user_id = ? WHERE `id` = ?", (name, surname, job_title, salary, pasport, secret_key, user_id, id,))

    def update_crypto(self, id, crypto, quantity):
        with self.connection:
            self.cursor.execute(f"UPDATE `crypto` SET name_crypto = ?, quantity = ? WHERE `ID` = ?", (crypto, quantity, id,))

    def update_card(self, id, name_bank, number_card, balance, turnover, turnover_sbp):
        with self.connection:
            self.cursor.execute(f"UPDATE `cards` SET name_bank = ?, number_card = ?, balance = ?, turnover = ?, turnover_sbp = ? WHERE `ID` = ?", (name_bank, number_card, balance, turnover, turnover_sbp, id,))

    def update_investor(self, id, name, summ, income, user_id):
        with self.connection:
            self.cursor.execute(f"UPDATE `investors` SET name = ?, summ = ?, income = ?, user_id = ? WHERE `ID` = ?", (name, summ, income, user_id, id,))

    #работа со сменой данных

    def get_element_id(self, table, id, element):
        with self.connection:
            self.cursor.execute(f"SELECT {element} FROM {table} WHERE id = ?", (id,))
            return self.cursor.fetchone()[0]
        

        

