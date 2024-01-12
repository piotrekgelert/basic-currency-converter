import itertools as it
import re

import lxml
import requests
from bs4 import BeautifulSoup as bs

site = 'https://www.exchangerate-api.com/docs/supported-currencies'
headers = {
    'User-Agent':\
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
}

def requestor_soup(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        pass
    else:
        print(resp.status_code)
    return bs(resp.content, 'lxml')

soup = requestor_soup(site)

tabs = soup.find_all(
    'table'
)
# print(tabs[2])
names = re.findall(r'\"left\">([a-zA-Z\s]{1,})\</td\>', str(tabs[2]))

currency_codes = []
names_countries = []
[currency_codes.append(x) if all([y.isupper() for y in x]) else names_countries.append(x) for x in  names]
print(len(currency_codes))

currency_names = []
currency_country = []
[currency_country.append(x) if names_countries.index(x) % 2 == 0 else currency_names.append(x) for x in names_countries]
print(len(currency_names))
print(len(currency_codes))


# name_code = []
# for code, name in it.zip_longest(currency_codes, currency_names):
#     name_code.append(f'{code} - {name}')

# print(name_code)


