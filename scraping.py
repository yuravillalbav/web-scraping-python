import requests
import pandas as pds
from bs4 import BeautifulSoup

# GET request to extract the data.
web = 'https://trii.co/stock-list#companies'
result = requests.get(web)
content = result.text

# Extract html
soup = BeautifulSoup(content, 'html.parser')
company = soup.find_all('div', class_='card_stock')

# Empty list to add.
companies = list()
values = list()
images = list()

# Item iteration.
for item_company in company:
    title = item_company.find('h2').getText()
    value = item_company.find('div', class_='title').getText()
    img = item_company.find('img').get('src')
    companies.append(title)
    values.append(value)
    images.append(img)


dictionary = {'Company': companies, 'Values': values, 'Imagen': images}
print(dictionary)

# Create and save CSV file.
columns = pds.DataFrame(dictionary, columns=['Company', 'Values', 'Imagen'])
columns.to_csv('company_two.csv')
