import sys
import requests
import json

base_currency = str(sys.argv[1])
to = str(sys.argv[2])
amount = float(sys.argv[3])

url = 'https://api.exchangeratesapi.io/latest?base=' + base_currency
request = requests.get(url)
text = request.text
data = json.loads(text)
to_rate = data["rates"][to]  # find needed currency in the dictionary
convert = float(amount * to_rate)
print(convert)
