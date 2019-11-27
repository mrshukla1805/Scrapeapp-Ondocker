from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('http://books.toscrape.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name','price'])

d={}
for article in soup.find_all('article'):

	name = article.h3.a.text
	price = article.find('div',class_="product_price").p.text.encode('utf-8')

	d[name]=price
	csv_writer.writerow([name,price])

csv_file.close()
print(d)

