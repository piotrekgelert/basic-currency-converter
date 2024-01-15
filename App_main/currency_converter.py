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
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_date()
        self.set_currencies()
        self.pb_clear.clicked.connect(self.get_from_currency)
        self.pb_swap.clicked.connect(self.get_to_currency)
    
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
        self.cbb_from.addItems(currency_names.keys())
        self.cbb_to.addItems(currency_names.keys())
    
    def get_from_currency(self):
        print(self.cbb_from.currentText())
        currency_name = self.get_json_data()
        self.lb_short_from.setWindowIcon(qtg.QIcon())
        self.lb_short_from.setText(currency_name[self.cbb_from.currentText()]['currency_country'])
        # if 
        # self.lb_short_from.
    
    def get_to_currency(self):
        print(self.cbb_to.currentText())
    
    def get_json_data(self):
        file = r'D:\Python_PORTFOLIO\12_basic_currency_converter\App_main\currency_countries_codes_names.json'
        with open(file, 'r') as f:
            curr = json.load(f)
            return curr





if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = ConvertMoney()
    window.show()
    sys.exit(app.exec())

