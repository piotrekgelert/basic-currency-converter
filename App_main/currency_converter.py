import json
import os
import sys

import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw
import requests
from UI.converter_ui import Ui_fm_main

currency = 'USD'
api_key = f'https://open.er-api.com/v6/latest/{currency}'
headers = {
    'User-Agent':\
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
}
# resp = requests.get(api_key)
# if resp.status_code == 200:
#     data = resp.json()

# print(data['rates'].keys())
    
class ConvertMoney(qtw.QWidget, Ui_fm_main):
    country_from, country_to = '', ''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_date()
        self.set_currencies()
        self.cbb_from
        self.cbb_from.activated.connect(self.get_from)
        self.cbb_to.activated.connect(self.get_to)

        # self.pb_clear_all.clicked.connect(self.get_currency(self.get_from))
        # self.pb_swap.clicked.connect(self.get_currency(self.get_to))
    
    def get_data(self, currency: str):
        api_key = f'https://open.er-api.com/v6/latest/{currency}'
        resp = requests.get(api_key)
        if resp.status_code == 200:
            data = resp.json()
            return data

    def set_date(self):
        self.lb_date.setText(self.get_data('USD')['time_last_update_utc'][:-6])
    
    def set_currencies(self):
        currency_names = self.get_json_data()
        names = []
        for x in currency_names.values():
            names.append(x['currency_code_name'])
        self.cbb_from.addItems(names)
        self.cbb_to.addItems(names)
    
    def get_from(self):
        self.get_currency(self.cbb_from.currentText())
    
    def get_to(self):
        self.get_currency(self.cbb_to.currentText())
    
    def get_currency(self, current_money):
        current_country = self.get_json_data()
        for x in current_country.values():
            if current_money == x['currency_code_name']:
                self.lb_message.setText(x['currency_country'])
    
    def get_json_data(self):
        file = r'D:\Python_PORTFOLIO\12_basic_currency_converter\App_main\currency_codes_code_name_countries.json'
        with open(file, 'r') as f:
            curr = json.load(f)
            return curr





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ConvertMoney()
    window.show()
    sys.exit(app.exec())

