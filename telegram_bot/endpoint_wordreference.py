#!/usr/bin/env python
import requests

# url dolar api
URL = 'https://www.wordreference.com/es/translation.asp?tranword=footwork'

# consumiendo json
json = requests.get(URL).text

print(json[id])