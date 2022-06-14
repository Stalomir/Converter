import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0]['rates']
with open('table.csv','w',newline='', encoding="utf-8") as csvfile:
    table = csv.writer(csvfile, delimiter=';')
    table.writerow(rates[0].keys())
    for i in rates:
        table.writerow(i.values()) 

    