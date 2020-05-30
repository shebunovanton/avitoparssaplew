import requests
from bs4 import BeautifulSoup
import csv

def html_data(data):
    soup = BeautifulSoup(data,'lxml')
    
    tr = soup.find_all('div', class_="item_table-wrapper")
  
    for trs in tr:
        
        try:
            name = trs.find('h3').text
        except:
            name = ''
        try:
            adress = 'https://www.avito.ru' + trs.find('h3').find('a').get('href')
        except:
            adress = ''
        try:
            price = trs.find('div', class_='snippet-price-row').text
        except:
            price = ''    
        data = {
            'name': name,
            'adress':adress,
            'price':price

        }
        csv_writ(data)
def html_resp(html):
    r = requests.get(html)
    if r.ok: # 200  ## 403 404
        return r.text
    print(r.status_code)


def csv_writ(data):
    with open("applew.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow((
            data['name'],
            data['adress'],
            data['price']

        ))

def main():
    url = 'https://www.avito.ru/tambov/chasy_i_ukrasheniya/kupit-chasy-ASgBAgICAUTQAYYG?q=apple+watch'
    html_data(html_resp(url))
    print('Parss ')

if __name__ == '__main__':
    main()
    