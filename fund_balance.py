import requests
import time
import hmac
import hashlib
import uuid
from config import api_key, api_secret

def sing(api_secret, data):
    return hmac.new(api_secret.encode(), data.encode(), hashlib.sha256).hexdigest()

def generate_transfer_id():
    transfer_id = str(uuid.uuid4())
    return transfer_id

def get_balance(symbol, type):
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

'''def tes():
    url = "https://api.bybit.com/v5/asset/transfer/inter-transfer"

    api_call = "v5/asset/transfer/inter-transfer"
    transferid = generate_transfer_id()
    coin = "USDT"
    from_ = "FUND"
    to_ = "SPOT"
    
    api_params = f"transferId={transferid}&coin={coin}&amount={1}&fromAccountType={from_}&toAccountType={to_}"
    
    recv_window = 5000
    timestamp = str(int(time.time() * 1000))
    
    def sign(secret, data):
        return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()
    
    signature = sign(api_secret, f'{timestamp}{api_key}{recv_window}{api_params}')

    #payload = "{\n  \"transferId\": \"42c0cab0-6bca-c242-bc76-4e6df6cbab16\",\n  \"coin\": \"USDT\",\n  \"amount\": \"10\",\n  \"fromAccountType\": \"UNIFIED\",\n  \"toAccountType\": \"SPOT\"\n}"
    headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': f'{recv_window}',
    'X-BAPI-SIGN': signature
    }

    response = requests.request("POST", url, headers=headers)

    print(response.text)

tes()

def send_balance(symbol, quantity, from_, to_):
    # Укажите свои значения для API ключа и секрета

    url = "https://api-testnet.bybit.com/v5/asset/transfer/inter-transfer"

    # Пример использования функции
    transferid = generate_transfer_id()

    recv_window = '5000'
    timestamp = str(int(time.time() * 1000))

    api_params = f"transferId={transferid}&coin={symbol}&amount={str(quantity)}&fromAccountType={from_}&toAccountType={to_}"

    def sign(secret, data):
        return hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()
    
    signature = sign(api_secret, f'{timestamp}{api_key}{recv_window}{api_params}')

    headers = {
        'X-BAPI-API-KEY': api_key,
        'X-BAPI-TIMESTAMP': timestamp,
        'X-BAPI-RECV-WINDOW': recv_window,
        'X-BAPI-SIGN': signature,
    }

    response = requests.post(url, headers=headers)

    return response.json()'''

# Пример использования функции
#print(send_balance("USDT", 0.1, "FUND", "SPOT"))
#print(get_balance('USDT', 'FUND'))

