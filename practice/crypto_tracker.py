"""
Нужно реализовать класс-адаптер, который будет:
1. Раз в 1 минуту получать цену на Bitcoin от
https://www.quandl.com/api/v3/datasets/BCHARTS/BITSTAMPUSD
2. Распаковывать нужные данные
3. Сохранять их во внешний словарь вида {"2020-03-19": 5340}

Импорты:
from time import sleep
import requests
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('input', action='store', type=int, default=1)


class CryptoPrice:
    def __init__(self, coins):
        self.url = 'https://coinmarketcap.com/'
        self.coins = coins

    def get_html(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        print(f'Response status code: {r.status_code}')
        return None

    def get_data(self, html):
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find('tbody').find_all('tr')[:self.coins]

        string = ''
        for tr in trs:
            tds = tr.find_all('td')
            price = tds[3].text
            name = tds[1].text
            time = datetime.now().strftime("%H:%M:%S")
            string += f'{name} -- {price}\ntime of check -- {time}\n{5 * "_____"}\n'

        return string

    def save(self, data):
        with open('crypto.txt', 'a') as file:
            file.write(data)

    def work(self):
        # while True:
        html = self.get_html(self.url)
        data = self.get_data(html)
        self.save(data)
        with open('crypto.txt', 'r') as file:
            print(file.read())
            # sleep(60)


args = my_parser.parse_args()

crypto = CryptoPrice(args.input)
crypto.work()
