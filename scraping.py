import requests
import csv
from bs4 import BeautifulSoup

# GET request to extract the data.
web = 'https://trii.co/stock-list#companies'
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, 'html')

# We identify the element where the desired information is located.
list = soup.find(id = 'local')

# We iterate through the elements to extract the data.
for data  in list:
    company = list.find('ul', id = 'paginated-list').get_text()
    print(company)

# We export the data obtained to an excel file.
with open('./scrape.csv', 'w') as test_file:
    csv_test = csv.writer(test_file, dialect='excel')
    csv_test.writerows(zip(company))