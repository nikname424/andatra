#from pybit.unified_trading import HTTP
from db import Database
import csv
import requests
import config as cf
import requests
import time
import hmac
import hashlib
import uuid
import json
db = Database('DataAnd.db')

def contains_only_digits(input_string):
    if not input_string:
        return False  # Если строка пуста, возвращаем False
    
    has_decimal_point = False  # Флаг для обнаружения десятичной точки

    # Проверяем каждый символ в строке
    for char in input_string:
        if char.isdigit():
            continue  # Если символ - цифра, идем дальше
        elif char == '.' and not has_decimal_point:
            has_decimal_point = True  # Обнаружена десятичная точка
        else:
            return False  # Если найден нецифровой символ или вторая десятичная точка, возвращаем False

    # Если не было нецифровых символов и допустимая структура для вещественного числа,
    # возвращаем True
    return True

def combo_pair(altcoin, liquidity):
    price = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={altcoin.upper()}{liquidity.upper()}')
    if price.status_code == 400:
        price = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={liquidity.upper()}{altcoin.upper()}')
        if price.status_code == 200:
            price = price.json()
            return float(price['price']), False # /

    elif price.status_code == 200:
        price = price.json()
        return float(price['price']), True # *

######################################

def read_csv(file_path): #нужен для чтения csv файлов
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return None

##########################################
def set_percent(summ, bank, SBP):
    if not SBP:
        limit = float(cf.limit_turnover_banks[bank.lower()])
        res = round(((summ * 100) / limit), 3)
        return res
    else:
        limit = float(cf.limit_turnover_banks_SBP[bank.lower()])
        res = round(((summ * 100) / limit), 1) - 100
        return res * (-1)

def return_percent(quantity, percent):
    percent /= 100
    percent_to_subtract = quantity * percent
    res =  quantity - percent_to_subtract
    return res

#################################################
def update_csv_cell(filename, row_number, column_number, new_value):
    try:
        with open(filename, mode='r', newline='') as file:
            rows = list(csv.reader(file))
        
        # Проверяем, что указанный номер строки и столбца существуют
        if row_number < 0 or row_number >= len(rows):
            print(f"Строка с номером {row_number} не существует в файле.")
            return
        
        if column_number < 0 or column_number >= len(rows[row_number]):
            print(f"Столбец с номером {column_number} не существует в строке {row_number}.")
            return
        
        # Обновляем значение в указанной ячейке
        rows[row_number][column_number] = new_value
        
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f"Значение в строке {row_number}, столбце {column_number} успешно обновлено.")
    except Exception as e:
        print(f"Произошла ошибка при обновлении ячейки: {str(e)}")
#####################################################################
def dict_to_string(input_dict):
    string_repr = "{\n"
    for key, value in input_dict.items():
        if value is None:
            value_str = "null"
        elif isinstance(value, str):
            value_str = f'"{value}"'
        else:
            value_str = str(value)
        string_repr += f'  "{key}": {value_str},\n'
    string_repr = string_repr.rstrip(',\n')  # Убрать последнюю запятую и перевод строки
    string_repr += "\n}"
    return string_repr
#####################################################################
def get_balance(symbol, type): #функция для принятия платежа
    api_key = 'd4pvo3cq5ofGv3uNMN'#db.get_from_config('api_key')
    api_secret = 'UqItzDQJEoe1R0FUn4aD7kRaO519JXcpHNoL' #db.get_from_config('api_secret')
    print(api_key, api_secret)
    # Установите метод и вызов API
    api_method = "GET"
    api_call = "v5/asset/transfer/query-account-coins-balance"

    # Установите параметры API
    account_type = type
    coin = symbol
    api_params = f"accountType={account_type}&coin={coin}"

    # Установите окно ожидания и отметку времени
    recv_window = 5000
    timestamp = str(int(time.time() * 1000))

    # Функция для создания подписи запроса
    def sign(secret, data):
        return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()

    # Создайте подпись с использованием секретного ключа и параметров API
    signature = sign(api_secret, f"{timestamp}{api_key}{recv_window}{api_params}")

    # Сформируйте URL и заголовки запроса
    url = f"https://api.bybit.com/{api_call}?{api_params}"
    headers = {
        "X-BAPI-API-KEY": api_key,
        "X-BAPI-TIMESTAMP": timestamp,
        "X-BAPI-SIGN": signature,
        "X-BAPI-RECV-WINDOW": str(recv_window)
    }

    # Выполните GET запрос
    response = requests.get(url, headers=headers)

    # Проверьте статус код ответа
    return response.json()

'''def proper_pare(from_crypto, to_crypto): #фунция для проверки пары
    try:
        session = HTTP(testnet=True)
        res = session.get_mark_price_kline(
        category="linear",
        symbol=from_crypto + to_crypto,
        interval=15,
        start=1670601600000,
        end=1670608800000,
        limit=1,)
        return "Sell", from_crypto + to_crypto
    except:
        return "Buy", to_crypto + from_crypto'''
    
def proper_pare(from_crypto, to_crypto):
    url = "https://api.bybit.com/v2/public/tickers"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        tickers = data.get("result", [])
        if tickers is not None:
            for ticker in tickers:
                if ticker["symbol"] == from_crypto + to_crypto:
                    return "Sell", from_crypto + to_crypto
                else:
                    return "Buy", to_crypto + from_crypto
    else:
        print(f"Ошибка при запросе данных: {response.status_code}")

def change_money(from_crypto, to_crypto, quantity): #функция для обмена криптовалюты
    api_key = db.get_from_config('api_key')
    api_secret = db.get_from_config('api_secret')
    url = "https://api.bybit.com/v5/order/create"

    def sign(secret, data):
        return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()

    #payload2 = "{\n  \"category\": \"spot\",\n  \"symbol\": \"BTCUSDT\",\n  \"isLeverage\": 0,\n  \"side\": \"Sell\",\n  \"orderType\": \"Market\",\n  \"qty\": \"0.002\",\n  \"triggerPrice\": null,\n  \"triggerDirection\": null,\n  \"triggerBy\": null,\n  \"orderFilter\": null,\n  \"orderIv\": null,\n  \"timeInForce\": \"GTC\",\n  \"positionIdx\": 0,\n  \"takeProfit\": null,\n  \"stopLoss\": null,\n  \"tpTriggerBy\": null,\n  \"slTriggerBy\": null,\n  \"reduceOnly\": false\n}"
    side, symbol = proper_pare(from_crypto, to_crypto)
    payload2 = f'{{\n  "category": "spot",\n  "symbol": "{symbol}",\n  "isLeverage": 0,\n  "side": "{side}",\n  "orderType": "Market",\n  "qty": "{quantity}",\n  "triggerPrice": null,\n  "triggerDirection": null,\n  "triggerBy": null,\n  "orderFilter": null,\n  "orderIv": null,\n  "timeInForce": "GTC",\n  "positionIdx": 0,\n  "takeProfit": null,\n  "stopLoss": null,\n  "tpTriggerBy": null,\n  "slTriggerBy": null,\n  "reduceOnly": false\n}}'
    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': str(int(time.time() * 1000)),
        'X-BAPI-RECV-WINDOW': '20000',
        'X-BAPI-SIGN': sign(api_secret, f"{str(int(time.time() * 1000))}{api_key}{20000}{payload2}")
    }

    response = requests.request("POST", url, headers=headers, data=payload2)

    return response.json()
