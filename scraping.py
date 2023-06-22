import requests
import csv
from bs4 import BeautifulSoup

# GET request to extract the data.
web = 'https://trii.co/stock-list#companies'
result = requests.get(web)
content = result.text

#Extract html
soup = BeautifulSoup(content, 'lxml')
company = soup.find_all('div', class_ = 'card_stock')

#Empty list to add.
companies = []

#Item iteration.
for item_company in company:
    title = item_company.find('h2').getText()
    value = item_company.find('div', class_='title').getText()
    companies.append(title)
    companies.append(value)

#Create CSV file.
with open('company.csv', 'w') as file:
    csv_reader = csv.writer(file, delimiter=',')
    csv_reader.writerows(zip(companies))
