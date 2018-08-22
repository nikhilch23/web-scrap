import urllib.request as urllib2
from bs4 import BeautifulSoup


quote_page = "http://www.bloomberg.com/quote/SPX:IND" #url of the page going to be scrapped

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


name = soup.find(string = "SPX:IND")
print(name)


name_box = soup.find('h1', attrs={'class':'companyName__99a4824b'})
name = name_box.text.strip()
print(name)

price_box = soup.find('span', attrs={'class':'priceText__1853e8a5'})
price = price_box.text
print(price)


