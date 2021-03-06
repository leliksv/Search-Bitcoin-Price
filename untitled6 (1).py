# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cgqjICh3V0DdF_vW-tTcxuCFZeS6kBiq
"""

from bs4 import BeautifulSoup
import requests
import time

def get_crypto_price(coin):
    url = "https://www.google.com/search?q="+coin+"+price"
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text, 'html.parser')
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div").text
    return text

def main():
    last_price = -1
    while True:
        crypto = 'bitcoin'
        price = get_crypto_price(crypto)
        if price != last_price:
            print(crypto + ' price:', price)
            last_price = price
    time.sleep(3)

main()

