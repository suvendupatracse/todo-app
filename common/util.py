import requests


def my_div(num1, num2):
    return num1 / num2


def get_crypto_values():
    headers = {"User-Agent": "Mozilla/5.0"}
    url = "https://api.cryptonator.com/api/ticker/btc-usd"
    res = requests.get(url, headers=headers)
    return res.json()