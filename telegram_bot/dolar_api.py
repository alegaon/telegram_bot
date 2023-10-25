#!/usr/bin/env python
import requests

# url dolar api
URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

# consumiendo json
json = requests.get(URL).json()

# dolar compar
# dolar venta
for index, emoji in enumerate(('🟢', '🔵')):
    compra = json[index]['casa']['compra'][:-1]
    venta = json[index]['casa']['venta'][:-1]


