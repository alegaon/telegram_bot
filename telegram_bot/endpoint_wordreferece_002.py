#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

URL = 'https://www.wordreference.com/'

# consumiendo json
html_doc = requests.get(URL).text

soup = BeautifulSoup(html_doc, 'html.parser')


print(soup.input('si'))