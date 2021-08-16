# HTTP Packages

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
import urllib.request
import json
import textwrap

url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224'

with urllib.request.urlopen(url) as f:
    text = f.read()
    decoded_text = text.decode('utf-8')
    print(textwrap.fill(decoded_text, width=50))

print()

objects = json.loads(decoded_text)
print(objects.keys())

print(objects['items'])