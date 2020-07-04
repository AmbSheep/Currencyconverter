#!usr/bin/env python3
import sys
import requests


def convert(base, to, amount):
    url = 'https://api.exchangeratesapi.io/latest?base=' + base
    data = requests.get(url).json()
    to_rate = data["rates"][to]  # find required currency in the dictionary
    return amount * to_rate


if __name__ == "__main__":
    base = str(sys.argv[1])
    to = str(sys.argv[2])
    amount = float(sys.argv[3])
    print(convert(base, to, amount))
