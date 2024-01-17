import json

# site = 'https://www.exchangerate-api.com/docs/supported-currencies'
# headers = {
#     'User-Agent':\
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
# }

# def requestor_soup(url):
#     resp = requests.get(url)
#     if resp.status_code == 200:
#         pass
#     else:
#         print(resp.status_code)
#     return bs(resp.content, 'lxml')

# soup = requestor_soup(site)

# tabs = soup.find_all(
#     'table'
# )
# # print(tabs[2])
# names = re.findall(r'\"left\"\>([a-zA-Z\s]{1,})\</td\>', str(tabs[2]))
# # print(names)

# currency_codes = []
# currency_names = []
# currency_country = []
# def third(ls:list):
#     res = []
#     count = 3
#     res.append(ls[0])
#     while len(ls) > 0:
#         if count > 0:
#             ls.pop(0)
#         else:
#             res.append(ls[0])
#             ls.pop(0)
#             count = 3
#         count -= 1
#     return res
# print(third(names))

# currency_codes.append(names[0])
# currency_names.append(names[1])
# currency_country.append(names[2])

# print(currency_codes)
# print(names[::3])


# currency_codes = []
# names_countries = []
# [currency_codes.append(x) if all([y.isupper() for y in x]) else names_countries.append(x) for x in names]
# print(len(currency_codes))
# # print(names_countries)

# currency_names = []
# currency_country = []
# [currency_country.append(x) if names_countries.index(x) % 2 == 0 else currency_names.append(x) for x in names_countries]
# print(len(currency_names))
# print(len(currency_country))


# name_code = []
# for code, name in it.zip_longest(currency_codes, currency_names):
#     name_code.append(f'{code} - {name}')

# print(name_code)


file = r'D:\Python_PORTFOLIO\12_basic_currency_converter\App_main\currency_name_country.txt'
results = {}
count = 0
while count < 161:
    with open(file, 'r', encoding='UTF-8') as tx:
        t = tx.read().splitlines()
        results[t[count].split('\t')[0]] = {
            'currency_code_name': '{} - {}'.format(t[count].split('\t')[0], t[count].split('\t')[1]),
            'currency_country': ''.join(['_' if z == ' ' else z for z in t[count].split('\t')[2].lower()])
            # 'currency_country': t[count].split('\t')[2]
        }
        # results['{} - {}'.format(t[count].split('\t')[0], t[count].split('\t')[1])] = {
        #     'currency_code': t[count].split('\t')[0],
        #     'currency_country': t[count].split('\t')[2]   
        # }
        count += 1

# print(results)
file_path = r'D:\Python_PORTFOLIO\12_basic_currency_converter\App_main\currency_codes_code_name_countries2.json'
with open(file_path, 'w') as f:
    json.dump(results, f)

# results = {'country': {'currency_code': 'CODE', 'currency_codes_names': 'CODE - name'}}

# file_json = r'D:\Python_PORTFOLIO\12_basic_currency_converter\App_main\currency_codes_code_name_countries.json'
# with open(file_json, 'r') as fn:
#     f = fn.read()
#     d = json.loads(f)
#     for x in d.values():
#         country = ''.join(['_' if z == ' ' else z for z in x['currency_country'].lower()])
#         print(country)
        # print(x['currency_country'])
    # print(d.values()['currency_country'])