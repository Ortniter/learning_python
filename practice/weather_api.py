# https://api.darksky.net/forecast/4141b0f2514be7d396158a3628b6eb29/46.29,30.44?exclude=[hourly,daily,flags]

import requests
from json import loads, JSONDecodeError
import sqlite3
from time import sleep
from datetime import datetime


class WeatherAPIWorker:
    def __init__(self, api_key, lat, lon, lang):
        self.api_key = api_key
        self.base_api_url = "https://api.darksky.net/forecast"
        self.lat = lat
        self.lon = lon
        self.lang = lang
        self.excluded_blocks = ""
        self.name = f'({lat},{lon}).db'
        self.while_mode = False
        self.mode = 'hourly'

    def _prepare_db(self):
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        cursor.execute(
            '''CREATE TABLE weather (timestamp, summary, temperature)''')
        connection.commit()
        connection.close()

    def _process_data(self, row_data):
        try:
            json_data = loads(row_data)
            return self._save_data(json_data)
        except JSONDecodeError as e:
            print(e)
        except Exception as e:
            print(e)

    def _save_data(self, data):
        if self.while_mode:
            with sqlite3.connect(self.name) as db:
                timestamp = int(data['currently']['time'])
                time = datetime.fromtimestamp(timestamp)
                cursor = db.cursor()
                cursor.execute(
                    f"INSERT INTO weather VALUES ('{str(time)}', '{data['currently']['summary']}', '{data['currently']['temperature']}')")
                db.commit()
        else:
            with sqlite3.connect(self.name) as db:
                data = data[f"{self.mode}"]["data"]
                temperature = 'temperatureHigh' if self.mode == 'daily' else 'temperature'
                for period in data:
                    timestamp = int(period['time'])
                    time = datetime.fromtimestamp(timestamp)
                    cursor = db.cursor()
                    cursor.execute(
                        f"INSERT INTO weather VALUES ('{str(time)}', '{period['summary']}', '{period[temperature]}')")
                db.commit()

    def saving_current_weather(self, sleep_sec):
        self.while_mode = True
        self.name = 'current_w_' + self.name
        self.excluded_blocks = "hourly, daily, flags"
        try:
            self._prepare_db()
        except sqlite3.OperationalError:
            print('DataBase already exists')
        while True:
            url = f"{self.base_api_url}/{self.api_key}/{self.lat},{self.lon}?exclude=[{self.excluded_blocks}]&units=auto&lang={self.lang}"
            response = requests.get(url)
            if response.status_code == 200:
                self._process_data(response.text)
            else:
                print(f'API response is {response.status_code}')
            sleep(sleep_sec)

    def saving_hourly(self):
        self.while_mode = False
        self.name = 'hourly_w_' + f'({self.lat},{self.lon}).db'
        self.excluded_blocks = "currently, daily, flags"
        self.mode = 'hourly'
        try:
            self._prepare_db()
        except sqlite3.OperationalError:
            print('DataBase already exists')
        url = f"{self.base_api_url}/{self.api_key}/{self.lat},{self.lon}?exclude=[{self.excluded_blocks}]&units=auto&lang={self.lang}"
        response = requests.get(url)
        if response.status_code == 200:
            self._process_data(response.text)
            print('Everything saved to DB')
        else:
            print(f'API response is {response.status_code}')

    def saving_daily(self):
        self.while_mode = False
        self.name = 'daily_w_' + f'({self.lat},{self.lon}).db'
        self.excluded_blocks = "currently, hourly, flags"
        self.mode = 'daily'
        try:
            self._prepare_db()
        except sqlite3.OperationalError:
            print('DataBase already exists')
        url = f"{self.base_api_url}/{self.api_key}/{self.lat},{self.lon}?exclude=[{self.excluded_blocks}]&units=auto&lang={self.lang}"
        response = requests.get(url)
        if response.status_code == 200:
            self._process_data(response.text)
            print('Everything saved to DB')
        else:
            print(f'API response is {response.status_code}')


key = "4141b0f2514be7d396158a3628b6eb29"
lat_w = 46.29
lon_w = 30.44

worker = WeatherAPIWorker(api_key=key, lat=lat_w, lon=lon_w, lang='uk')

worker.saving_daily()
