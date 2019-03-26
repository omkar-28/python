import requests
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
print(html)
#soup = BeautifulSoup(features="html.parser")
#print(soup.prettify())
