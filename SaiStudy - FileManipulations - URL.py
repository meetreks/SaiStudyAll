#Time now to play with URI and URL
import urllib.request
from urllib.parse import urlparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup

url = "https://google.co.uk"
df =urllib.request.urlopen(url)
#print(df.read())
o = urlparse(url)
#print(o)
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'lxml')
#to strip all the HTML crap, just pass the text to BS.get_text and it is done
text = soup.get_text()
#print(text)
rows = soup.find_all('tr')
#print(rows[:10])
for row in rows:
    row_td = row.find_all('td')
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells,"lxml").getText()
#print(cleantext)


