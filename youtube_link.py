import requests
from bs4 import BeautifulSoup as soup

site = requests.get('https://www.youtube.com/playlist?list=PLbcjWbaVdChfTwp0-FFYZ1WFy3Zkgm8oS')
si = soup(site.text,'html5lib')
# print(si.prettify)
for url in si.find_all('a'):
    print(url.get('href'))
