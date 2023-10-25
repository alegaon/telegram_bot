#!/usr/bin/env python
import requests

# URL API TRANSLATE
URL = 'https://es.libretranslate.com/translate'

# consumiendo json
rest = requests.get(URL).json

print(rest)

"""
res = await fetch("https://es.libretranslate.com/translate", {
	method: "POST",
	body: JSON.stringify({
		q: "",
		source: "auto",
		target: "es",
		format: "text",
		api_key: ""
	}),
	headers: { "Content-Type": "application/json" }
});

console.log(await res.json()); """