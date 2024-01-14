import requests

currency = 'USD'
api_key = f'https://open.er-api.com/v6/latest/{currency}'
headers = {
    'User-Agent':\
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
}
resp = requests.get(api_key)
if resp.status_code == 200:
    data = resp.json()

print(data['rates'].keys())

