import requests
from bs4 import BeautifulSoup as bs
import re

proxy = "https://piratebay-proxylist.net"

Base_url = "https://tpbbazpirate.in/search.php?q="
query = "Interstellar"
url_ender = "&all=on&search=Pirate+Search&page=0&orderby="
url = Base_url + query + url_ender
print(url)
response = requests.get(url)
print(response.text)
soup = bs(response.content, 'lxml')

