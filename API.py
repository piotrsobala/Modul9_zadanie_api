import requests
import pandas as pd

# Pobierz dane z API
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates_list = data[0]['rates']

df = pd.DataFrame(rates_list)

df_csv = df[['currency', 'code', 'bid', 'ask']]

df_csv.to_csv('exchange_rates.csv', sep=';', index=False)