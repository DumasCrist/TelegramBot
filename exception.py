import requests
import json
from config import keys

class APIException(Exception):
    pass

class TelegramConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f' не удалось обработать валюту{quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'не удалось обработать валюту{base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'не удалось обработрать количество {amount}')
        url = f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}'
        headers = {
            "apikey": "193948937d0429bd85b517a30413f154fc77058a90b438a9186d4566f057ac26"
        }
        r = requests.get(url, headers)
        new_price = json.loads(r.content)[base_ticker]
        return new_price
