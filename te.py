import requests
import hashlib
import hmac
import time
import json
from config import api_key, api_secret

url = "https://api-testnet.bybit.com/v5/asset/transfer/inter-transfer"

payload = {
    "transferId": "re-6bca-c242-bc76-4e6df6cbab16",
    "coin": "USDT",
    "amount": "1",
    "fromAccountType": "SPOT",
    "toAccountType": "FUND"
}

# Генерация временной метки
timestamp = str(int(time.time() * 1000))

# Строка для подписи
signature_payload = f"{timestamp}POST/v5/asset/transfer/inter-transfer{json.dumps(payload, separators=(',', ':'))}"

# Вычисление подписи
signature = hmac.new(api_secret.encode('utf-8'), signature_payload.encode('utf-8'), hashlib.sha256).hexdigest()

headers = {
    'X-BAPI-API-KEY': api_key,
    'X-BAPI-TIMESTAMP': timestamp,
    'X-BAPI-RECV-WINDOW': '20000',
    'X-BAPI-SIGNATURE': signature
}

response = requests.post(url, headers=headers, json=payload)

print(response.text)