import requests

currency = 'USD'
api_key = f'https://open.er-api.com/v6/latest/{currency}'

resp = requests.get(api_key)
if resp.status_code == 200:
    data = resp.json()

print(data['rates'].keys())

