from bs4 import BeautifulSoup
import requests

url = 'http://www.ctabustracker.com/bustime/eta/eta.jsp?id=15475'
r = requests.get(url)
s = BeautifulSoup(r.text,'html.parser')
